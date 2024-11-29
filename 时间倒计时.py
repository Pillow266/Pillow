import time
my_time=int(input(f"请输入所需要的时间："))
for x in range(my_time,0,-1):#用reversed（）同理可以做到倒数
    seconds=x % 60
    minutes=x // 60 % 60
    print(f"{minutes:02}:{seconds:02}")
    time.sleep(1)
print(f"时间到了")