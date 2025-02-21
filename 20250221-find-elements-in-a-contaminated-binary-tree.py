# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def find(self, target: int) -> bool:
        queue = []
        # Case root == NIL
        if self.root != None :
            self.root.val = 0
        else :
            return False
        # Base case
        if target == 0 :
            return True
        # Otherwise, recreate and look for the value using BFS
        queue.append(self.root)
        while len(queue) > 0 :
            pos = queue.pop(0)
            if pos.left != None :
                pos.left.val = (2*pos.val)+1
                if pos.left.val == target : 
                    return True
                elif pos.left.val < target : 
                    queue.append(pos.left)
            if pos.right != None :
                pos.right.val = (2*pos.val)+2
                if pos.right.val == target : 
                    return True
                elif pos.right.val < target : 
                    queue.append(pos.right)
        return False


        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
