temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30,
                32, 30, 28, 24, 23]

temperatures2 = list(filter(lambda x: x > 28, temperatures))
print(temperatures2)
print(max(temperatures2))
print(min(temperatures2))
aver = sum(temperatures2) / len(temperatures2)
print(round(aver, 2))
