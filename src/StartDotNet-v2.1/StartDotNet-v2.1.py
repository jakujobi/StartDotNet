"""
StartDotNet - C# Automated Rapid Project Setup (CARPS)

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

greeting_text = """
C# Automated Rapid Project Setup (CARPS)
Welcome to CARPS!
This application helps you set up a new .NET project.
It will:
- Create a new directory for your project,
- Initialize a new solution,
- Create a new console application,
- Add the application to the solution,
- Build the application, and run it.
Please ensure that .NET SDK are installed.
Let's get started!\n
"""

def greeting():
    print(greeting_text)

class DotNetProject:
    def __init__(self, project_name=None):
        self.project_name = project_name if project_name else self.get_project_name()
        self.validate_project_name()
        self.project_directory_path = os.path.join(os.getcwd(), self.project_name)

    def get_project_name(self):
        return input("Enter the name of the project: ")

    def validate_project_name(self):
        if not self.project_name or not re.match("^[A-Za-z0-9_]+$", self.project_name):
            raise ValueError("Invalid project name. Project name must be non-empty and can only contain alphanumeric characters and underscores.")

    def execute_single_command(self, single_command):
        print(f"Executing command: {single_command}")
        process = subprocess.Popen(single_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            print(f"Failed to execute command: {single_command}")
            print(f"Error: {stderr.decode()}")
            print(f"Output: {stdout.decode()}")
            raise SystemExit("Stopping execution due to command failure.")
        else:
            print(f"Successfully executed command: {single_command}")
            print(f"Output: {stdout.decode()}")

    def execute_dotnet_commands(self):
        os.makedirs(self.project_name, exist_ok=True)
        os.makedirs(self.project_directory_path, exist_ok=True)

        dotnet_commands = [
            f'dotnet new sln -n {self.project_name} -o "{self.project_directory_path}"',
            f'dotnet new console -o "{os.path.join(self.project_directory_path, self.project_name)}"',
            f'dotnet sln "{os.path.join(self.project_directory_path, f"{self.project_name}.sln")}" add "{os.path.join(self.project_directory_path, self.project_name, f"{self.project_name}.csproj")}"',
            f'dotnet build "{os.path.join(self.project_directory_path, self.project_name, f"{self.project_name}.csproj")}"',
            f'dotnet run --project "{os.path.join(self.project_directory_path, self.project_name, f"{self.project_name}.csproj")}"'
        ]

        for single_command in dotnet_commands:
            self.execute_single_command(single_command)


def main():
    parser = argparse.ArgumentParser(description="Set up a new .NET project.")
    parser.add_argument("project_name", nargs='?', default=None, help="The name of the project to create.")
    args = parser.parse_args()

    project = DotNetProject(args.project_name)
    if project.project_name is None:
        project.project_name = project.get_project_name()

    project.execute_dotnet_commands()# Corrected function name

if __name__ == "__main__":
    greeting()
    main()