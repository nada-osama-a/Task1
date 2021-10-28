x = int(input())
count = 0

while x >= 0 :
    x = int(x/10)
    count = count + 1
    if x == 0 : break

print(count)
