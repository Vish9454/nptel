class Node:
    def __init__(self,initval=None):
        self.value=initval
        self.next=None
    def isempty(self):
        return self.value==None
    def append_i(self,v):
        if self.isempty():
            self.value=v
        elif self.next==None:
            newnode=Node(v)
            self.next=newnode
        else:
            self.next.append_i(v)
        return ()
l1=Node(5);print(l1.isempty())
print(l1.append_i(3))
l1.append_i(4)
l1.append_i(5)