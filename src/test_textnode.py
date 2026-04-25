import unittest

from textnode import TextNode, TextType
from textdelimiter import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALIC)
        node4 = TextNode("This is a text node", TextType.ITALIC)
        node5 = TextNode("This is a text node", TextType.TEXT)
        node6 = TextNode("This is a text node", TextType.TEXT)
        node7 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev/")
        node8 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev/")
        node9 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev/")


        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)
        self.assertEqual(node5, node6)
        self.assertEqual(node7, node8)

        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node4)
        self.assertNotEqual(node, node6)
        self.assertNotEqual(node7, node9)

    def test_split_bold(self):
        node = TextNode("The text makes me sick **boldtext rules** but some times needs to exist", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("The text makes me sick ", TextType.TEXT),
            TextNode("boldtext rules", TextType.BOLD),
            TextNode(" but some times needs to exist", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_italic(self):
        node = TextNode("The text makes me sick _boldtext rules_ but some times needs to exist", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.BOLD)
        expected = [
            TextNode("The text makes me sick ", TextType.TEXT),
            TextNode("boldtext rules", TextType.ITALIC),
            TextNode(" but some times needs to exist", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)  

if __name__ == "__main__":
    unittest.main()