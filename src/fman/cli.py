import argparse


def main():
    #main function for the CLI, this is where we will define the argument parser and handle the commands

    # parser is the main argument parser for the CLI ,prog is the name of the program, and description is a brief description of the CLI
    parser=argparse.ArgumentParser(
        prog="devtool", 
        description="A developer productivity CLI"
    )
    # add_argument is used to add arguments to the parser, -v and --version are the flags for the version argument, action="version" tells argparse to print the version and exit, and version is the version string to print
    parser.add_argument(
        "-v",
        "--version",
        action="version", 
        version="devtool 0.1.0"
    )

    parser.add_argument(
        "--info",
        action="store_true",
        help="Display configuration information"
    )

    info_subparser=parser.add_subparsers(
        
    )

    #add_subparsers is used to add subcommands to the parser, dest is the name of the attribute to store the subcommand name in
    subparsers=parser.add_subparsers(
        dest="command"
    )

    #TODO: Add subcommands here

    todo_parser=subparsers.add_parser(
        "todo",
        help="Manage your TODOs"
    )
    todo_subparser=todo_parser.add_subparsers(
        dest="todo_command"
    )
    add_todo_parser=todo_subparser.add_parser(
        "add",
        help="Add a new TODO"
    )

    add_todo_parser.add_argument(
        "task",
        help="The TODO task to add"
    )
    args=parser.parse_args()

    if args.command == "todo":
        if args.todo_command == "add":
            print(f"Adding task: {args.task}")
        else:
            print("Unknown task command")

    if args.info:       
        print("Configuration information:") 
    print(f"Commands: {args.command}")
#__name__ is a special variable in Python that is set to "__main__" when the script is run directly,
#  and to the name of the module when it is imported. This allows us to check if the script is being run directly or imported as a module,
#  and only call main() if it is being run directly.
if __name__ == "__main__":
    main()



    
"""


from pathlib import Path

cwd = Path.cwd()
print(f"Current working directory: {cwd}")

home_dir = Path.home()
print(f"Home directory: {home_dir}")

path_name=Path.name

print(f"Path name: {path_name}")

filename=Path.stem
print(f"Filename: {filename}")

"""