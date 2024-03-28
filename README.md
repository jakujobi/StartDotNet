# StartDotNet - C# Automated Rapid Project Setup

## Introduction

StartDotNet is a tool designed to simplify the setup process for new C# projects using the .NET framework. It automates the creation of project directories, solution files, and project files, streamlining the initialization process for developers. StartDotNet can be used either through a Python script or as a standalone executable file.

## Features

- **Interactive Setup**: Guides users through the setup process with prompts for project names and types.
- **Project Type Support**: Supports various project types including console applications, web APIs, class libraries, and test projects (xUnit, MSTest).
- **Automation**: Automatically generates and executes .NET CLI commands to set up the project.
- **Multiple Usage Options**: Available as a Python script or a Windows executable file.

## Prerequisites

For Python Script:

- Python 3.x
- .NET SDK

For Executable File:

- .NET SDK

You can check if the .NET SDK is installed by running `dotnet --version` in your terminal or command prompt.

## Installation

### Python Script

1. Download the `StartDotNet.py` script to your local machine.

### Executable File

1. Download the `StartDotNet.exe` executable file to your local machine.

## Usage

### Using the Executable File

1. **Open a Command Prompt**: Navigate to the folder where you've downloaded `StartDotNet.exe`.
2. **Run the Executable**: Simply double-click on `StartDotNet.exe` or run it from the command prompt:

   ```cmd
   StartDotNet.exe
   ```
3. **Follow the Prompts**: The executable will guide you through the same process as the script.


### Using the Python Script

1. **Open a Terminal or Command Prompt**: Navigate to the folder where you've saved `StartDotNet.py`.
2. **Run the Script**: Execute the script by running the following command:

   ```bash
   python StartDotNet.py
   ```
3. **Follow the Prompts**: The script will guide you through the process. You'll be asked to enter a project name and select a project type.

### Command Line Arguments

For both the Python script and the executable, you can use command line arguments to specify the project name, directory, and type:

- `-d`, `--directory`: Specify the directory where the project should be created.
- `-t`, `--type`: Specify the type of .NET project (`console`, `webapi`, `mvc`).

Example for the Python script:

```bash
python StartDotNet.py MyNewProject -d ./Projects -t console
```

Example for the executable:

```cmd
StartDotNet.exe MyNewProject -d .\Projects -t console
```

## Contributing

We welcome contributions to StartDotNet! If you have suggestions for improvements or encounter any issues, please feel free to submit an issue or pull request on our GitHub repository.

## License

StartDotNet is open-sourced under the GNU General Public  License. See the LICENSE file for more details.

## Acknowledgments

Created by John Akujobi in March 2024.

Special thanks to the .NET community and my classmates in CSC 346 OOP SP24 for being the first users and providing feedback.
