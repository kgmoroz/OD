class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Вставка нового значения"""
        def _insert(node, key):
            if node is None:
                return TreeNode(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            return node

        self.root = _insert(self.root, key)

    def in_order_traversal(self):
        """Обход в порядке: left -> root -> right"""
        def _in_order(node):
            if node:
                _in_order(node.left)
                print(node.key, end=" ")
                _in_order(node.right)
        _in_order(self.root)

    def search(self, key):
        """Поиск значения"""
        def _search(node, key):
            if node is None or node.key == key:
                return node
            if key < node.key:
                return _search(node.left, key)
            return _search(node.right, key)

        return _search(self.root, key)

# Пример использования
bst = BinarySearchTree()
for value in [8, 3, 10, 1, 6, 14]:
    bst.insert(value)

bst.in_order_traversal()  # 1 3 6 8 10 14
print("\nПоиск 6:", bst.search(6).key)  # 6
print("Поиск 9:", bst.search(9))        # None