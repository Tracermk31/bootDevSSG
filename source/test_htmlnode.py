import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_not_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("Blah", "Blie", "Bloo", {"target":"blank"})
        self.assertTrue(node.props_to_html() == ' target="blank"')

    def test_all_not_none(self):
        node = HTMLNode("Blah", "Blie", "Bloo", {"target":"_blank"})
        self.assertTrue(node.tag != None and node.value != None and node.children != None and node.props != None)
   
if __name__ == "__main__":
    unittest.main() 