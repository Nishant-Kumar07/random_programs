class Tree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


    def print_tree(self):
        print self.data
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()

    
def identicalTrees(a, b): 
      
    # 1. Both empty 
    if a is None and b is None: 
        return True 
  
    # 2. Both non-empty -> Compare them 
    if a is not None and b is not None: 
        return ((a.data == b.data) and 
                identicalTrees(a.left, b.left)and
                identicalTrees(a.right, b.right)) 
      
    # 3. one empty, one not -- false 
    return False
  

t1= Tree(5)
t1.left = Tree(10)
t1.right = Tree(15)
t1.left.left = Tree(20)
t1.left.right = Tree(25)

print("Tree 1 is ")
t1.print_tree()


t2= Tree(5)
t2.left = Tree(10)
t2.right = Tree(15)
t2.left.left = Tree(20)
t2.left.right = Tree(25)


print("\nTree 2 is ")
t2.print_tree()


response = identicalTrees(t1, t2)

if response:
    print("Tree is identical")
else:
    print("Tree is not identical")


