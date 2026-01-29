from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag)
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("tag cannot be missing in a ParentNode")
        elif not self.children:
            raise ValueError("Parent Nodes MUST have children")
        else:
            html_string = f"<{self.tag}>"
            for child in self.children:
                html_string += child.to_html()
            html_string += f"</{self.tag}>"
        return html_string
