import queue
import stack
import unittest

#========================================
#------------ queue.py ------------------
#========================================

class Test_Class_Node_queue(unittest.TestCase):
    def test__init__(self):
        n1 = queue.Node(5)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, None)
        n2 = queue.Node("Thiago")
        self.assertEqual(n2.data, "Thiago")
        self.assertEqual(n2.next_node, None)

class Test_Class_Queue(unittest.TestCase):
    def test__init__(self):
        q = queue.Queue()
        self.assertIsInstance(q, queue.Queue)
        self.assertEqual(q.first, None)
        self.assertEqual(q.last, None)

    def test_add(self):
        q = queue.Queue()
        q.add(1)
        self.assertEqual(str(q.first), '1 < None')
        self.assertEqual(str(q.last), '1 < None')
        q.add(2)
        self.assertEqual(str(q.first), '1 < 2 < None')
        self.assertEqual(str(q.last), '2 < None')
        q.add("Thiago")
        self.assertEqual(str(q.first), '1 < 2 < Thiago < None')
        self.assertEqual(str(q.last), 'Thiago < None')

    def test_rem(self):
        q = queue.Queue()
        for i in range (4):
            q.add(i)
        # '0 < 1 < 2 < 3 < None'
        q.rem()
        self.assertEqual(str(q.first), '1 < 2 < 3 < None')
        self.assertEqual(str(q.last), '3 < None')
        q.rem()
        self.assertEqual(str(q.first), '2 < 3 < None')
        self.assertEqual(str(q.last), '3 < None')
        q.rem()
        self.assertEqual(str(q.first), '3 < None')
        self.assertEqual(str(q.last), '3 < None')
        q.rem()
        self.assertEqual(str(q.first), 'None')
        self.assertEqual(str(q.last), 'None')
        q.rem()
        self.assertEqual(str(q.first), 'None')
        self.assertEqual(str(q.last), 'None')
    
    def test_is_empty(self):
        q = queue.Queue()
        self.assertEqual(q.is_empty(), True)
        q.add(1)
        self.assertEqual(q.is_empty(), False)
        q.rem()
        self.assertEqual(q.is_empty(), True)

class Test_Class_Person(unittest.TestCase):
    def test__init__(self):
        p = queue.Person("James", 50)
        self.assertIsInstance(p, queue.Person)
        self.assertEqual(p.name, "James")
        self.assertEqual(p.age, 50)

#========================================
#------------ stack.py ------------------
#========================================

class Test_Class_Node_stack(unittest.TestCase):
    def test__init__(self):
        n1 = stack.Node(5)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, None)
        n2 = stack.Node("Thiago")
        self.assertEqual(n2.data, "Thiago")
        self.assertEqual(n2.next_node, None)

class Test_Class_Stack(unittest.TestCase):
    def test__init__(self):
        s = stack.Stack()
        self.assertIsInstance(s, stack.Stack)
        self.assertEqual(s.last, None)

    def test_add(self):
        s = stack.Stack()
        s.add(1)
        self.assertEqual(str(s.last), '1|')
        s.add(2)
        self.assertEqual(str(s.last), '2 < 1|')
        s.add("Thiago")
        self.assertEqual(str(s.last), 'Thiago < 2 < 1|')

    def test_rem(self):
        s = stack.Stack()
        for i in range (4):
            s.add(i)
        # '3 < 2 < 1 < 0|'
        s.rem()
        self.assertEqual(str(s.last), '2 < 1 < 0|')
        s.rem()
        self.assertEqual(str(s.last), '1 < 0|')
        s.rem()
        self.assertEqual(str(s.last), '0|')
        s.rem()
        self.assertEqual(str(s.last), 'None')
        s.rem()
        self.assertEqual(str(s.last), 'None')

    def test_is_empty(self):
        s = stack.Stack()
        self.assertEqual(s.is_empty(), True)
        s.add(1)
        self.assertEqual(s.is_empty(), False)
        s.rem()
        self.assertEqual(s.is_empty(), True)

if __name__ == '__main__':
    unittest.main()