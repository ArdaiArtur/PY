from platform import node
import ListNode


class Solution(object):
    def deleteNode(self,node)  : 
        n=ListNode
        n=node.next
        node.val=n.val
        node.next=n.next
        n.next=None
        del(node)
        

    