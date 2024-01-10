s = ''.join(input("введи").split())
s = s.lower()
print('yes' if list(s) == list(reversed(s)) else 'no')