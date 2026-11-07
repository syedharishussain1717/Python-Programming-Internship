# Python Programming Internship – Progree

A collection of Python programming tasks and practical projects completed as part of my **Python Programming Internship at Progree**. This repository demonstrates my learning journey, programming fundamentals, problem-solving abilities, and hands-on experience with Python.

## About the Internship

The internship focuses on developing practical Python programming skills through structured coding tasks and real-world problem-solving exercises.

**Internship Details:**
- **Organization:** Progree
- **Role:** Python Programming Intern
- **Domain:** Python Programming
- **Programming Language:** Python 3

## Tasks & Projects

### Task 01 – Fibonacci Series
Developed a Python program to generate the Fibonacci sequence using programming fundamentals, loops, functions, and basic input validation.

**Key Concepts:** Functions, Loops, Variables, Input Validation.

### Task 02 – Fibonacci Generation Module
Developed a reusable Python module for generating Fibonacci numbers with proper input validation, exception handling, and execution-time benchmarking using the `timeit` module.

**Key Concepts:** Modular Programming, Exception Handling, Code Reusability, Performance Benchmarking.

### Task 03 – Automated File Operations & Text Parsing
Developed a Python-based automation script to organize files by extension, extract email addresses and transaction details using Regular Expressions, and export extracted information into structured CSV files.

**Key Concepts:** File Handling, Regular Expressions (RegEx), CSV Processing, Automation, Python Standard Libraries.

### Task 04 – Production-Ready Multi-Intent Rule-Based Chatbot
Developed an interactive, terminal-based chatbot that understands multiple user intents, remembers the user's name, guides users through nested help menus, and handles unknown or invalid input gracefully. The bot is built from small, modular handler functions routed through dictionary maps and session-state logic.

**Features:**
- **Text normalization:** trims whitespace, converts to lowercase, and strips punctuation and apostrophes so inputs like `What's your name?` and `whats your name` match the same rule.
- **Multi-intent detection:** a keyword dictionary maps phrases to intents (greeting, how are you, bot identity, set name, get name, thanks, help). Single words match whole words only, so `this` never triggers `hi`.
- **Functional dictionary maps:** each intent is linked to its own handler function, which keeps the code modular and easy to extend.
- **Nested state logic:** an `if-elif-else` router checks the current session mode (`main`, `help_menu`, `tree_N`, `awaiting_name`) before intent detection, so the same input can mean different things in different states.
- **Multiple help trees:** a help menu leads to three trees (Account, Orders, Technical Support), each with its own topics and a `back` command to move up one level.
- **Session state management:** a session dictionary tracks the user's name, current mode, turn count, and consecutive unrecognized inputs.
- **Graceful fallbacks:** unknown input gets a rephrase prompt, repeated misses point the user to the help menu, empty input gets a reminder, invalid menu choices get guidance, and `Ctrl+C` or end-of-input exits cleanly.

**Key Concepts:** Text Normalization, Dictionary Dispatch, Nested Conditional Logic, Session State Management, Input Validation, Error Handling, Modular Functions.

**Sample Session:**

```text
========================================
       Welcome to Python Chatbot
========================================
Bot: Hi! Type 'help' for options or 'exit' to quit.

You: Hello!
Bot: Hello! How can I help you?

You: my name is
Bot: What should I call you?

You: ali khan
Bot: Nice to meet you, Ali Khan!

You: help
Bot: What do you need help with?
  1. Account
  2. Orders
  3. Technical support
  (type a number, or 'back')

You: 1
Bot: Account help:
  1. Topic 1
  2. Topic 2
  (type a number, or 'back')

You: 2
Bot: To update your email, go to Settings > Profile.

You: back
Bot: Back to help topics. Choose 1, 2 or 3.

You: back
Bot: Back to the main menu. What else can I do?

You: exit
Bot: Goodbye, Ali Khan!
```

## Technologies & Tools

- **Language:** Python 3
- **Libraries & Modules:** `string`, `re`, `csv`, `os`, `pathlib`, `shutil`, `timeit`
- **Development Environment:** Visual Studio Code
- **Version Control:** Git & GitHub

## Repository Structure

```text
Python-Programming-Internship/
│
├── Task_2_Fibonacci_Module/
│   └── fibonacci.py
│
├── Task_3_File_Operations/
│   ├── main.py
│   ├── email_extraction.py
│   ├── transaction_extraction.py
│   ├── csv_generation.py
│   ├── data/
│   │   └── files/
│   └── organized/
│       ├── pdf/
│       ├── log/
│       ├── jpg/
│       └── txt/
│
├── Task_4_Rule_Based_Chatbot/
│   └── main.py
│
└── README.md
```

- `Task_2_Fibonacci_Module/fibonacci.py` is a reusable module, meant to be imported by other scripts.
- `Task_3_File_Operations/data/files/` holds the input files, and `organized/` holds the output sorted into folders by extension.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- Git installed (for cloning the repository).

### Installation

1. Clone the repository:

```bash
git clone https://github.com/syedharishussain1717/Python-Programming-Internship.git
```

2. Navigate to the repository:

```bash
cd Python-Programming-Internship
```

3. Open the folder of the task you want to execute.

4. Run the Python script:

```bash
python main.py
```

**Note:** Run `main.py` in the Task 3 and Task 4 folders. Task 2 is a reusable module (`fibonacci.py`) that you import into other scripts.

### Chatbot Quick Start (Task 04)

```bash
cd Task_4_Rule_Based_Chatbot
python main.py
```

Try these inputs: `hello`, `my name is <your name>`, `what is my name`, `help`, then a number from the menu. Type `back` to go up a level and `exit` to quit.

## Learning Outcomes

Through these practical tasks, I gained experience in:

- Strengthening Python programming fundamentals.
- Developing logical thinking and problem-solving skills.
- Writing reusable, modular, and structured code.
- Handling files and automating file operations.
- Extracting and processing data using Regular Expressions.
- Working with CSV files and Python standard libraries.
- Implementing interactive command-line applications.
- Designing dictionary-based routing and session-state logic for multi-step conversations.
- Handling invalid input and errors gracefully to build more robust programs.
- Using Git and GitHub for version control and project management.

## Author

**Syed Haris Hussain Shah**

Python Programming Intern | Computer Science Student

- **GitHub:** [syedharishussain1717](https://github.com/syedharishussain1717)
---

*This repository reflects my practical learning, continuous improvement, and hands-on development experience throughout my Python Programming Internship at Progree.*