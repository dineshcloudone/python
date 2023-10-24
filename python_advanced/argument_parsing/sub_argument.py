import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="Argument Example")

# Add five arguments (one of which will have subarguments)
parser.add_argument('--arg1', help="Argument 1")
parser.add_argument('--arg2', help="Argument 2")
parser.add_argument('--arg3', help="Argument 3")
parser.add_argument('--arg4', help="Argument 4")

# Define a custom argument that will have subarguments
subparser = argparse.ArgumentParser(add_help=False)
subparser.add_argument('--subarg1', help="Subargument 1")
subparser.add_argument('--subarg2', help="Subargument 2")

# Manually parse the command-line arguments
args, remaining = parser.parse_known_args()

# Check if the custom argument with subarguments is present
if '--subarg1' in remaining:
    subargs = subparser.parse_args(remaining)
    print("Subarguments:", subargs.subarg1, subargs.subarg2)
else:
    print("No subarguments provided.")

# Handle the other arguments (args.arg1, args.arg2, etc.)
print("Other arguments:", args.arg1, args.arg2, args.arg3, args.arg4)
