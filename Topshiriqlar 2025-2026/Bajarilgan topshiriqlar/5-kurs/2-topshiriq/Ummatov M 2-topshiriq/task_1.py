students = ["Ali", "Vali", "Oybek", "Gulbahor", "Nodir", "Faxriddin", "Oripov"]

name = input("Ismingizni kiriting: ").strip()

students_lower = [s.lower() for s in students]
if name.lower() in students_lower:
    print("Topildi")
else:
    print("Topilmadi")
