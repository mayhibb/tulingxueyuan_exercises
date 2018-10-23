# 红球 3个，黄球3个，绿球6个，摸8次，写出所有可能

import random as r
total = []
reds = []
yellows = []
greens = []
for i in range(3):
    reds.append("红球")
    yellows.append("黄球")

for i in range(6):
    greens.append("绿球")

total.extend(reds)
total.extend(yellows)
total.extend(greens)

# total = ['红球', '红球', '红球', '黄球', '黄球', '黄球', '绿球', '绿球', '绿球', '绿球', '绿球', '绿球']

def ran():
    count = []
    leng = 0

    while leng < 8:
        a = r.randint(0,11)
        count.append(a)
        leng = len(set(count))
        count = list(set(count))

    result = []
    for j in count:
        result.append(total[j])
    result.sort()
    print(result)

for a in range(100):
    ran()
