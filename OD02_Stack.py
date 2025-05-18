class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Добавить элемент в стек"""
        self.items.append(item)

    def pop(self):
        """Удалить и вернуть верхний элемент стека"""
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """Посмотреть верхний элемент без удаления"""
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """Проверить, пуст ли стек"""
        return len(self.items) == 0

    def size(self):
        """Вернуть размер стека"""
        return len(self.items)

# Пример использования
s = Stack()
s.push(10)
s.push(20)
print(s.pop())      # 20
print(s.peek())     # 10
print(s.is_empty()) # False