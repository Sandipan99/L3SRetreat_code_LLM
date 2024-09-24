items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
counter_dict = dict()

for item in items:
    if counter_dict[item]:
        counter_dict[item] += 1
    else:
        counter_dict[item] = 1

print(counter_dict)
