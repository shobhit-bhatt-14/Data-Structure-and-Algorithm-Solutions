str = input().strip()

k = ['Realize', 'that', 'excellent', 'marks', 'qualify', 'everybody', 'for', 'jumps', 'in', 'wages']
c = w = s = message = ''

for x in str:
    if x == '-':
        w = int(s)
        w -= 1
        s = ''
    elif x == ',':
        c = int(s)
        c -= 1
        message += k[w][c]
        s = ''
    elif x == '@':
        c = int(s)
        c -= 1
        message += k[w][c]
        message += ' '
        s = ''
    else:
        s += x

c = int(s)
c -= 1
message += k[w][c]

print(message)