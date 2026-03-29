# 🔐 Random Password Generator

A simple command-line Python tool that generates a strong, randomized password using a mix of lowercase letters, uppercase letters, digits, and special characters.

---

## 📖 How It Works

You choose how many characters you want in your password (minimum 8). The program then:

1. Pulls characters from four different character sets
2. Distributes them proportionally for a balanced, secure password
3. Shuffles everything randomly before displaying the final result

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your machine

### Running the Script

```bash
python password_generator.py
```

---

## 🎮 Usage Example

```
Enter the number of characters you want in your password: 5

Please enter a valid number (at least 8).
Enter the number of characters you want in your password: 12

Your password is: aG3!kR#mZ1Lq
```

---

## 🧮 Password Composition

The generated password is built from four character types, distributed as follows:

| Character Type     | Example Characters     | Share of Password |
|--------------------|------------------------|-------------------|
| Lowercase letters  | `a b c ... z`          | ~30%              |
| Uppercase letters  | `A B C ... Z`          | ~30%              |
| Digits             | `0 1 2 ... 9`          | ~20%              |
| Special characters | `! @ # $ % ^ & * ...`  | ~20%              |

All characters are drawn randomly, then shuffled again to ensure an unpredictable output every time.

---

## ✅ Input Validation

The script ensures your input is valid before generating a password:

- Must be a **numeric** value
- Must be **at least 8 characters** long (shorter passwords are considered insecure)

If an invalid input is entered, the program will prompt you again until a valid number is provided.

---

## 🔒 Security Notes

- Passwords are generated using Python's `random` module — suitable for general use
- For cryptographically secure passwords (e.g., production systems), consider using the `secrets` module instead
- Always store your passwords in a trusted password manager

---

## 📁 Project Structure

```
password_generator.py   # Main script
README.md               # Project documentation
```

---

## 📝 License

This project is open source and free to use.
