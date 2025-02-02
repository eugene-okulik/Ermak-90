words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

def result(diction):
    for key, value in diction.items():
        for i in range(value):
            print(key, end="")
        print()
result(words)
