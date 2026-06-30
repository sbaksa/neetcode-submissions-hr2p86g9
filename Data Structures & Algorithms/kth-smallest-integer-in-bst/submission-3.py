class Solution:
    def kthSmallest(self, root, k):
        count = [0]
        result = [0]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            count[0] += 1
            if count[0] == k:
                result[0] = node.val
            inorder(node.right)
        inorder(root)
        return result[0]