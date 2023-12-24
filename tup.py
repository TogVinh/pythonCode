import os
tup1 = (1,5,4,6,7, 'sdfhk', (1, 'sf'))
print(tup1)

tup2 = (1)
print(tup2) # sẽ hiểu tup2 là một int được cặp bởi dấu ngoặc như thể là ưu tiên trong tính toán
a = tuple([1,2,3])
print(a)

os.system("cls")
tup3 = (1,2,3)
tup4 = (3,4,5)
tup_new = tup3 + tup4
print(tup_new)