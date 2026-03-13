import unittest

from node import Node

class TestNode(unittest.TestCase):
    def test_node_initialization(self):
        node = Node(10)

        self.assertEqual(node.data, 10)
        self.assertIsNone(node.next)
        
    def test_node_next_assignment(self):
        node1 = Node(10)
        node2 = Node(20)

        node1.next = node2

        self.assertEqual(node1.next, node2)
        self.assertEqual(node1.next.data, 20)