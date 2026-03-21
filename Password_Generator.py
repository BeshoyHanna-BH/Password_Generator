import string
import random

characters_num =input("Enter the number of characters you want in your password: ")

while not characters_num.isdigit() or int(characters_num) < 8:
    print("\nPlease enter a valid number (at least 8).")
    characters_num = input("Enter the number of characters you want in your password: ")
    
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

random.shuffle(s1)
random.shuffle(s2)    
random.shuffle(s3)
random.shuffle(s4)


part1 = round(int(characters_num)*0.3)
part2 = round(int(characters_num)*0.2)
              
password = []
password.extend(s1[0:part1])
password.extend(s2[0:part1])
password.extend(s3[0:part2])    
password.extend(s4[0:part2])

random.shuffle(password)

print("Your password is: " + "".join(password))