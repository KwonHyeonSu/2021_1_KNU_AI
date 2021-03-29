test = 'hello'
test = list(test)
test[0] = 'i'
test = ''.join(test)
print(test)
print(type(test))