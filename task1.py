res = [[]]
with open('recipes.txt') as f:
    for line in f:
        if len(line) > 1:
            res[-1].append(line.strip())
        else:
            res.append([])

key = ['ingredient_name', 'quantity', 'measure']
result = [[]]

for j in range(len(res)):
    for i in range(2, len(res[j])):
        result[-1].append({k:v for k, v in zip(key, res[j][i].split(' | '))})
    result.append([])

dict_key = []
dict_value = []
for i in range(len(res)):
    dict_key.append(res[i][0])
    dict_value.append(result[i])

cook_book = {k:v for k, v in zip(dict_key, dict_value)}

