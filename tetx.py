a=[1,2,3,4,5,6,7,8,9,10]
b=["a","b","c","d","e","f","g","h","i","j"]
c=["x","y","z","w","v","u","t","s","r","q"]
import time
for i,j,k in zip(a,b,c):
    print(i)
    time.sleep(1)
    print(j)
    time.sleep(1)