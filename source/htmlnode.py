class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented("Method not implemented")
    
    def props_to_html(self):
        html_attributes = ""
        if not self.props:
            #Return an empty string if props is empty
            return html_attributes
        else:
            for key in self.props:
                html_attributes += f' {key}="{self.props[key]}"'
        return html_attributes

    def __repr__(self):
        return (f"tag: {self.tag} value: {self.value} children: {self.children} props: {self.props}")
            
