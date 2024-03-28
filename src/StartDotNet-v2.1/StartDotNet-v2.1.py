"""
StartDotNet - C# Automated Rapid Project Setup

This Python script automates the setup of new C# projects. It generates a text file with 
commands to create a .NET project and solution file, streamlining the project initialization process.

Usage:
Run this script in a Python environment. Follow the prompts to input the name of the new project.
The script will generate a text file with commands to set up the project.

Features:
- Creates a new .NET project and solution file.
- Interactive prompts for project name input.
- Generates a text file with necessary commands for project setup.

Created by: John Akujobi
Date: January 2024
Version: 5.0

Note: Ensure Python 3.x and .NET SDK are installed before running this script.
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
    def __init__(self, project_name, project_type='console'):
        self.project_name = project_name
        self.project_type = project_type
        self.project_directory_path = os.path.join(os.getcwd(), self.project_name)

    def execute_single_command(self, single_command):
        print(f"Executing command: {single_command}")
        process = subprocess.Popen(single_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            print(f"Failed to execute command: {single_command}")
            print(f"Error: {stderr.decode()}")
            print(f"Output: {stdout.decode()}")
            return False
        else:
            print(f"Successfully executed command: {single_command}")
            print(f"Output: {stdout.decode()}")
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
        os.chdir(args.directory)

    project = DotNetProject(args.project_name, args.type)
    project.execute_dotnet_commands()

if __name__ == "__main__":
    main()