# coding:utf-8
# author:MichaelWong6677
'''
求三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 判断list是否为空，或者长度是否小于3
        list_length = len(nums)
        if nums == [] or list_length < 3:
            return []
        # 将list进行排序，如果排序完第一个数字大于零，则返回空
        nums.sort()
        if nums[0] > 0:
            return []
        res = []
        for i in range(list_length):
            if(i > 0 and nums[i] == nums[i - 1]):
                continue
            L = i + 1
            R = list_length - 1
            while(L < R):
                if(nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while(L < R and nums[L] == nums[L + 1]):
                        L += 1
                    while(L < R and nums[R] == nums[R - 1]):
                        R -= 1
                    L += 1
                    R -= 1
                elif(nums[i] + nums[L] + nums[R] > 0):
                    R -= 1
                else:
                    L += 1
        return res
