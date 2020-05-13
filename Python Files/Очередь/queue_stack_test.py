import unittest
import queue_stack


class test_QueueFIFO(unittest.TestCase):

    def test_constructor(self):
        a = queue_stack.QueueFIFO()
        self.assertEqual(first=0, second=len(a))

    def test_add_element(self):
        a = queue_stack.QueueFIFO()
        a.add_item(8)
        self.assertEqual(a[0], 8)
        del a

    def test_del_element(self):
        a = queue_stack.QueueFIFO()
        print('test_del_element')
        a.add_item(8)
        a.add_item(7)
        a.add_item(9)
        a.del_item()
        self.assertEqual(7, a[0])
        del a

class test_StackLIFO(unittest.TestCase):

    def test_constructor(self):
        a = queue_stack.StackLIFO()
        self.assertEqual(len(a), 0)

    def test_add_element(self):
        a = queue_stack.StackLIFO()
        a.add_item(8)
        self.assertEqual(a[0], 8)
        del a

    def test_del_element(self):
        a = queue_stack.StackLIFO()
        for i in range(40):
            a.add_item(i)
        for i in range(39, -1, 1):
            self.assertEqual(i, a[len(a) - i])

if __name__ == '__main__':
    unittest.main()
