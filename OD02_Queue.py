from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """Добавить элемент в конец очереди"""
        self.items.append(item)

    def dequeue(self):
        """Удалить и вернуть первый элемент очереди"""
        if not self.is_empty():
            return self.items.popleft()
        return None

    def peek(self):
        """Посмотреть первый элемент без удаления"""
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        """Проверить, пуста ли очередь"""
        return len(self.items) == 0

    def size(self):
        """Вернуть размер очереди"""
        return len(self.items)

# Пример использования
q = Queue()
q.enqueue("A")
q.enqueue("B")
print(q.dequeue())   # A
print(q.peek())      # B
print(q.is_empty())  # False