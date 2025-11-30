# 0x03 Shell, Variables, Expansions

This project covers **shell scripting fundamentals**, **environment variables**, **local variables**, **aliases**, **expansions**, and basic **arithmetic in Bash**. Each script is designed to be concise (exactly two lines) and executable on **Ubuntu 20.04 LTS**.

## Project Structure

| Script | Description |
|--------|-------------|
| `0-alias` | Creates an alias `ls` that executes `rm *`. |
| `1-hello_you` | Prints "hello" followed by the current Linux username. |
| `2-path` | Adds `/action` to the end of the `PATH` environment variable. |
| `3-paths` | Counts the number of directories in the current `PATH`. |
| `4-global_variables` | Lists all global environment variables. |
| `5-local_variables` | Lists all local variables, environment variables, and functions. |
| `6-create_local_variable` | Creates a new **local** variable `BEST` with value `School`. |
| `7-create_global_variable` | Creates a new **global** variable `BEST` with value `School`. |
| `8-true_knowledge` | Adds 128 to the environment variable `TRUEKNOWLEDGE` and prints the result. |
| `9-divide_and_rule` | Divides `POWER` by `DIVIDE` and prints the result. |
| `10-love_exponent_breath` | Raises `BREATH` to the power of `LOVE` and prints the result. |
| `11-binary_to_decimal` | Converts a binary number stored in `BINARY` to decimal. |
| `12-combinations` | Prints all combinations of two lowercase letters except `oo`. |
| `13-print_float` | Prints the number stored in `NUM` with **two decimal places**. |
| `100-decimal_to_hexadecimal` | Converts a decimal number in `DECIMAL` to hexadecimal. |
| `101-rot13` | Encodes or decodes text using the **ROT13** cipher. |
| `102-odd` | Prints every other line from input, starting with the first line. |
| `103-water_and_stir` | Adds the environment variables `WATER` and `STIR` and prints the result. |

## Requirements

- All scripts must:
  - Be **exactly two lines** (including `#!/bin/bash`).
  - End with a **newline**.
  - Be **executable** (`chmod +x <script>`).
- **Restrictions**:
  - Do not use `&&`, `||`, or `;`.
  - Do not use `bc`, `sed`, or `awk` (except for allowed cases like `awk` in `102-odd`).
  - Use only **bash built-ins** and standard commands.

## Usage

To run a script:

```bash
# Make the script executable
chmod +x <script_name>

# Execute the script
./<script_name>
