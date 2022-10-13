from platform import node
import ListNode

class Solution(object):
    def deleteNode(self,node)  : 
    nou=node.next
    node.val=nou.val
    node.next=nou.next
    nou.next=None
    
    del(node)
        

    