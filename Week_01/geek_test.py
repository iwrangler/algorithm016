# 题目：两数之和
# author:MichaelWong6677
# date:2020-09-21


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for key, value in enumerate(nums):
            if target - value in dic:  # 写之前判断，避免了重复元素的覆盖
                return [dic[target - value], key]
            dic[value] = key
