# 1-topshiriq

# def toqlarmi(n):
#     if n%2!=0:
#         return True
#     else:
#         return False
# son=int(input("Son kiriting: "))
# print(toqlarmi(son))

# 3-topshiriq

def filtr_toq_sonlar(sonlar):
    toqlar=[]
    for i in sonlar:
        if i%2!=0:
            toqlar.append(i)
    return toqlar

ruyxat=[1,5,19,17,11,16,52,18,53]
print(filtr_toq_sonlar(ruyxat))