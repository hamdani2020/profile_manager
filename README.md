# User Profile Manager

This script checks and manages a user's profile information when they log into the terminal. It verifies if the user is in the correct working directory (matching their username) and manages a `.profile.txt` file, which stores basic profile information like name, phone, and email. If the profile information is missing or out of date, the script prompts the user to update it.

## Features

- **Current Directory Check**: Ensures the user is in a directory named after their username.
- **Profile Information Management**:
  - Checks for a hidden `profile.txt` file.
  - Displays profile information if available, and asks the user to confirm if it is up to date.
  - If the file is missing or information is outdated, the script prompts the user to enter or update their profile information.
- **Directory and File Creation**: 
  - If the current directory does not match the username, it creates a new directory in the user's home directory with their username.
  - Creates a new `.profile.txt` file to store profile information if it does not exist.

## Requirements

- Python 3.x
- Access to a terminal or command line interface

## Usage

1. **Download the Script**: Save the script as `main.py` and `login.py`.
2. **Set the Script to Run on Login**: You can set this script to run automatically upon login by adding it to your shell’s startup configuration:
   - **Bash**: Add the following line to `~/.bashrc` or `~/.bash_profile`:
     ```bash
     python3 /path/to/main.py
     ```
   - **Zsh**: Add the following line to `~/.zshrc`:
     ```zsh
     python3 /path/to/main.py
     ```
3. **Run Manually (Optional)**: You can also run the script manually by navigating to the script's directory and executing:
    - Make the file executable
    ```
    chmod +x main.py
    ```
    - Run the script
   ```bash
   python3 main.py

