# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #BST
        # two nodes which we can p and q
        #find LCA od the two nodes

        if not root: return None

        pVal = p.val
        qVal = q.val 

        if (pVal < root.val) and (qVal < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (pVal > root.val) and (qVal > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root



        
        
        