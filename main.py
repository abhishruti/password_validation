name, phone, username, password = input().split(" ")

def display(name, phone, username, password):
    print(name)
    print(phone)
    print(username)
    print(password)
  
def contains(chars, word):
    for c in chars:
        if c in word:
            return True
    return False 
    
count = 0

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"


if len(password)>=6 and len(password)<=20:
    try:
        if not contains(numbers, password):
            count+=1
        if not contains(lower_case, password):
            count+=1
        if not contains(upper_case, password):
            count+=1
        if not contains(special_characters, password):
            count+=1
    except password:
        count=0
    if count==0:
        display(name, phone, username, password)
    else:
        raise Exception("Invalid password")
else:
    raise Exception("Invalid password")