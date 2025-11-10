# 1-topshiriq 

talabalar = int(input("Talabalarni kiriting sonini kiriting: "))
ruyxat = []
past=0
yuqori=0
for i in range(talabalar):
    son = int(input(f"{i+1} - talabani bahosini kiriting: "))
    ruyxat.append(son)
    if ruyxat[i] >= 60:
        yuqori+=1
    else:
        past+=1
print("Yuqori baho olgan talabalar soni: ",  yuqori,end="\n")
print("Past baho olagan talabalar soni: ", past )

# 2-topshiriq

# ruyxat = [45,50,20,15,70,90,99,87,59,63,55,78,81]
# toifa_1=[]
# toifa_2=[]
# toifa_3=[]
# toifa_4=[]
# for i in ruyxat:
#     if i > 0 and i<=54:
#         toifa_1.append(i)
#     elif i > 54 and i<=70:
#         toifa_2.append(i)
#     elif i > 70 and i<=85:
#         toifa_3.append(i)
#     elif i > 85 and i<=100:
#         toifa_4.append(i)
# print("Birinchi toifa", toifa_1)
# print("Ikkinchi toifa", toifa_2)
# print("Uchinchi toifa", toifa_3)
# print("To'rtinchi toifa", toifa_4)
