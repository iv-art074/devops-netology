abc = 'abcdefghijklmnopqrstuvwxyz'
size = 12
for i in range(size):
    string = []
    #
    for j in range(i + 1):
        string.append(abc[size - 1 - j])
    j = size - i
    while j < size:
        string.append(abc[j])
        j += 1
        # j-=1

    # while j>=0:
    #     string.append(abc[j])
    #     j-=1
    str1 = '-'.join(string)
    print(str1.center(((size - 1) * 4 + 1), '-'))
for i in range(1, size):
    string = []
    j = size - 1
    while j >= i:
        string.append(abc[j])
        j -= 1
    for j in range(i + 1, size):
        string.append(abc[j])
    # j=size-i
    # while j<size:
    #   string.append(abc[j])
    #   j+=1
    # j-=1

    # while j>=0:
    #     string.append(abc[j])
    #     j-=1
    str1 = '-'.join(string)
    print(str1.center(((size - 1) * 4 + 1), '-'))