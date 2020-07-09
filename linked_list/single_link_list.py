class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    
    def delete_node(self, node):
        # https://www.pythoncentral.io/find-remove-node-linked-lists/
        prev = None
        curr = self.headval
        while curr is not None:
             if curr == node:
                 if prev:
                     prev.nextval = curr.nextval
                 else:
                     self.headval = curr.nextval
                 del curr
                 return True
             prev = curr
             curr = curr.nextval
        return False



list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()

list.delete_node(e2)

list.listprint()
