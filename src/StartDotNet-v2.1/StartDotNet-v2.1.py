"""
Created by: John Akujobi
Date: March 28, 2024
Version: 2.1

Note: Ensure Python 3.x and .NET SDK are installed before running this script.
"""

"""
= SPEC-1: StartDotNet - C# Automated Rapid Project Setup Documentation
:sectnums:
:toc:

== Background
StartDotNet is a Python-based script designed to automate the setup process for new C# projects.
It simplifies the initialization of .NET projects by generating a text file with commands to create the project and solution files, enhancing the project setup experience.

== Requirements
* Must run in a Python environment with access to the .NET SDK.
* The user should input the project name when prompted.
* The script creates the project and solution files in the current working directory.
* Supported project types include console, webapi, classlib, xunit, and mstest.

== Method

=== UserInterface Class
The `UserInterface` class manages interactions with the user, guiding them through the project setup process.

* `greeting()`: Displays a welcoming message and a brief overview of the script's capabilities.
* `get_project_name()`: Prompts the user to enter a project name, validating the input to ensure it contains only alphanumeric characters and underscores.
* `get_project_type()`: Asks the user for the project type, ensuring it's one of the supported types (console, webapi, classlib, xunit, mstest).
* `display_menu()`: Shows a menu with options to create a new .NET project or exit the script.
* `handle_menu_selection()`: Processes the user's selection from the menu, initiating the project setup process or exiting the script based on the input.

=== DotNetProject Class
The `DotNetProject` class encapsulates the functionality for setting up the .NET project, including creating directories, initializing the solution, and building the project.

* `__init__(self, project_name, project_type='console')`: Initializes a new instance of the `DotNetProject` class with the specified project name and type.
* `execute_single_command(self, single_command)`: Executes a given shell command and prints the output or error message.
* `execute_dotnet_commands(self)`: Sequentially executes a series of .NET CLI commands to set up the project environment, including creating the solution and project files, and building and running the project.

== Implementation
The implementation involves initializing instances of the `UserInterface` and `DotNetProject` classes and invoking their methods based on user input. The script starts by displaying a greeting message, then prompts the user for project details and executes the necessary .NET CLI commands to set up the project.

== Milestones

1. User interaction and input validation.
2. Project directory and file setup.
3. .NET project build and execution.

== Gathering Results

The success of the script can be evaluated based on the ease of use, the accuracy of input validation, and the successful creation, building, and running of the .NET project.

===========================================================================================================================================================================

"""


import os
import subprocess
import re
import argparse
import sys

greeting_text = """
StartDotNet - C# Automated Rapid Project Setup
Welcome to StartDotNet!
This application helps you set up a new .NET project.
It will:
- Create a new directory for your project,
- Initialize a new solution,
- Create a new console application,
- Add the application to the solution,
- Build the application, and run it.
Please ensure that .NET is installed.
Let's get started!\n
"""

class UserInterface:
    """
    The UserInterface class is responsible for handling all interactions with the user. It displays
    messages, gathers user input, and guides the user through the project setup process.

    Methods:
        greeting: Displays a welcoming message and a brief overview of the script's capabilities.
        get_project_name: Prompts the user for the project name, ensuring it adheres to naming conventions.
        get_project_type: Asks the user for the project type and validates the input against supported types.
        display_menu: Shows a menu with options to create a new .NET project or exit.
        handle_menu_selection: Processes the user's selection from the menu.
    """
    
    def greeting(self):
        print(greeting_text)

    def get_project_name(self):
        while True:
            try:
                project_name = input("Enter the name of the project: ")
                if re.match("^[A-Za-z0-9_]+$", project_name):
                    return project_name
                else:
                    print("Invalid project name. Project name must be non-empty and can only contain alphanumeric characters and underscores.")
            except Exception as e:
                print(f"Error: {e}")
                sys.exit(1)
                
    def get_project_type(self):
        while True:
            project_type = input("Enter the type of the project (console, webapi, etc.): ")
            if project_type in ['console', 'webapi', 'classlib', 'xunit', 'mstest']:
                return project_type
            else:
                print("Invalid project type. Please enter a valid project type (console, webapi, classlib, xunit, mstest).")

    def display_menu(self):
        print("\nPlease select an option from the menu:")
        print("1. Create a new .NET project")
        print("2. Exit")

    def handle_menu_selection(self):
        self.display_menu()
        try:
            selection = int(input("Enter your selection: "))
            if selection == 1:
                project_name = self.get_project_name()
                project_type = self.get_project_type()
                project = DotNetProject(project_name, project_type)
                project.execute_dotnet_commands()
            elif selection == 2:
                print("Exiting...")
                sys.exit(0)
            else:
                print("Invalid selection. Please enter a number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number.")

class DotNetProject:
    """
    The DotNetProject class encapsulates the functionality required to set up a new .NET project.
    It manages the creation of the project directory, the initialization of the solution and project files,
    and the building and execution of the project.

    Attributes:
        project_name (str): The name of the project.
        project_type (str): The type of the project (default is 'console').
        project_directory_path (str): The filesystem path to the project directory.

    Methods:
        __init__: Initializes a new instance of the DotNetProject class.
        execute_single_command: Executes a single shell command and prints its output or error.
        execute_dotnet_commands: Executes a series of .NET CLI commands to set up the project.
    """
    
    def __init__(self, project_name, project_type='console'):
        self.project_name = project_name
        self.project_type = project_type
        self.project_directory_path = os.path.join(os.getcwd(), self.project_name)

    def execute_single_command(self, single_command):
        print(f"Executing command: {single_command}")
        completed_process = subprocess.run(single_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if completed_process.returncode != 0:
            print(f"Failed to execute command: {single_command}")
            print(f"Error: {completed_process.stderr.decode()}")
            print(f"Output: {completed_process.stdout.decode()}")
            return False
        else:
            print(f"Successfully executed command: {single_command}")
            print(f"Output: {completed_process.stdout.decode()}")
            return True

    def execute_dotnet_commands(self):
        os.makedirs(self.project_name, exist_ok=True)
        os.makedirs(self.project_directory_path, exist_ok=True)

        dotnet_commands = [
            f'dotnet new sln -n {self.project_name} -o "{self.project_directory_path}"',
            f'dotnet new {self.project_type} -o "{os.path.join(self.project_directory_path, self.project_name)}"',
            f'dotnet sln "{os.path.join(self.project_directory_path, f"{self.project_name}.sln")}" add "{os.path.join(self.project_directory_path, self.project_name, f"{self.project_name}.csproj")}"',
            f'dotnet build "{os.path.join(self.project_directory_path, self.project_name, f"{self.project_name}.csproj")}"',
            f'dotnet run --project "{os.path.join(self.project_directory_path, self.project_name, f"{self.project_name}.csproj")}"'
        ]

        failed_commands = [cmd for cmd in dotnet_commands if not self.execute_single_command(cmd)]

        if failed_commands:
            print("The following commands failed:")
            for cmd in failed_commands:
                print(cmd)
            sys.exit(1)


def main():
    ui = UserInterface()
    ui.greeting()

    parser = argparse.ArgumentParser(description="Set up a new .NET project.")
    parser.add_argument("project_name", nargs='?', default=None, help="The name of the project to create.")
    parser.add_argument("-d", "--directory", help="The directory where the project should be created.")
    parser.add_argument("-t", "--type", choices=['console', 'webapi', 'mvc'], default='console', help="The type of .NET project to create.")
    args = parser.parse_args()

    if args.project_name is None:
        args.project_name = ui.get_project_name()

    if args.directory:
        try:
            os.chdir(args.directory)
        except FileNotFoundError:
            print(f"Error: The directory {args.directory} does not exist.")
            sys.exit(1)

    project = DotNetProject(args.project_name, args.type)
    project.execute_dotnet_commands()

#=====================================================================

if __name__ == "__main__":
    main()