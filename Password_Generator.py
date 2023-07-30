import random
import string

#Ask user how long password is required?

def generate_password(min_length, numbers=True,special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

#generate_password(10,False) will generate password with length 10 and will not include numbers


    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    passwrd = ""
    meets_criteria = False #this means that a password contains a number and a special character
    has_num = False
    has_special = False

    while not meets_criteria or len(passwrd) < min_length:
        new_char = random.choice(characters)
        passwrd += new_char
        if new_char in digits:
            has_num = True
        elif new_char in special:
            has_special = True
        
        #Complicated way to update criteria variable, for learning purpose
        meets_criteria = True
        if numbers:
            meets_criteria = has_num
            if special_characters:
                meets_criteria= meets_criteria and has_special

    return passwrd

min_length = int(input("Enter the minimum length: "))
has_num = input("Do you want to have numbers in your password (y/n)?").lower()=="y"
has_special = input("Do you want to have special chars (y/n)? ").lower() == "y"
passwrd = generate_password(min_length,has_num,has_special)
print("Generated password is:", passwrd)
