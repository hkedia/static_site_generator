import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_bold(self):
        node = TextNode("bolded", TextType.BOLD)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "b")
        self.assertEqual(html.value, "bolded")
        self.assertEqual(html.props, None)

    def test_italic(self):
        node = TextNode("slanted", TextType.ITALIC)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "i")
        self.assertEqual(html.value, "slanted")

    def test_code(self):
        node = TextNode("x = 1", TextType.CODE)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "code")
        self.assertEqual(html.value, "x = 1")

    def test_link(self):
        node = TextNode("Boot.dev", TextType.LINK, "https://boot.dev")
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "a")
        self.assertEqual(html.value, "Boot.dev")
        self.assertEqual(html.props, {"href": "https://boot.dev"})

    def test_image(self):
        node = TextNode("an image", TextType.IMAGE, "https://example.com/a.png")
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "img")
        self.assertEqual(html.value, "")  # per assignment
        self.assertEqual(html.props, {"src": "https://example.com/a.png", "alt": "an image"})

    def test_invalid_type_raises(self):
        node = TextNode("oops", "not-a-real-type")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()