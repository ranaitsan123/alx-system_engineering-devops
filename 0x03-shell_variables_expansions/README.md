# 0x03 Shell, Variables, Expansions

This project focuses on **Bash scripting**, **environment variables**, **local variables**, **aliases**, **expansions**, and **basic arithmetic**. Each script is exactly two lines long, following project requirements, and is compatible with **Ubuntu 20.04 LTS**.

## Project Overview

| Script | Description |
|--------|-------------|
| `0-alias` | Creates an alias `ls` that executes `rm *` instead of listing files. |
| `1-hello_you` | Prints "hello" followed by the current Linux username (`$USER`). |
| `2-path` | Adds `/action` to the end of the `PATH` environment variable. |
| `3-paths` | Counts the number of directories in the current `PATH` variable. |
| `4-global_variables` | Lists all global environment variables. |
| `5-local_variables` | Lists all local variables, environment variables, and functions in the current shell. |
| `6-create_local_variable` | Creates a **local** variable `BEST` with value `School`. |
| `7-create_global_variable` | Creates a **global** variable `BEST` with value `School`. |
| `8-true_knowledge` | Adds `128` to the environment variable `TRUEKNOWLEDGE` and prints the result. |
| `9-divide_and_rule` | Divides the value of `POWER` by `DIVIDE` and prints the result. |
| `10-love_exponent_breath` | Raises `BREATH` to the power of `LOVE` and prints the result. |
| `11-binary_to_decimal` | Converts a binary number stored in the `BINARY` environment variable to decimal. |
| `12-combinations` | Prints all two-letter combinations of lowercase letters except `oo`, one per line. |
| `13-print_float` | Prints the number stored in `NUM` with **two decimal places**. |
| `100-decimal_to_hexadecimal` | Converts a decimal number stored in `DECIMAL` to hexadecimal. |
| `101-rot13` | Encodes or decodes text using the ROT13 cipher. |
| `102-odd` | Prints every other line from input, starting with the first line. |
| `103-water_and_stir` | Adds the values of `WATER` and `STIR` environment variables and prints the result. |

## Requirements

- All scripts:
  - Must be **exactly two lines** including `#!/bin/bash`.
  - Must end with a newline.
  - Must be executable (`chmod +x <script>`).
- Restrictions:
  - Do **not** use `&&`, `||`, or `;`.
  - Do **not** use `bc`, `sed`, or `awk` (except allowed cases like `102-odd`).

## Usage

1. Make scripts executable:

```bash
chmod +x <script_name>
````

2. Run a script:

```bash
./<script_name>
```

3. For scripts that depend on environment variables, set them first:

```bash
export TRUEKNOWLEDGE=1209
./8-true_knowledge

export POWER=42784
export DIVIDE=32
./9-divide_and_rule
```

---

**Author:** Your Name
**Date:** 2025-11-30
**ALX SE DevOps**
