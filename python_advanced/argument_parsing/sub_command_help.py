import argparse

# import argparse

# Create the top-level ArgumentParser object
parser = argparse.ArgumentParser(description='Example script with subcommand for the second argument')

# Add the first argument
parser.add_argument('--arg1', help='First argument')

# Create a subparsers object for the second argument
parser.add_argument('--env-var', dest='subcommand', help='Subcommand for environment variable')
subparsers = parser.add_subparsers(title='Subcommands', help='Subcommand help')

# Subcommand 1: option1
parser_option1 = subparsers.add_parser('option1', help='Subcommand 1 help')
parser_option1.add_argument('--json-file', help='Path to a JSON file')

# Subcommand 2: option2
parser_option2 = subparsers.add_parser('option2', help='Subcommand 2 help')
parser_option2.add_argument('--env-vars', action='store_true',help='Set this flag to true if env vars are need to be used')

# Add the third argument
parser.add_argument('--arg3', help='Third argument')

# Parse the command-line arguments
args = parser.parse_args()

# Handle the first argument
arg1_value = args.arg1
print(f'First argument value: {arg1_value}')

# Handle the third argument
arg3_value = args.arg3
print(f'Third argument value: {arg3_value}')

# Handle the second argument (with subcommands)
if hasattr(args, 'subcommand'):
    subcommand = args.subcommand

    if subcommand == 'option1':
        # Code to handle option1 and its arguments
        print(f'Subcommand "option1" selected for environment variable.')
    
    elif subcommand == 'option2':
        # Code to handle option2 and its arguments
        print(f'Subcommand "option2" selected for environment variable.')
else:
    # No subcommand specified for the second argument
    print(f'No subcommand specified for environment variable.')


#==========

# # Create the top-level ArgumentParser object
# parser = argparse.ArgumentParser(description='Example script with subcommands')

# parser.add_argument('--arg1', help="Argument 1")
# # parser.add_argument('--arg2', help="Argument 2")
# # parser.add_argument('--arg3', help="Argument 3")
# # parser.add_argument('--arg4', help="Argument 4")

# # Create a subparsers object to handle subcommands
# subparsers = parser.add_subparsers(title='Subcommands', dest='subcommand', help='Subcommand help')

# # Subcommand 1: option1
# parser_option1 = subparsers.add_parser('option1', help='Subcommand 1 help')
# parser_option1.add_argument('--json-file', required=True, help='Path to a JSON file')

# # Subcommand 2: option2
# parser_option2 = subparsers.add_parser('option2', help='Subcommand 2 help')
# parser_option2.add_argument('--env-var', required=False, help='Name of an environment variable')

# # Parse the command-line arguments
# args = parser.parse_args()

# print('parent args'+args.arg1)

# # Handle subcommands and their respective arguments
# if args.subcommand == 'option1':
#     # Code to handle option1 and its arguments
#     json_file_path = args.json_file
#     print(f'Subcommand "option1" selected with JSON file: {json_file_path}')
    
# elif args.subcommand == 'option2':
#     # Code to handle option2 and its arguments
#     env_var_name = args.env_var
#     print(f'Subcommand "option2" selected with environment variable: {env_var_name}')
