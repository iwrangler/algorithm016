# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        # 方法一：采用递归的方式
        # return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
        # 方法二：采用迭代的方式
        temp_stack = [root]
        result_list = []
        while temp_stack:
            current_node = temp_stack.pop()
            result_list.append(current_node.val)
            if current_node.right:
                temp_stack.append(current_node.right)
            if current_node.left:
                temp_stack.append(current_node.left)
        return result_list
