import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_not_eq(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode("p", "Hello, world!")
        self.assertNotEqual(node, node2)

    def test_props(self):
        node = LeafNode("p", "Hello, world!", {"BA":"DOOEY"})
        self.assertTrue(node.props)

if __name__ == "__main__":
    unittest.main()