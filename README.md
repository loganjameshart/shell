# Shell Emulator

This project is a Python-based shell emulator that mimics basic shell functionalities, allowing users to interact with their file system through commands.

## Features

The shell provides the following commands:

### File and Directory Operations
- **`ls [directory]`**: Lists items in the specified directory (or the current directory if none is specified).
- **`pwd`**: Prints the current working directory.
- **`cd [directory]`**: Changes the working directory.
- **`mkdir [directory name]`**: Creates a new directory.
- **`touch [file name]`**: Creates a new blank file.
- **`rm [file/directory]`**: Deletes a file or directory. For directories, confirmation is required if they are not empty.
- **`mv [source] [destination]`**: Moves a file or directory to the specified destination.
- **`cp [source] [destination]`**: Copies a file to the specified destination.
- **`cat [file]`**: Reads and outputs the content of a file.

### Environment Management
- **`echo [string]`**: Prints the specified string to the console.
- **`export [variable]=[value]`**: Sets or updates an environment variable for the shell session.

### Miscellaneous
- **`clear`**: Clears the terminal screen.
- **`help [command]`**: Provides usage information for a command. If no command is specified, lists all available commands.
- **`quit`**: Exits the shell.

## Setup and Execution

### Prerequisites
- Python 3.x

### Running the Program
1. Clone or download this repository.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using the command:
   ```bash
   ./script_name.py
   ```
   Ensure the script has executable permissions. You can set them with:
   ```bash
   chmod +x script_name.py
   ```

## Design Details

- **Environment Variables**: Managed through the `ENV` dictionary.
- **ANSI Colors**: Provides color-coded output using ANSI escape codes defined in the `COLOR` dictionary.
- **Command Dispatch Table**: Uses a `DISPATCH` dictionary to map command strings to their corresponding functions, ensuring extensibility.

## Example Usage

```bash
~$ ls
Documents  Downloads  Pictures
~$ cd Documents
~$ pwd
/home/user/Documents
~$ touch newfile.txt
~$ ls
newfile.txt
~$ echo "Hello, World!"
Hello, World!
~$ quit
```

## Contributing

Feel free to fork this repository and submit pull requests for improvements or additional features.

## License

This project is open-source and available under the [MIT License](LICENSE).
