
# StartDotNet - C# Automated Rapid Project Setup

## Introduction

StartDotNet is a Python-based tool designed to simplify the setup process for new C# projects using the .NET framework. It automates the creation of project directories, solution files, and project files, streamlining the initialization process for developers.

## Features

- **Interactive Setup**: Guides users through the setup process with prompts for project names and types.
- **Project Type Support**: Supports various project types including console applications, web APIs, class libraries, and test projects (xUnit, MSTest).
- **Automation**: Automatically generates and executes .NET CLI commands to set up the project.

## Prerequisites

Before running StartDotNet, ensure you have the following installed:

- Python 3.x
- .NET SDK

You can check if these are installed by running `python --version` and `dotnet --version` in your terminal or command prompt.

## Installation

StartDotNet does not require a separate installation process. Simply download the `StartDotNet.py` script to your local machine.

## Usage

1. **Open a Terminal or Command Prompt**: Navigate to the folder where you've saved `StartDotNet.py`.
2. **Run the Script**: Execute the script by running the following command:

   ```bash
   python StartDotNet.py
   ```
3. **Follow the Prompts**: The script will guide you through the process. You'll be asked to enter a project name and select a project type.
4. **Check the Output**: Upon completion, the script will have created a new directory for your project, initialized a solution, created the project according to the type specified, added the project to the solution, and built and run the project.

### Command Line Arguments

Optionally, you can use command line arguments to specify the project name, directory, and type:

- `-d`, `--directory`: Specify the directory where the project should be created.
- `-t`, `--type`: Specify the type of .NET project (`console`, `webapi`, `mvc`).

Example:

```bash
python StartDotNet.py MyNewProject -d ./Projects -t console
```

## Contributing

We welcome contributions to StartDotNet! If you have suggestions for improvements or encounter any issues, please feel free to submit an issue or pull request on our GitHub repository.

## License

StartDotNet is open-sourced under the GNU 3 License. See the LICENSE file for more details.

## Acknowledgments

Created by John Akujobi in March 2024.
Special thanks to the .NET community.
