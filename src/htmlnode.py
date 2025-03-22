
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError('to_html not implemented')
    
    def props_to_html(self):
        if not self.props:
            return ""
        res = ""
        for key, value in self.props.items():
            res += f" {key}='{value}'"
        return res
   
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError()
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag is None:
            raise ValueError('Missing tag')
        if self.children is None:
            raise ValueError('Missing Children')
        res = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            res += child.to_html()
        res += f'</{self.tag}>'
        return res


