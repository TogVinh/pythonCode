# file_object = open('testFile.txt')
# print(file_object)
# print(type(file_object))

# data = file_object.read(1000)
# print(data)

teo_file = open('testFile.txt', 'w+')
teo_file.write('Teo dep trai\n')
teo_file.seek(0)
teo_file.read()
