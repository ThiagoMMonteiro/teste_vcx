import time

class Node:
    """
    """
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return f"{self.data} < {self.next_node}"

class Queue:
    """
    """
    def __init__(self):
        self.first = None
        self.last = None
    
    def add(self, data):
        node = Node(data)

        if self.first == None:
            self.first = node
            self.last = node
        else:
            self.last.next_node = node
            self.last = node

    def rem(self):
        if self.first == None:
            print("The queue is already empty!")
        elif not self.first.next_node:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next_node
            

    def __str__(self):
        return f" <- {self.first}"

class Person:
    """
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}"

if __name__ == "__main__":
    q = Queue()

    print (q)
    time.sleep(2)
    print ("Inserting...")
    time.sleep(2)
    q.add(5)
    print (q)
    time.sleep(2)
    q.add("foo")
    print (q)
    time.sleep(2)
    q.add(10.5)
    print (q)
    time.sleep(2)
    q.add("baz")
    print (q)
    
    print ("___________________________________")
    time.sleep(2)
    print ("Removing...")
    time.sleep(2)

    q.rem()
    print (q)
    time.sleep(2)
    q.rem()
    print (q)
    time.sleep(2)
    q.rem()
    print (q)
    time.sleep(2)
    q.rem()
    print (q)
    time.sleep(2)
    print ("Trying to remove empty queue...")
    time.sleep(2)
    q.rem()

    print ("___________________________________")
    time.sleep(5)

    print ("Inserting an object...")
    p1 = Person("James", 50)
    q.add(p1)
    print (q)
    time.sleep(2)
    print (p1.age)