class Stack():
    def __init__(self):
        self.values = []

    def push(self, new_item):
        self.values.insert(0, new_item)

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            self.values.pop(0)

    def peek(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            return self.values[0]
    
    def is_empty(self):
        return len(self.values) == 0
    
    def size(self):
        return len(self.values)

st = Stack()
st.values = [1, 2, 3]
st.push(189)
print(st.values)
st.pop()
print(st.values)
print(f'Peek item in stack is {st.peek()}')
print(f'The stack is empty - {st.is_empty()}')
print(f'The stack size is {st.size()}')

