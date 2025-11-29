ch = input("Belgini kiriting: ")
if ch.isdigit():
    print("digit")
elif ch.isalpha() and ch.encode().isalpha(): 
    if ('a' <= ch.lower() <= 'z'):
        print("lotin")
    else:
        print(0)
else:
    print(0)