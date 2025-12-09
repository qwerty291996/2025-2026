# 1-topshiriq

# import os

# fayl = "testfile.txt"
# katalog = "testdir"

# if os.path.exists(fayl):
#     print(f"{fayl} fayli mavjud")
# else:
#     print(f"{fayl} fayli mavjud emas")

# if os.path.exists(katalog):
#     print(f"{katalog} katalogi mavjud")
# else:
#     print(f"{katalog} katalogi mavjud emas")

import os

joriy_katalog = os.getcwd()
print("Joriy ishchi katalog:", joriy_katalog)

yangi_katalog = "testdir"

try:
    os.chdir(yangi_katalog)
    print("Ishchi katalog ozgartirildi")
    print("Yangi ishchi katalog:", os.getcwd())
except FileNotFoundError:
    print("'testdir' katalogi topilmadi. Avval uni yarating yoki to'g'ri yo'l kiriting.")
