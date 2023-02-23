class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            return popped_node.value
    
    def is_empty(self):
        return self.top is None


def is_palindrome(word):
    stack = Stack() 
    for letter in word:
        stack.push(letter)
    reverse_word = ''
    while not stack.is_empty():
        reverse_word += stack.pop()
    if word.lower() == reverse_word.lower():
        return True
    else:
        return False


with open('palindrome.txt', 'r') as file:
        words = file.read().split(',')
        for word in words:
            if is_palindrome(word):
                print(word, 'is a proper palindrome')
            else:
                print(word, 'is NOT a proper palindrome')
