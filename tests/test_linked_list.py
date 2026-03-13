import unittest, io, sys

from linked_list import LinkedList
from node import Node

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()
    
    def create_list(self, values):
        for v in values:
            self.list.insert_end(v)

    # -------------------------
    # Estado inicial
    # -------------------------

    def test_initial_state(self):
        self.assertIsNone(self.list.head)
        self.assertEqual(self.list._size, 0)

    # -------------------------
    # Insert beginning
    # -------------------------

    def test_insert_beginning_empty_list(self):
        self.list.insert_beginning(10)

        self.assertIsInstance(self.list.head, Node) 
        self.assertEqual(self.list.head.data, 10)
        self.assertIsNone(self.list.head.next)   
        self.assertEqual(self.list._size, 1)

    def test_insert_beginning_with_existing_element(self):
        self.list.insert_beginning(5)
        self.list.insert_beginning(10)

        self.assertIsInstance(self.list.head, Node)
        self.assertEqual(self.list.head.data, 10)
        self.assertIsInstance(self.list.head.next, Node) 
        self.assertEqual(self.list.head.next.data, 5)
        self.assertEqual(self.list._size, 2)

    def test_insert_beginning_multiple_elements(self):
        self.list.insert_beginning(1)
        self.list.insert_beginning(2)
        self.list.insert_beginning(3)


        self.assertIsInstance(self.list.head, Node)
        self.assertEqual(self.list.head.data, 3)
        self.assertIsInstance(self.list.head.next, Node)
        self.assertEqual(self.list.head.next.data, 2)
        self.assertIsInstance(self.list.head.next.next, Node)
        self.assertEqual(self.list.head.next.next.data, 1)
        self.assertEqual(self.list._size, 3)

    # -------------------------
    # Insert end
    # -------------------------

    def test_insert_end_empty_list(self):
        self.list.insert_end(10)

        self.assertIsInstance(self.list.head, Node)
        self.assertEqual(self.list.head.data, 10)
        self.assertIsNone(self.list.head.next)
        self.assertEqual(self.list._size, 1)

    def test_insert_end_with_existing_element(self):
        self.list.insert_end(5)
        self.list.insert_end(10)

        self.assertIsInstance(self.list.head, Node)
        self.assertEqual(self.list.head.data, 5)
        self.assertIsInstance(self.list.head.next, Node)
        self.assertEqual(self.list.head.next.data, 10)
        self.assertIsNone(self.list.head.next.next)
        self.assertEqual(self.list._size, 2)

    def test_insert_end_multiple_elements(self):
        self.list.insert_end(1)
        self.list.insert_end(2)
        self.list.insert_end(3)

        self.assertIsInstance(self.list.head, Node)
        self.assertEqual(self.list.head.data, 1)
        self.assertIsInstance(self.list.head.next, Node)
        self.assertEqual(self.list.head.next.data, 2)
        self.assertIsInstance(self.list.head.next.next, Node)
        self.assertEqual(self.list.head.next.next.data, 3)
        self.assertIsNone(self.list.head.next.next.next)
        self.assertEqual(self.list._size, 3)

    # -------------------------
    # Remove
    # -------------------------

    def test_remove_from_empty_list_raises_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.list.remove(1)

        self.assertEqual(str(context.exception), "list is empty")

    def test_remove_nonexistent_value_raises_value_error(self):
        self.create_list([1])

        with self.assertRaises(ValueError) as context:
            self.list.remove(2)

        self.assertEqual(str(context.exception), "value not found in the list")

    def test_remove_only_element_using_remove(self):
        self.create_list([42])
        self.list.remove(42)
        self.assertIsNone(self.list.head)
        self.assertEqual(self.list._size, 0)

    def test_remove_head_in_two_element_list(self):
        self.create_list([1, 2])
        self.list.remove(1)

        self.assertEqual(self.list.head.data, 2)
        self.assertIsNone(self.list.head.next)
        self.assertEqual(self.list._size, 1)

    def test_remove_tail_in_two_element_list(self):
        self.create_list([1, 2])
        self.list.remove(2)

        self.assertEqual(self.list.head.data, 1)
        self.assertIsNone(self.list.head.next)
        self.assertEqual(self.list._size, 1)

    def test_remove_middle_element_in_three_element_list(self):
        self.create_list([1, 2, 3])
        self.list.remove(2)

        self.assertEqual(self.list.head.data, 1)
        self.assertEqual(self.list.head.next.data, 3)
        self.assertIsNone(self.list.head.next.next)
        self.assertEqual(self.list._size, 2)

    def test_remove_tail_in_three_element_list(self):
        self.create_list([1, 2, 3])
        self.list.remove(3)

        self.assertEqual(self.list.head.data, 1)
        self.assertEqual(self.list.head.next.data, 2)
        self.assertIsNone(self.list.head.next.next)
        self.assertEqual(self.list._size, 2)

    def test_remove_tail_in_five_element_list(self):
        self.create_list([1, 2, 3, 4, 5])
        self.list.remove(5)

        self.assertEqual(self.list.head.data, 1)
        self.assertEqual(self.list.head.next.data, 2)
        self.assertEqual(self.list.head.next.next.data, 3)
        self.assertEqual(self.list.head.next.next.next.data, 4)
        self.assertIsNone(self.list.head.next.next.next.next)
        self.assertEqual(self.list._size, 4)

    def test_remove_tail_in_five_element_list(self):
        self.create_list([1, 2, 3, 4, 5])
        self.list.remove(4)
        self.list.remove(5)

        self.assertEqual(self.list.head.data, 1)
        self.assertEqual(self.list.head.next.data, 2)
        self.assertEqual(self.list.head.next.next.data, 3)
        self.assertIsNone(self.list.head.next.next.next)
        self.assertEqual(self.list._size, 3)

    def test_remove_alternate_elements_sequentially(self):
        self.create_list([1, 2, 3, 4, 5])
        self.list.remove(1)
        self.list.remove(3)
        self.list.remove(5)

        self.assertEqual(self.list.head.data, 2)
        self.assertEqual(self.list.head.next.data, 4)
        self.assertIsNone(self.list.head.next.next)
        self.assertEqual(self.list._size, 2)

    # -------------------------
    # Search
    # -------------------------

    def test_search_in_empty_list_raises_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.list.search(10)
        self.assertEqual(str(context.exception), "list is empty")

    def test_search_value_not_found_raises_value_error(self):
        self.create_list([1, 2, 3])
        with self.assertRaises(ValueError) as context:
            self.list.search(10)
        self.assertEqual(str(context.exception), "value not found in the list")

    def test_search_value_found_returns_node(self):
        self.create_list([1, 2, 3])
        node = self.list.search(2)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 2)
        self.assertEqual(node.next.data, 3)

    def test_search_first_element_returns_head(self):
        self.create_list([1, 2, 3])
        node = self.list.search(1)
        self.assertEqual(node, self.list.head)

    def test_search_last_element_returns_tail(self):
        self.create_list([1, 2, 3])
        node = self.list.search(3)
        self.assertEqual(node.data, 3)
        self.assertIsNone(node.next)

    # -------------------------
    # Print list
    # -------------------------

    def test_print_list_empty_raises_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.list.print_list()
        self.assertEqual(str(context.exception), "list is empty")

    def test_print_list_with_elements(self):
        self.create_list([1, 2, 3])

        captured_output = io.StringIO()
        sys.stdout = captured_output

        self.list.print_list()

        sys.stdout = sys.__stdout__ 

        output = captured_output.getvalue().strip().split("\n")
        self.assertEqual(output, ["1", "2", "3"])

    def test_print_list_single_element(self):
        self.create_list([42])

        captured_output = io.StringIO()
        sys.stdout = captured_output

        self.list.print_list()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip().split("\n")
        self.assertEqual(output, ["42"])

    # -------------------------
    # Size
    # -------------------------

    def test_size_empty_list(self):
        self.assertEqual(self.list.size(), 0)

    def test_size_non_empty_list(self):
        self.create_list([1, 2, 3])
        self.assertEqual(self.list.size(), 3)

    def test_size_after_multiple_operations(self):
        self.create_list([1,2,3])
        self.list.remove(2)
        self.list.insert_end(4)
        self.assertEqual(self.list.size(), 3)

    # -------------------------
    # Is empty
    # -------------------------

    def test_is_empty_on_empty_list(self):
        self.assertTrue(self.list.is_empty())

    def test_is_empty_on_non_empty_list(self):
        self.create_list([1])
        self.assertFalse(self.list.is_empty())

if __name__ == "__main__":
    unittest.main()