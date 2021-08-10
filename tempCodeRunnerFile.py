ts = [0] * 26
left = ord('a')
for char in range(len(a)):
    alphabets[ord(a[char]) - left] += 1
    alphabets[ord(b[char]) - left] -= 1
for i in alphabets:
    if i:
        print('false')