import time

class Node:
    """
    """
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        if self.next_node == None:
            return f"{self.data}|"
        else:
            return f"{self.data} < {self.next_node}"

class Stack:
    """
    """
    def __init__(self):
        self.last = None
    
    def add(self, data):
        node = Node(data)

        node.next_node = self.last
        self.last = node

    def rem(self):
        if self.last == None:
            print("The stack is already empty!")
        else:
            self.last = self.last.next_node

    def __str__(self):
        return f" <- {self.last}"

if __name__ == "__main__":
    
    s = Stack()

    print (s)
    time.sleep(2)
    s.add(5)
    print (s)
    time.sleep(2)
    s.add("foo")
    print (s)
    time.sleep(2)
    s.add("10.5")
    print (s)
    time.sleep(2)
    s.add("7")
    print (s)    

    print ("___________________________________")
    time.sleep(2)
    print ("Removing...")
    time.sleep(2)

    s.rem()
    print(s)
    time.sleep(2)
    s.rem()
    print(s)
    time.sleep(2)
    s.rem()
    print(s)
    time.sleep(2)
    s.rem()
    print(s)
    time.sleep(2)
    print ("Trying to remove empty stack...")
    time.sleep(2)
    s.rem()