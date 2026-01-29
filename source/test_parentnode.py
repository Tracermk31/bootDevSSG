import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_several_children(self):
        child_node_one = LeafNode("span", "child")
        child_node_two = LeafNode("b", "child_two")
        parent_node = ParentNode("div", [child_node_one, child_node_two])
        self.assertEqual(
            parent_node.to_html(), 
            "<div><span>child</span><b>child_two</b></div>"
        )

    def test_to_html_with_several_grandchildren(self):
        grandchild_node_one = LeafNode("p", "grandchild_one")
        grandchild_node_two = LeafNode("s", "grandchild_two")
        child_node_one = ParentNode("span", [grandchild_node_one])
        child_node_two = ParentNode("b", [grandchild_node_two])
        parent_node = ParentNode("div", [child_node_one, child_node_two])
        self.assertEqual(
            parent_node.to_html(), 
            "<div><span><p>grandchild_one</p></span><b><s>grandchild_two</s></b></div>"
        )