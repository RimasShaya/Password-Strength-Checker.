# Simple program to check password strength  

# The number of attempts allowed
attempts = 3  

while attempts > 0: 
    password = input("Enter your password: ") 

    # Conditions 
    length = len(password) >= 8 
    uppercase = False  
    lowercase = False 
    digit = False 
    special_character = False 

    # Checking each character 
    for char in password: 
        if char.isupper():  
            uppercase = True  
        if char.islower(): 
            lowercase = True  
        if char.isdigit(): 
            digit = True 
        if char in "@#$%^&*": 
            special_character = True 

    # Checking conditions 
    if length and uppercase and lowercase and digit and special_character: 
        print("Strong Password") 
        break 
    else :
        print("Weak Password") 
        print("Missing:") 

        if not length: 
            print("At least 8 characters") 
        if not uppercase: 
            print("At least one uppercase letter") 
        if not lowercase: 
            print("least one lowercase letter") 
        if not digit: 
          print("At least one digit") 
        if not special_character: 
            print("At least one special character") 

        attempts -= 1 
        print("Attempts left:", attempts) 
        print("---------------------") 

# When all attempts are used 
if attempts == 0: 
    print("Too many attempts! Try again later.")

