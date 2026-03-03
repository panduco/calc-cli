# 🧮 Advanced CLI Calculator

A powerful command-line calculator that supports both direct evaluation and an interactive REPL (Read-Eval-Print Loop) mode.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue) ![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- **Interactive Mode:** A shell-like environment for continuous calculations.
- **Scientific Functions:** Supports `sqrt`, `sin`, `cos`, `tan`, `log`, and powers (`^`).
- **History Tracking:** Automatically saves all calculations to a local file.
- **Flexible Input:** Accepts standard operators (`+`, `-`, `*`, `/`) and aliases (`x` for multiply).

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/calc-cli.git
   cd calc-cli
   ```

2. **Run the script:**
   ```bash
   python calc.py
   ```

## 💻 Usage

### Interactive Mode (Recommended)
Launch the calculator shell to perform multiple calculations without restarting.

```bash
python calc.py -i
```

**Example Session:**
```text
calc > 10 + 5
= 15
calc > 2 ^ 8
= 256
calc > sqrt 144
= 12
calc > history
--- Calculation History ---
10 + 5 = 15
2 ^ 8 = 256
sqrt 144 = 12
calc > exit
```

### Direct Mode
Quickly solve a single expression from the command line.

```bash
python calc.py 5 "*" 10
# Result: 50

python calc.py sqrt 81
# Result: 9
```

## 🧪 Supported Operations

| Type | Operators/Commands |
|------|--------------------|
| **Basic** | `+`, `-`, `*`, `/`, `%` (modulo) |
| **Advanced** | `^` (power), `x` (multiply alias) |
| **Scientific** | `sqrt`, `sin`, `cos`, `tan`, `log` |

*Note: Trigonometric functions assume degrees.*

## 📜 License

This project is licensed under the MIT License.