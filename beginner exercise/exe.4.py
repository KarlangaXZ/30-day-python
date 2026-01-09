
def remove_chars(str, n):
    result = ''
    for i in range(len(str)):
        if i % n != 0:
            result += str[i]
    return result

print(remove_chars("pynative", 4))  