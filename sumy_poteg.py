a, b = input().split(" ")
a = int(a)
b = int(b)

liczby = [float(x) for x in input().split(" ")]

sum = 0

for i in liczby:
    sum += i**b

print("%.3f" %sum)