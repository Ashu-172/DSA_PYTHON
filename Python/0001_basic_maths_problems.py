import math

num = 7720800
count = 0
reverse=0

while num>0:
    digit = num%10
    num = int(num/10)
    count+=1
    reverse = reverse*10+digit

print(reverse)
# count = int(math.log(num, 10)+1)
# print(count)
