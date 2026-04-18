import unittest

from textnode import TextNode, TextType

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

if __name__ == "__main__":
    unittest.main()