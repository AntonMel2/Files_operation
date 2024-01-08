name_count = {}
with open('1.txt') as f:
    line_count1 = 0
    for line in f:
        line_count1 += 1
    name_count['1.txt'] = line_count1

with open('2.txt') as f:
    line_count2 = 0
    for line in f:
        line_count2 += 1
    name_count['2.txt'] = line_count2

with open('3.txt') as f:
    line_count3 = 0
    for line in f:
        line_count3 += 1
    name_count['3.txt'] = line_count3

sort_count = sorted(name_count.items(), key = lambda item: item[1])
with open('new.txt', 'a') as f:
    for i in range(len(sort_count)):
        f.write(sort_count[i][0])
        f.write('\n' + str(sort_count[i][1]))
        f.write('\n' + open(sort_count[i][0]).read().strip() + '\n')
