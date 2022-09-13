lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst_1 = [1, 2, 6, 7]
result = []

for i in lst:
    if i not in lst_1:
        result.append(i)

lst = []
lst.extend(result)
print(lst)