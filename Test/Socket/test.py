import numpy as np
import time

my_list = list(range(10000))
my_array = np.array(range(10000))

start = time.time()
for i in range(10000):
    my_list[i] *= 2
   
end = time.time()
print(my_list)
print("Ishlash vaqti:", end - start, "sekund")
