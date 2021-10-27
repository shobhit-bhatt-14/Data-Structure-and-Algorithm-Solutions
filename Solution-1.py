str, ch = input().strip().split()

str = str.lower() if ch.islower() else str.upper()

flag = 0
for x in str:
    if x == ch:
        flag += 1

print(flag)
