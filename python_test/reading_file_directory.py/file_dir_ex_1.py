from pathlib import Path

# to check if a directory exists
# path = Path("packages")
# print(path.exists())

# to create a directory in the root folder and returns None which basically means it doesn't return any value
# path = Path("emails")
# print(path.mkdir())

# ro remove the given directory from root folder
# path = Path("emails")
# print(path.rmdir())

# to print all files from current folder
# path = Path()
# for file in path.glob('*.py'): 
#     print(file)

path = Path("/root/workspace/pre_prod_tenant1_infra")
# to print all files and directories
for file in path.glob('*'): 
    print(file)