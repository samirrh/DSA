class BST:
    def __init__(self, val):
        self.val = val
        self.L = None
        self.R = None
    
    def insert(self, val):
        if val <= self.val and self.L:
            self.L.insert(val)
        elif val <= self.val:
            self.L = BST(val)
        elif val > self.val and self.R:
            self.R.insert(val)
        else:
            self.R = BST(val)
    
    def search(self, val):
        if val < self.val and self.L:
            return self.L.search(val)
        if val > self.val and self.R:
            return self.R.search(val)
        
        return self.val == val
    
    def delete(self, val, parent):
        if val < self.val and self.L:
            return self.L.delete(val, self)
        elif val < self.val:
            return False
        elif val > self.val and self.R:
            return self.R.delete(val, self)
        elif val > self.val:
            return False
        else:
            if self.L is None and self.R is None and self == parent.L:
                parent.L = None
                self.clearNode()
            elif self.L is None and self.R is None and self == parent.R:
                parent.R = None
                self.clearNode()
            elif self.L and self.R is None and self == parent.L:
                parent.L = self.L
                self.clearNode()
            elif self.L and self.R is None and self == parent.R:
                parent.R = self.L
                self.clearNode()
            elif self.R and self.L is None and self == parent.L:
                parent.L = self.R
                self.clearNode()
            elif self.R and self.L is None and self == parent.R:
                parent.R = self.R
                self.clearNode()
            else:
                self.val = self.R.findMin()
                self.R.delete(self.val, self)

            return True
        
    def clearNode(self):
        self.val = None
        self.R = None
        self.L = None
    
    def findMin(self):
        if self.L:
            return self.L.findMin()
        else:
            return self.val

bst = BST(15)
bst.insert(10)
bst.insert(8)
bst.insert(12)
bst.insert(20)
bst.insert(17)
bst.insert(25)
bst.insert(19)
print(bst.search(15))
print(bst.delete(8, None))
print(bst.delete(8, None))
            
