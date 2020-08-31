import random
import string
import sys
Green = "\033[32m"
Blue = "\034[40m"
End = "\033[0m"
Red = "\033[31m"
specialChars = "!@#$%^&*-_+="
all = string.ascii_letters + string.digits + specialChars



def passowrd_generator(number):
    password = []
    for i in range(number):
        for j in random.choice(all):
            password.append(j)
    return "".join(x for x in password)

def validate_password(result):
    Upper = 0
    Lower = 0
    digits = 0
    special_characters = 0
    for i in result:
        if i.isupper() == True:
            Upper += 1     
        elif i.islower() == True:
            Lower += 1
        elif i in specialChars:
            special_characters += 1
        elif i.isdigit() == True:
            digits += 1
    if Upper and Lower and special_characters and digits >=1:
        print(Green + "{}    passowrd is good ".format(result) +End)        
    else:
        print(Red+ "{}    is not a good passowrd. It does not contain all the requirments. Rerun the script again".format(result) + End)

if __name__ == "__main__":
        number = int(raw_input("enter the number : "))
        if number < 4:
            print("provide the number greater or equal to 4")
            sys.exit(0)


        result = passowrd_generator(number)
        validate_password(result)
    
