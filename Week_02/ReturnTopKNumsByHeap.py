from collections import Counter
nums = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5, 6]
nums_count_dic = dict(Counter(nums))
# print(nums_count_dic)
"""
{1: 3, 2: 2, 3: 5, 4: 2, 5: 2, 6: 1}

"""

import heapq
temp_list = []
for key, value in nums_count_dic.items():
    heapq.heappush(temp_list, (value, key))
    if len(temp_list) >= 3:
        heapq.heappop(temp_list)

print(temp_list)
# for item in temp_list:
# 	for key in item:
# 		print(item[key])
# print(type(temp_list))
result = [item[1] for item in temp_list]
print(result[::-1])
