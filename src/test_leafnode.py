import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_attributes(self):
        node = LeafNode("a", "Link to Google", {'href': 'www.google.com'})
        self.assertEqual(node.to_html(), "<a href='www.google.com'>Link to Google</a>")

if __name__ == "__main__":
    unittest.main()
