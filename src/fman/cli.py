import argparse
from pathlib import Path

from commands import cat, find, info, ls, mkdir, move, remove

def main():

    """Created a parser"""
    parser=argparse.ArgumentParser(
        prog="Files Managing CLI"
    )

    """Created severeal command with add_argument function"""
    parser.add_argument(
        "-mv",
        "--move",
        help="Move the source path to destination path.",

       action="store_true"
    )

    parser.add_argument(
        "--source",
    
        help="The path of the file you want to move"
        )
    parser.add_argument(
        "--destination",
        help="The path of destination Folder or file. "

    )


    parser.add_argument(
        "-ls",
        "--list",
        action="store_true",
        help="List files in the current directory",
    )

    parser.add_argument(
        "-cat",
        "--cat",
        help="Display the contents of a file",
        type=str,
        metavar="FILE",
    )

    parser.add_argument(
        "-mkdir",
        "--mkdir",
        help="Create a new directory",
        type=str,
        metavar="DIR",
    )

    parser.add_argument(
        "-rm",
        "--remove",
        help="Deleting Dir or File ",
        type=str
    )

    """args objects store whole arguments which we created"""
    args: argparse.Namespace = parser.parse_args()


    if args.remove:
        remove.removePath(args.remove)
    if args.move:
        try:
            move.move_path(args.source,args.destination)
        except Exception as e:
            print(f"Error from moving operation : {e}")

    if args.mkdir:
        
        print(f"Creating directory: {args.mkdir}")
        mkdir.make_dir(args.mkdir)


    if args.list:
        print("Listing files in the current directory:")
        current_directory = Path.cwd()

        result=ls.list_dir(current_directory)

        for item in result:
            if item['type'] == 'Dir':
                print(f"[DIR] {item['name']} - Size: {item['size']} bytes")
            elif item['type'] == 'File':
                print(f"[FILE] {item['name']} - Size: {item['size']} bytes")

    if args.cat:
        path_to_file = Path(args.cat)
        print(f"Displaying contents of file: {path_to_file}")
        
        cat.cat_file(path_to_file)












if __name__=="__main__":
    main()
    