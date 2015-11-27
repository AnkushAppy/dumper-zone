class node:
    def __init__(self, value = None, left = None , right = None):
        self.value = value
        self.left = left
        self.right = right

class queue:
    def __init__(self):
        self.array = []

    def insert(self,value):
        self.array.insert(0,value)

    def dequeue(self):
        return self.array.pop()

print "Hello"


class tree:
    def __init__(self):
        self.queue = queue()

    def add(self, root,value):

        while len(self.queue.array) > 0:
            new_node = self.queue.dequeu()
            if new_node.left:
                self.queue.insert(new_node.left)
            else :
                new_node.left.value = 0 

            if new_node.right:
                self.queue.insert(new_node.right)
            else :
                new_node.right.value = 0 








'''
'''

