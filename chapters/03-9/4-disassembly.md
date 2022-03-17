---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Zerlegung

Das Standard-Modul [dis](https://docs.python.org/3/library/dis.html) erlaubt die Analyse von CPython *Bytecode* durch *Zerlegung* (engl. disassembling).
Das Modul erlaubt es uns kleine ``Python``-Codeblöcke in den entsprechenden *Bytecode* zu überführen und diesen dann in verständlicher Form anzuzeigen.
Dadurch erhalten wir Einblicke in den übersetzten Code!

Blicken Sie auf folgenden ``Python``-Code:

```{code-cell} python3
def func1():
    return 7 * 21233

def func2():
    x = 21233
    return x * 7
```

Beide Funktionen berechnen das Produkt aus 7 und 21233 und liefern das Ergebnis zurück.

```{exercise} Laufzeit
:label: exercise-run-time-simple-mult

Welche der beiden Funktionen benötigt bei Ausführung weniger Laufzeit?
Oder benötigen beide im Schnitt die gleiche Laufzeit?
Begründen Sie Ihre Antwort.
```

```{solution} exercise-run-time-simple-mult
:label: solution-run-time-simple-mult
:class: dropdown

``func2`` benötigt im Schnitt mehr Zeit, da durch die zusätzliche Initialisierung einer Variablen die mehr Operationen benötigt werden.
```

Sie können die oben gestellte Frage eigentlich gar nicht beantworten, denn wir wissen nicht welche Optimierungen Übersetzer und Interpreter durchführen.
Wir können uns aber ansehen, welchen *Bytecode* der Übersetzer erzeugt.

```{code-cell} python3
import dis

dis.dis(func1)
```

```{code-cell} python3
dis.dis(func2)
```

Der Code der Funktion ``func1`` wird zu zwei *Bytecode*-Befehlen disassambled.
``LOAD_CONST`` scheint eine konstante Zahl zu laden und ``RETURN_VALUE`` scheint diese zurückzuliefern.
Wo ist aber unsere Multiplikation hin?
Der Übersetzer optimiert unseren Code und ersetzt ``7 * 21233`` durch ``148631``.
In anderen Worten, der Übersetzer berechnet das Ergebnis selbst.

Für ``func2`` macht er dies nicht.
Hier sehen wir stattdessen zweimal ``LAOD_CONST`` und die Multiplikation ``BINARY_MULTIPLY``.
Zusätzlich wird in den Speicher geschrieben (``STORE_FAST``) und vom Speicher gelesen (``LOAD_FAST``).
Was der Interpreter aus diesen Befehlen macht ist wiederum eine andere Frage.

Lassen Sie uns zum Spaß den *Bytecode* sinnvollerer Funktionen analysieren.

```{code-cell} python3
def add(a, b):
    return a + b

dis.dis(add)
```

```{code-cell} python3
def mexp(a, b):
    return a**b

dis.dis(mexp)
```

Wir sehen, dass der Exponentialoperator nicht durch die Multiplikation in *Bytecode* realisiert wird, sondern erst durch die Interpretation der ``BINARY_POWER``-Anweisung realisiert wird.
``BINARY_POWER`` ist wiederum ein Aufruf einer *built-in* ``C``-*Funktion*.
Den Code hierfür finden Sie auf [GitHub](https://github.com/python/cpython/blob/109fc2792a490ee5cd8a423e17d415fbdedec5c8/Objects/longobject.c#L4244-L4447) und im folgenden Codeblock (bitte nicht erschrecken):

```c
/* pow(v, w, x) */
static PyObject *
long_pow(PyObject *v, PyObject *w, PyObject *x)
{
    PyLongObject *a, *b, *c; /* a,b,c = v,w,x */
    int negativeOutput = 0;  /* if x<0 return negative output */

    PyLongObject *z = NULL;  /* accumulated result */
    Py_ssize_t i, j, k;             /* counters */
    PyLongObject *temp = NULL;

    /* 5-ary values.  If the exponent is large enough, table is
     * precomputed so that table[i] == a**i % c for i in range(32).
     */
    PyLongObject *table[32] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                               0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};

    /* a, b, c = v, w, x */
    CHECK_BINOP(v, w);
    a = (PyLongObject*)v; Py_INCREF(a);
    b = (PyLongObject*)w; Py_INCREF(b);
    if (PyLong_Check(x)) {
        c = (PyLongObject *)x;
        Py_INCREF(x);
    }
    else if (x == Py_None)
        c = NULL;
    else {
        Py_DECREF(a);
        Py_DECREF(b);
        Py_RETURN_NOTIMPLEMENTED;
    }

    if (Py_SIZE(b) < 0 && c == NULL) {
        /* if exponent is negative and there's no modulus:
               return a float.  This works because we know
               that this calls float_pow() which converts its
               arguments to double. */
        Py_DECREF(a);
        Py_DECREF(b);
        return PyFloat_Type.tp_as_number->nb_power(v, w, x);
    }

    if (c) {
        /* if modulus == 0:
               raise ValueError() */
        if (Py_SIZE(c) == 0) {
            PyErr_SetString(PyExc_ValueError,
                            "pow() 3rd argument cannot be 0");
            goto Error;
        }

        /* if modulus < 0:
               negativeOutput = True
               modulus = -modulus */
        if (Py_SIZE(c) < 0) {
            negativeOutput = 1;
            temp = (PyLongObject *)_PyLong_Copy(c);
            if (temp == NULL)
                goto Error;
            Py_DECREF(c);
            c = temp;
            temp = NULL;
            _PyLong_Negate(&c);
            if (c == NULL)
                goto Error;
        }

        /* if modulus == 1:
               return 0 */
        if ((Py_SIZE(c) == 1) && (c->ob_digit[0] == 1)) {
            z = (PyLongObject *)PyLong_FromLong(0L);
            goto Done;
        }

        /* if exponent is negative, negate the exponent and
           replace the base with a modular inverse */
        if (Py_SIZE(b) < 0) {
            temp = (PyLongObject *)_PyLong_Copy(b);
            if (temp == NULL)
                goto Error;
            Py_DECREF(b);
            b = temp;
            temp = NULL;
            _PyLong_Negate(&b);
            if (b == NULL)
                goto Error;

            temp = long_invmod(a, c);
            if (temp == NULL)
                goto Error;
            Py_DECREF(a);
            a = temp;
        }

        /* Reduce base by modulus in some cases:
           1. If base < 0.  Forcing the base non-negative makes things easier.
           2. If base is obviously larger than the modulus.  The "small
              exponent" case later can multiply directly by base repeatedly,
              while the "large exponent" case multiplies directly by base 31
              times.  It can be unboundedly faster to multiply by
              base % modulus instead.
           We could _always_ do this reduction, but l_divmod() isn't cheap,
           so we only do it when it buys something. */
        if (Py_SIZE(a) < 0 || Py_SIZE(a) > Py_SIZE(c)) {
            if (l_divmod(a, c, NULL, &temp) < 0)
                goto Error;
            Py_DECREF(a);
            a = temp;
            temp = NULL;
        }
    }

    /* At this point a, b, and c are guaranteed non-negative UNLESS
       c is NULL, in which case a may be negative. */

    z = (PyLongObject *)PyLong_FromLong(1L);
    if (z == NULL)
        goto Error;

    /* Perform a modular reduction, X = X % c, but leave X alone if c
     * is NULL.
     */
#define REDUCE(X)                                       \
    do {                                                \
        if (c != NULL) {                                \
            if (l_divmod(X, c, NULL, &temp) < 0)        \
                goto Error;                             \
            Py_XDECREF(X);                              \
            X = temp;                                   \
            temp = NULL;                                \
        }                                               \
    } while(0)

    /* Multiply two values, then reduce the result:
       result = X*Y % c.  If c is NULL, skip the mod. */
#define MULT(X, Y, result)                      \
    do {                                        \
        temp = (PyLongObject *)long_mul(X, Y);  \
        if (temp == NULL)                       \
            goto Error;                         \
        Py_XDECREF(result);                     \
        result = temp;                          \
        temp = NULL;                            \
        REDUCE(result);                         \
    } while(0)

    if (Py_SIZE(b) <= FIVEARY_CUTOFF) {
        /* Left-to-right binary exponentiation (HAC Algorithm 14.79) */
        /* http://www.cacr.math.uwaterloo.ca/hac/about/chap14.pdf    */
        for (i = Py_SIZE(b) - 1; i >= 0; --i) {
            digit bi = b->ob_digit[i];

            for (j = (digit)1 << (PyLong_SHIFT-1); j != 0; j >>= 1) {
                MULT(z, z, z);
                if (bi & j)
                    MULT(z, a, z);
            }
        }
    }
    else {
        /* Left-to-right 5-ary exponentiation (HAC Algorithm 14.82) */
        Py_INCREF(z);           /* still holds 1L */
        table[0] = z;
        for (i = 1; i < 32; ++i)
            MULT(table[i-1], a, table[i]);

        for (i = Py_SIZE(b) - 1; i >= 0; --i) {
            const digit bi = b->ob_digit[i];

            for (j = PyLong_SHIFT - 5; j >= 0; j -= 5) {
                const int index = (bi >> j) & 0x1f;
                for (k = 0; k < 5; ++k)
                    MULT(z, z, z);
                if (index)
                    MULT(z, table[index], z);
            }
        }
    }

    if (negativeOutput && (Py_SIZE(z) != 0)) {
        temp = (PyLongObject *)long_sub(z, c);
        if (temp == NULL)
            goto Error;
        Py_DECREF(z);
        z = temp;
        temp = NULL;
    }
    goto Done;

  Error:
    Py_CLEAR(z);
    /* fall through */
  Done:
    if (Py_SIZE(b) > FIVEARY_CUTOFF) {
        for (i = 0; i < 32; ++i)
            Py_XDECREF(table[i]);
    }
    Py_DECREF(a);
    Py_DECREF(b);
    Py_XDECREF(c);
    Py_XDECREF(temp);
    return (PyObject *)z;
}
```