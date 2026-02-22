import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="p", value="Hello", props={"class": "greeting"})
        self.assertEqual(node.props_to_html(), ' class="greeting"')

        node = HTMLNode(tag="p", value="Hello", props={})
        self.assertEqual(node.props_to_html(), "")

        node = HTMLNode(tag="p", value="Hello", props={"class": "greeting", "id": "welcome"})
        self.assertEqual(node.props_to_html(), ' class="greeting" id="welcome"')

        node = HTMLNode(tag="p", value="Hello")
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()