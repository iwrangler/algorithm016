class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []

        while stack or root:
            if root:
                # 这部分将左子树压入栈中
                stack.append(root)
                root = root.left
            else:
                # 进入右子树前处理值
                tmp = stack.pop()
                ans.append(tmp.val)
                # 进入右子树，继续循环
                root = tmp.right
            
        return ans

