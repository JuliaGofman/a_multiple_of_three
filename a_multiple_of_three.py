a, b = int(input()), int(input())
sum, c = 0, 0
for i in range(a, b+1):
    if i%3 == 0:
        c += 1
        sum += i
print(sum/c)