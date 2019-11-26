
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'value:{self.value}, l:{self.left}, r:{self.right}'

    def get(self):
        return self.value

    def set(self, value):
        self.value = value

    def get_children(self):
        children = []
        if self.left:
            children.append(self.left)
        if self.right:
            children.append(self.right)
        return children


class BST:
    def __init__(self):
        self.root = None

    def set_root(self, node):
        self.root = node

    def insert(self, node, root=None):
        if root is None:
            root = Node(node)
            return root
        else:
            if node.value >= root.value:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)
            return root

    def delete(self, root, value):
        if root is None:
            return False
        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            pass

    def find(self, value, current_node=None):
        if self.root is None:
            return None
        if current_node:
            if current_node.value == value:
                return current_node
            elif current_node.value < value:
                return self.find(value, current_node.left)
            else:
                return self.find(value, current_node.right)

    # def find_depth(self, node):
    #     if node is None:
    #         return None
    #     else:
    #         left_depth = self.find_depth(node.left)
    #         right_depth = self.find_depth(node.right)
    #     if left_depth > right_depth:
    #         return left_depth + 1
    #     else:
    #         return right_depth + 1
    def find_depth(self, root):
        if root is None:
            return 0
        else:
            return max(self.find_depth(root.left), self.find_depth(root.right)) + 1


bst = BST()
r = Node(1)
n1 = Node(2)
n2 = Node(3)
n3 = Node(4)
n4 = Node(5)
n5 = Node(5)
n6 = Node(0)
bst.insert(r)
bst.insert(r, n1)
bst.insert(r, n2)
bst.insert(r, n3)
bst.insert(r, n4)
bst.insert(r, n5)
bst.insert(r, n6)
print(bst.find_depth(n5))
print(n1.get_children())