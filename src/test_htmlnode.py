import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_props(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com"')

    def test_props_to_html_with_none(self):
        node = HTMLNode()
        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_props_to_html_with_empty_dict(self):
        node = HTMLNode(props={})
        result = node.props_to_html()
        self.assertEqual(result, "")

if __name__ == "__main__":
    unittest.main()