class Stack:
    def __init__(self, size=10):
        self.stack = [None] * size
        self.top_index = -1
        self.size = size

    def push(self, value):
        if self.top_index >= self.size - 1:
            print("Ошибка: стек переполнен")
        else:
            self.top_index += 1
            self.stack[self.top_index] = value
            print(f"Элемент {value} добавлен в стек")

    def pop(self):
        if self.is_empty():
            print("Ошибка: стек пустой, нельзя извлечь элемент")
            return None
        else:
            value = self.stack[self.top_index]
            self.stack[self.top_index] = None
            self.top_index -= 1
            print(f"Элемент {value} удалён из стека")
            return value

    def top(self):
        if self.is_empty():
            print("Ошибка: стек пустой, нет вершины")
            return None
        else:
            return self.stack[self.top_index]

    def is_empty(self):
        return self.top_index == -1



s = Stack()

s.push(5)
s.push(10)
print("Вершина стека:", s.top())
s.pop()
print("Стек пустой?", s.is_empty())
s.pop()
s.pop()
