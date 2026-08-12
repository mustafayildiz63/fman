import argparse

parser=argparse.ArgumentParser(
    prog="I am a CLI",
    description="A simple CLI to demonstrate argparse"
)

subparser=parser.add_subparsers(dest="info")

name_parser=subparser.add_parser("name",help="enter user name")
name_parser.add_argument(   
    "--name",
    help="enter user name"
)

age_parser=subparser.add_parser("age",help="enter user age")
age_parser.add_argument(
    "--age",
    help="enter user age"
)
email_parser=subparser.add_parser("email",help="enter user email")
email_parser.add_argument(
    "--email",
    help="enter user email"
)

args=parser.parse_args()

if args.info == "name":
    print(f"Name: {args.name}")
if args.info == "age":
    print(f"Age: {args.age}")
if args.info == "email":
    print(f"Email: {args.email}")

print(args)