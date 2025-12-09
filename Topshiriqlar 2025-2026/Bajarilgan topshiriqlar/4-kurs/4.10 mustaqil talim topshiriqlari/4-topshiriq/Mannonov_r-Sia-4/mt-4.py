#  1-topshiriq

# import os

# if os.path.exists("oldfile.txt"):
#     os.rename("oldfile.txt", "newfile.txt")
#     print("Fayl nomi o'zgartirildi!")
# else:
#     print("oldfile.txt topilmadi!")

# 2-topshiriq

import os

if os.path.exists("oldfile.txt"):
    os.remove("oldfile.txt")
    print("Fayl o'chirildi!")
else:
    print("Fayl mavjud emas!")
