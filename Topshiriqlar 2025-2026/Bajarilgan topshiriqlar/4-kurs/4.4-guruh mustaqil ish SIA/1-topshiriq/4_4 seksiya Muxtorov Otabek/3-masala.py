Muxtorov = input("Belgini kirit: ")
if Muxtorov.isdigit():
    print("digit")
elif Muxtorov.isalpha() and Muxtorov.isascii():
    print("lotin")
else:
    print("nol")
