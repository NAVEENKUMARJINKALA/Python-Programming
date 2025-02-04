#21. Write a Python program to find the longest common prefix of all strings. Use the Python set.

def commonprefix(strings):
    if not strings:
        return ""
    prefix=""
    latest=zip(*strings)
    print(latest)

    for chars in latest:
        print(chars)
        if (len(set(chars))) == 1:
            prefix += chars[0]
        else:
            break

    return prefix
strings=["flow","floght","flows","flower"]
print(commonprefix(strings))