import time
num=int(input("enter the number of seconds: "))
for x in range(num,-1,-1):
    sec=x%60
    min=int(x/60)%60
    hours=int(x/3600)
    print(f"{hours:02}:{min:02}:{sec:02}")
    time.sleep(1)
print("End")
