# 🏢 ℙ𝕪𝕥𝕙𝕠𝕟 𝕆𝕆ℙ ℙ𝕣𝕠𝕛𝕖𝕔𝕥 — ℂ𝕠𝕞𝕡𝕒𝕟𝕪 𝕄𝕒𝕟𝕒𝕘𝕖𝕞𝕖𝕟𝕥 𝕊𝕪𝕤𝕥𝕖𝕞

> **A beginner-friendly Python console application built to demonstrate core Object-Oriented Programming (OOP) concepts.**
> The program interactively collects and manages data for different roles within a company, showcasing classes, inheritance, encapsulation, method overriding, and interactive console menus.

[🎥 **Watch the live demo here**](Insert your link here)

---

## 📌 𝕆𝕓𝕛𝕖𝕔𝕥𝕚𝕧𝕖

Create an Interactive Company Management System in Python that captures, processes, and displays employee information across various hierarchical roles. This project demonstrates a working understanding of:

* **Object-Oriented Programming:** Classes, Objects, and `__init__` initialization.
* **Inheritance:** Using `super()` and building hierarchical relationships.
* **Encapsulation:** Securing data using getters and setters.
* **Method Overriding:** Customizing inherited behaviors via `display()` and `__del__()`.
* **Control Flow:** Managing user inputs using `match-case` statements and `while` loops.
* **Built-in Functions:** Practical application of `type()`, `getattr()`, and `issubclass()`.

---

## ✅ 𝔽𝕖𝕒𝕥𝕦𝕣𝕖𝕤 & ℝ𝕖𝕢𝕦𝕚𝕣𝕖𝕞𝕖𝕟𝕥𝕤

| Core Concept | Implementation Details |
| --- | --- |
| **OOP & Inheritance** | Implements a clear class hierarchy: `Person ➔ Employee ➔ Manager ➔ Developer`. Uses `super().__init__()` for efficient initialization. |
| **Encapsulation** | Secures attributes and manages updates via setter/getter methods (e.g., `set_emp_id()`, `get_salary()`). |
| **Polymorphism** | Overrides `display()` to print role-specific details and overrides `__del__()` using `getattr()` for safe record cleanup. |
| **Interactive Menus** | Features a `match-case` main menu for navigation, plus sub-menus for immediate attribute updates on newly created objects. |
| **Advanced Built-ins** | Employs `type()` to strictly verify object types and `issubclass()` upon exit to mathematically prove hierarchical relationships. |
| **Serialization** | Converts object attributes into key-value dictionary pairs before appending them to global tracking lists. |
| **Record Iteration** | Employs a reusable `Show_Details()` function that iterates dynamically through dictionary `.items()` to print formatted data. |
| **Safe Destruction** | Utilizes `getattr()` with fallback values (like "Unknown") to safely reference attributes during object deletion without throwing exceptions. |

---

## 🌊 ℙ𝕣𝕠𝕘𝕣𝕒𝕞 𝔽𝕝𝕠𝕨

The application follows a structured, intuitive loop to ensure a seamless user experience, from initial role creation to viewing the simulated database.

1. **Welcome & Main Menu:** Displays a welcome message and a 6-option main menu to create roles, show details, or exit.
2. **Collect Information:** Depending on the choice, prompts the user for role-specific information (e.g., ID, Name, Age, Salary, Department, Languages).
3. **Record Management:** Enters a sub-loop allowing the user to update the newly created record's ID/Salary or display its details.
4. **Global View:** The "Show Details" option lets the user iterate through lists of specific roles and visually display all appended records.
5. **Exit Message & Checks:** Verifies class hierarchies via `issubclass()`, thanks the user, and terminates the application.

---

## 💻 𝔼𝕩𝕒𝕞𝕡𝕝𝕖 ℂ𝕠𝕟𝕤𝕠𝕝𝕖 𝕀𝕟𝕥𝕖𝕣𝕒𝕔𝕥𝕚𝕠𝕟

```console
Welcome to Python OOP Project: Company Management System.

Choose an operation :
 1. Create a Person
 2. Create an Employee
 3. Create a Manager
 4. Create a Developer
 5. Show Details
 6. Exit

Enter your choice:  2

Enter Employee ID : 101
Enter Employee Name : Bob
Enter Employee Age : 30
Enter Employee Salary : 55000.0

 1. Update
 2. Display
 3. Display All Details
 4. Exit

 Enter Your choice : 2

Person Name : Bob
Age: 30
Employee_ID : 101
Salary: $55000.0


## 📁 ℙ𝕣𝕠𝕛𝕖𝕔𝕥 𝕊𝕥𝕣𝕦𝕔𝕥𝕦𝕣𝕖

```text
Python-OOP-Company-Management/
├── company_management.py  # Main application source code
└── README.md              # Project documentation (this file)

```

---

## 🧠 𝔸𝕤𝕤𝕦𝕞𝕡𝕥𝕚𝕠𝕟𝕤 𝕄𝕒𝕕𝕖

* **Input Validation:** Input types are generally assumed to be valid (e.g., entering an integer when prompted for an ID). Error handling for ValueError strings in integer fields is currently beyond the scope of this project.
* **Data Persistence:** Global lists (person, employees, managers, Developers) act as a volatile, in-memory database that clears completely upon program termination.

---

## 📝 𝔸𝕔𝕒𝕕𝕖𝕞𝕚𝕔 𝕀𝕟𝕥𝕖𝕘𝕣𝕚𝕥𝕪

This project was completed independently to demonstrate proficiency in core Object-Oriented Programming principles using Python. All code is structured to satisfy typical OOP learning outcomes, specifically focusing on inheritance, encapsulation, and dictionary mapping behaviors.

By-Nihar Sheladiya 


                                 🎓 Red & White Skill Education — Shaping skills for scaling higher...!!!
