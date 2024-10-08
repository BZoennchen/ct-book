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

# Quiz

```{code-cell} python3
---
tags: 
    - remove-input
---
quiz=[{
        "question": "Welche Fähigkeiten zählen wir zum Computational Thinking?",
        "type": "many_choice",
        "answers": [
            {
                "answer": "Abstraktes Denken",
                "correct": True,
                "feedback": "Richtig."
            },
            {
                "answer": "Probleme in Teilprobleme zerlegen",
                "correct": True,
                "feedback": "Richtig."
            },
            {
                "answer": "Strukturen erkennen",
                "correct": True,
                "feedback": "Richtig."
            },
            {
                "answer": "Algorithmen entwerfen",
                "correct": True,
                "feedback": "Richtig."
            },
            {
                "answer": "Software entwickeln",
                "correct": False,
                "feedback": "Falsch."
            },
            {
                "answer": "Die Abarbeitung wiederholender Aufgaben",
                "correct": False,
                "feedback": "Falsch."
            }
        ]
    },
    {
        "question": "Welche Aussagen sind korrekt?",
        "type": "many_choice",
        "answers": [
            {
                "answer": "Informatik ist eine Wissenschaftsdiziplin",
                "correct": True,
                "feedback": "Richtig."
            },
            {
                "answer": "CT ist eine Denkweise",
                "correct": True,
                "feedback": "Richtig."
            },
            {
                "answer": "CT ist ein Teilgebiet der Informatik",
                "correct": False,
                "feedback": "Falsch."
            },
            {
                "answer": "CT ist eine Fähigkeit die Informatiker*innen lernen",
                "correct": True,
                "feedback": "Richtig."
            },
            {
                "answer": "Informatik ist die Wissenschaft der Computer",
                "correct": False,
                "feedback": "Falsch."
            }
        ]
    },
    {
        "question": "Weshalb kann ein sehr kurzer Programmcode zu einer langen Ausführungszeit führen?",
        "type": "many_choice",
        "answers": [
            {
                "answer": "Weil das Programm Fehler enthält",
                "correct": False,
                "feedback": "Richtig."
            },
            {
                "answer": "Weil ein bestimmter Programmcode wiederholt ausgeführt wird",
                "correct": True,
                "feedback": "Richtig."
            },
            {
                "answer": "Weil es Abzweigungen im Programmcode gibt",
                "correct": False,
                "feedback": "Falsch."
            }
        ]
    }]

from jupyterquiz import display_quiz
display_quiz(quiz, border_radius=2, lang='de')
```