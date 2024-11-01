class Node:
    def __init__(self, key, value, left: None=None, right: None=None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def search(self, key):
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right
    
    def add(self, key, value) -> bool:
        def add_node(node: Node, key, value) -> Node:
            if key == node.key:
                return False
            elif key < node.key:
                if node.left == None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right == None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True
        
        if self.root == None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)

    def remove(self, key) -> bool:
        p = self.root           # 当前遍历节点
        parent = None           # 当前遍历节点的父节点
        is_left_child = True    # P是parent的左子节点

        while True:
            if p == None:
                return False
            
            if key == p.key:
                break
            else:
                parent = p
                if key < p.key:
                    is_left_child = True
                    p = p.left
                else:
                    is_left_child = False
                    p = p.right
        
        if p.left is None:
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right
            else:
                parent.right = p.right
        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left
        else:
            parent = p
            left = p.left
            is_left_child = True
            while left.right is not None:
                parent = left
                left = left.right
                is_left_child = False

            p.key = left.key
            p.value = left.value
            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.left
            
        return True
    

    def dump(self) -> None:
        def print_subtree(node: Node):
            if node is not None:
                print_subtree(node.left)
                print(f'{node.key} ')
                print_subtree(node.right)
        print_subtree(self.root)


tree = BinarySearchTree()
tree.add(9, None)
tree.add(5, '5')
tree.add(10, None)
tree.add(11, None)
tree.add(12, None)
tree.add(1, None)
tree.add(2, None)
tree.add(3, None)
tree.add(4, None)
tree.add(6, None)
tree.add(7, None)
tree.add(8, '8')

# tree.remove(1)
tree.remove(5)
print(tree.search(5))
print(tree.search(8))

# tree.dump()
