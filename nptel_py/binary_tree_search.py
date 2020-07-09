class Tree:
    def __init__(self,initval=None):
        self.value=initval
        if self.value:
            self.left=Tree()
            self.right=Tree()
        else:
            self.left=None
            self.right=None
        return
    def isempty(self):
        return (self.value==None)

    def isleaf(self):
        return (self.left.isempty() and self.right.isempty())

    def makeempty(self):
         self.value=None
         self.right=None
         self.left=None

    def copyright(self):
        self.value=self.right.value
        self.left =self.right.left
        self.right=self.right.right
        return

    def find(self,v):
        if self.isempty():
            return False
        if self.value==v:
            return True
        if v<self.value:
            return self.left.find(v)
        if v>self.value:
            return self.right.find(v)

    def insert(self,v):
        if self.isempty():
            self.value=v
            self.left=Tree()
            self.right=Tree()

        if self.value==v:
            return

        if v<self.value:
            self.left.insert(v)
            return

        if v>self.value:
            self.right.insert(v)
            return

    def maxval(self):
        if self.right.isempty():
            return self.value
        else:
            return self.right.maxval()

    def delete(self,v):
        if self.isempty():
            return
        if v< self.value:
            self.left.delete(v)
            return
        if v> self.value:
            return self.right.delete(v)
        if v==self.value:
            if self.isleaf():
                self.makeempty()
            elif self.left.isempty():
                self.copyright()
            else:
                self.value=self.left.maxval()
                self.left.delete(self.left.maxval())
            return

    def inorder(self):
        if self.isempty():
            return ([])
        else:
            return (self.left.inorder()+[self.value]+self.right.inorder())

    def __str__(self):
        return (str(self.inorder()))

t=Tree()
for i in [1,3,3,18,7,5,4,22,14]:
    t.insert(i)
print(t)

t.delete(3)
print(t)
