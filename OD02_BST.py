# Узел дерева (одиночный элемент)
class TreeNode:
    def __init__(self, key):
        # Значение, хранимое в узле
        self.key = key

        # Ссылки на левое и правое поддеревья (изначально None)
        self.left = None
        self.right = None

# Класс, представляющий всё бинарное дерево поиска
class BinarySearchTree:
    def __init__(self):
        # Начинаем с пустого дерева: корень отсутствует
        self.root = None

    def insert(self, key):
        """
        Вставка нового значения в дерево.
        Значение размещается так, чтобы сохранялся порядок:
        всё меньшее — слева, всё большее — справа.
        """
        def _insert(node, key):
            # Если достигли пустого места, создаём новый узел
            if node is None:
                return TreeNode(key)

            # Если значение меньше текущего — идём влево
            if key < node.key:
                node.left = _insert(node.left, key)

            # Если значение больше — идём вправо
            elif key > node.key:
                node.right = _insert(node.right, key)

            # Если значение равно — ничего не делаем (дубликаты игнорируются)
            return node

        # Начинаем вставку с корня дерева
        self.root = _insert(self.root, key)

    def in_order_traversal(self):
        """
        Обход дерева «в порядке возрастания» (in-order):
        сначала левое поддерево, затем текущий узел, затем правое.
        Результат — отсортированный список значений.
        """
        def _in_order(node):
            if node:
                _in_order(node.left)       # Сначала левое поддерево
                print(node.key, end=" ")   # Затем сам узел
                _in_order(node.right)      # Затем правое поддерево

        # Запускаем рекурсивный обход от корня
        _in_order(self.root)

    def search(self, key):
        """
        Поиск значения в дереве.
        Возвращает узел с этим значением или None, если не найден.
        """
        def _search(node, key):
            # Если достигли пустого места или нашли нужный ключ — вернуть узел
            if node is None or node.key == key:
                return node

            # Ищем в левом поддереве, если значение меньше
            if key < node.key:
                return _search(node.left, key)

            # Иначе ищем в правом поддереве
            return _search(node.right, key)

        # Запускаем поиск с корня дерева
        return _search(self.root, key)

# -------------------------------
# Пример использования дерева:
# -------------------------------

bst = BinarySearchTree()  # Создаём пустое бинарное дерево поиска

# Вставляем элементы
for value in [8, 3, 10, 1, 6, 14]:
    bst.insert(value)

# Печатаем все элементы в отсортированном порядке (in-order)
bst.in_order_traversal()  # Вывод: 1 3 6 8 10 14

# Поиск существующего элемента
print("\nПоиск 6:", bst.search(6).key)  # Найдёт и выведет: 6

# Поиск отсутствующего элемента
print("Поиск 9:", bst.search(9))        # Не найдёт, вернёт: None