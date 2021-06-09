from ctci.LinkedBinaryTree import LinkedBinaryTree

class LinkedBinarySearchTree(LinkedBinaryTree):
    
    def add(self, node, current=None):

        if self.root is None:
            self.root = node
            return

        # no duplicates
        if current is None:
            current = self.root

        done = False
        
        while done is False:

            if node < current:
                if current.left is None:
                    current.left = node
                    done = True
                else:
                    current = current.left

            if current < node:
                if current.right is None:
                    current.right = node
                    done = True
                else:
                    current = current.right