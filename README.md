# Password Strength Checker 🔐

A simple yet effective Python program built to evaluate the strength of a user-entered password based on fundamental cybersecurity requirements. 

## 🚀 Features
The program systematically validates each password against 5 critical criteria:
* **Minimum Length:** At least 8 characters long.
* **Uppercase Check:** Contains at least one uppercase letter.
* **Lowercase Check:** Contains at least one lowercase letter.
* **Digit Check:** Contains at least one number.
* **Special Characters:** Contains at least one special symbol (e.g., `@`, `#`, `$`, `%`, `^`, `&`, `*`).

## 🔄 Logic & Control Flow
* Implements a strict **3-attempt limit**. If the user fails to provide a strong password within 3 tries, the program securely exits with a `"Too many attempts!"` warning.
* Dynamically identifies and displays exactly **which criteria are missing**, helping the user improve their password entry in real-time.

## 🛠️ Built With
* **Python 3** (Using basic control flows: Loops, Conditionals, and String Methods).
