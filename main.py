# with open(file='file.txt') as file:
#     contents = file.read()
#     print(contents)


with open(file='file.txt', mode='w') as file:
    file.write('New text')
