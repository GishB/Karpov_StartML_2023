# nums = [2,11,7,15], target = 9 - > [0,2]

nums = [2,11,7,15]
target = 9

queue = []
dictionary = {2:0, 11:1, 7:2, 15:3}

for i in dictionary.keys():
    queue.append(dictionary[i])
    target_temp = target - i
    if target < 0:
        queue.pop()
        continue
    elif target > 0:
        next_target = dictionary.get(target_temp)
        if next_target == None:
            queue.pop()
            continue
        else:
            queue.append(next_target)
            break
    else:
        break
print(queue)
#


























