def greet_user(first_name, last_name): #name is parameter
    print(f"Hi {first_name} {last_name} !") 
    print("Welcome aboard")

print("Start")
#greet_user("john") # john is argument
#greet_user("mary") # mary is argument
greet_user(last_name="Smith", first_name="John") # order is not correct but still works

#keyword arguments should always come after positional arguments

print("Finish")