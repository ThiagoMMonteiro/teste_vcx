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
    q.add(5)
    print (q)
    q.add("foo")
    print (q)
    q.add(10.5)
    print (q)
    q.add("baz")
    print (q)
    
    print ("___________________________________")

    q.rem()
    print (q)
    q.rem()
    print (q)
    q.rem()
    print (q)
    q.rem()
    print (q)
    q.rem()
    print (q)

    print ("___________________________________")

    q.add("baz")
    print (q)

    print ("___________________________________")

    p1 = Person("James", 50)
    q.add(p1)
    print (q)
    print (p1.age)