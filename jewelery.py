n = int(input())
bizuteria = []

for i in range(n):
    bizuteria.append(input())

bizuteria.sort(key= lambda x: (len(x) + 1) ** 15 + ord(x[0]))

for i in range(len(bizuteria)):
    try:
        bizuter = bizuteria[i]
        nastepny_bizuter = bizuteria[i + 1]
    except IndexError:
        pass
    else:
        if len(bizuter) == len(nastepny_bizuter):
            j = 0
            while bizuter[j] == nastepny_bizuter[j]:
                j+=1

            else:
                if ord(bizuter[j]) > ord(nastepny_bizuter[j]):
                    bizuteria[i], bizuteria[i + 1] = nastepny_bizuter, bizuter


for bizuter in bizuteria:
    print(bizuter)