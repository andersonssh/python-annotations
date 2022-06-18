# python-annotations

This repository was created to store my notes about python. 
To assist me in creating new folders to store new notes, 
I created a script to create the folder structure according 
to the pattern I defined.


For the structure of the new annotations I chose a main theme, 
which currently consists of: 
**functions**, **apps**, **concepts**, **quick_tests** and **others**.

* functions: tests of functions and algorithms.
* apps: apps created to train new acquired knowledge.
* concepts: notes on theoretical subjects.
* quick_tests: quick tests of daily tasks.
* others: random language subjects.

The script creates the following structure for each main theme:
```bash
python-annotations
├── <maintheme>
│   ├── <subject>
│   │   ├── quick_note.txt
│   │   ├── README.md
│   │   └── references.json
```
Some themes may choose not to create some of the script files.
These settings can be found in ```python-annotations/config.json```