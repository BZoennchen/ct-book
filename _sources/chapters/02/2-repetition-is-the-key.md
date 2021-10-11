---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Wiederholung als Grundlage

```{code-cell} ipython3
def sum_sqrt(n):
    sum_sqrt = 0
    for i in range(n):
        sum_sqrt += (i+1) * (i+1)
    return sum_sqrt
```

Die Anzahl der auszuführenden Anweisungen steigt linear mit ``n``, doch der Programmiercode bleibt unverändert.
Hierin liegt die ganze Magie: **Wiederholung**!
