with open("demo.txt", "rb") as f:
    f.seek(100)          
    t = f.read()

print(t.decode(errors="ignore"))
