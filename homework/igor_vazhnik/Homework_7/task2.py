words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

def fun(dict):
    for key, value in dict.items():
        for i in range(value):
            print(key, end ="")
        print()
fun(words)
