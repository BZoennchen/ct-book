# Wiederholung als Grundlage

def sum_sqrt(n):
    sum_sqrt = 0
    for i in range(n):
        sum_sqrt += (i+1) * (i+1)
    return sum_sqrt

Die Anzahl der auszuführenden Anweisungen steigt linear mit ``n``, doch der Programmiercode bleibt unverändert.
Hierin liegt die ganze Magie: **Wiederholung**!