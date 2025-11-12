import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
  def test_to_html_props(self):
    node = HTMLNode(
      "div",
      "Hello, world!",
      None,
      {"class": "greeting", "href": "https://boot.dev"},
    )
    self.assertEqual(
      node.props_to_html(),
      ' class="greeting" href="https://boot.dev"',
    )

  def test_values(self):
    node = HTMLNode(
        "div",
        "I wish I could read",
    )
    self.assertEqual(
        node.tag,
        "div",
    )
    self.assertEqual(
        node.value,
        "I wish I could read",
    )
    self.assertEqual(
        node.children,
        None,
    )
    self.assertEqual(
        node.props,
        None,
    )

  def test_repr(self):
    node = HTMLNode(
        "p",
        "What a strange world",
        None,
        {"class": "primary"},
    )
    self.assertEqual(
        node.__repr__(),
        "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
    )

  def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

  def test_leaf_to_html_a(self):
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    self.assertEqual(node.to_html(), f"<a href=\"https://www.google.com\">Click me!</a>")

  def test_leaf_to_html_no_tag(self):
    node = LeafNode("", "Click me!")
    self.assertEqual(node.to_html(), "Click me!")

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

  def test_to_html_with_multiple_children(self):
    children = [
        LeafNode("b", "bold"),
        LeafNode(None, " text "),
        LeafNode("i", "italic")
    ]
    parent_node = ParentNode("p", children)
    self.assertEqual(
        parent_node.to_html(),
        "<p><b>bold</b> text <i>italic</i></p>"
    )

  def test_to_html_with_nested_parents(self):
    deep_node = ParentNode(
        "div",
        [
          ParentNode("span", [LeafNode("i", "nested")]),
          LeafNode(None, " plain"),
        ],
    )
    self.assertEqual(
        deep_node.to_html(),
        "<div><span><i>nested</i></span> plain</div>"
    )

  def test_to_html_with_empty_children_list(self):
    parent_node = ParentNode("p", [])
    self.assertEqual(parent_node.to_html(), "<p></p>")

  def test_to_html_with_none_tag_raises_error(self):
    node = ParentNode(None, [])
    with self.assertRaises(ValueError) as context:
        node.to_html()
    self.assertIn("valid HTML tag", str(context.exception))

  def test_to_html_with_none_children_raises_error(self):
    node = ParentNode("div", None)
    with self.assertRaises(ValueError) as context:
        node.to_html()
    self.assertIn("must have children", str(context.exception))

if __name__ == "__main__":
    unittest.main()
