# coding:utf-8
# author:MichaelWong6677
'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组 并在使用O(1)额外空间的条件下完成。

 示例 1:
给定数组 nums = [1,1,2], 
函数应该返回新的长度2, 并且原数组nums的前两个元素被修改为1,2。 
你不需要考虑数组中超出新长度后面的元素。
'''


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        index = 0
        for j in range(index + 1, len(nums)):
            if nums[index] != nums[j]:
                index += 1
                nums[index] = nums[j]
        return index + 1
