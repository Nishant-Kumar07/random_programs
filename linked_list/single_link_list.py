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

    def add_node(self, pos, node):
        # Add a node:
        # pos 0, middle or last
        # 1. if position first then make that as head node and existing head node becomes current's next node
        # 2. If position in middle then make previous next node as current and current next node as next node
        
        pos_count = 0
        prev = None
        curr = self.headval
        #import pdb; pdb.set_trace()
        while curr is not None:
            if pos_count == pos:
                if prev:
                    prev.nextval = node
                    node.nextval = curr
                else:
                    self.headval = node
                    node.nextval = curr
                return True
            pos_count+=1
            prev = curr
            curr = curr.nextval

    def delete_node_at_index(self, pos):
        # pos can be 0
        ## delete the node and make the next node as head
        # pos can be in between
        ## delete the node and link prev and next node for curr node
        # Keep track of prev and curr node

        # Three basic variables to track my list
        pos_count =0
        prev = None
        curr = self.headval

        # Now start traversing the list
        while curr is not None:
            if pos_count == pos:
                # This means that it is not the first node.
                if prev:
                    prev.nextval = curr.nextval
                    del curr
                else:
                    self.headval = curr.nextval
                    del curr
                return True
            pos_count+=1
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


#list.delete_node(e2)


e4 = Node("Thurs")

print("*********\n")

list.add_node(0,e4)
list.listprint()

e5 = Node("Friday")
print("*********\n")
list.add_node(1,e5)
list.listprint()

response = list.delete_node_at_index(9)
print("*********\n")

if response == True:
    list.listprint()
else:
    print("Invalid input: Out of index")
