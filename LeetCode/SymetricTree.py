from typing import Optional

#se verifica daca treeul este symetric
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or not root.left and not root.right:
            return True
        stack=[root.left,root.right]
        while stack:
            num_items=len(stack)
            for i in range(num_items//2):
                node1=stack.pop()
                node2=stack.pop()
                if node1 and not node2 or node2 and not node1:
                    return False
                elif not node1 and not node2:
                    continue
                elif node1.data!=node2.data:
                    return False
                else:
                    stack.append(node1.left)
                    stack.append(node2.right)
                    stack.append(node1.right)
                    stack.append(node2.left)
                    
        return True            
root=TreeNode()
root.data="root"
root.left=TreeNode()
root.left.data = "a"
root.right = TreeNode()
root.right.data = "a"
root.left.left=TreeNode()
root.left.left.data="a"
root.right.right=TreeNode()
root.right.right.data="a"

if Solution.isSymmetric(self=Solution,root=root):
    print("true")
else:
    print("false")
  
    