import random
small = "asdfghjklpoiuytrewqzxcvbnm"
big = "ASDFGHJKLMNBVCXZQWERTYUIO"
num = "1234567890"
lenght = 10 
all =small + big + num
password = "".join(random.sample(all,lenght))
print("the password is: ",password)







input("press enter to exit")
