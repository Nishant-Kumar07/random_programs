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


t1= Tree(5)

t1.left = Tree(10)
t1.right = Tree(15)
t1.left.left = Tree(20)
t1.left.right = Tree(25)

t1.print_tree()
