S = input()

alphabets = []
numbers = 0
for s in S:
    if s.isalpha():
        alphabets.append(s)
    elif s.isdigit():
        numbers += int(s)
    else:
        print("Invalid input!")
alphabets.sort()

answer = ''.join(alphabets) + str(numbers)
print(answer)

# 10분