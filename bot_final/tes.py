s = 'i see.... vegetable calories 65.2 kcal corn calories 88 kcal '

s = s.replace(' calories ', '\n')
s = s.split('\n')
s.pop(0)
s.insert(0, s.pop())
s.insert(0, s.pop())
s = '\n'.join(s)

print(s)