

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        result=""
        if self.props is None or self.props == {}:
            return result
        for prop in self.props:
            word = f' {prop}="{self.props[prop]}"'
            result += word
        return result

    def __repr__(self):
        return (f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")


class LeafNode(HTMLNode):
    '''
    Nodo hoja, el final de la ramificacion
    No contiene ningun hijo y finaliza la rama del arbol
    (Contiene igualmente un TAG, VALUE y PROPS como parametros
    para la creacion, interpretacion y configuracion del contenido)
    '''
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf node must have a value")
        if self.tag is None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return (f"HTMLNode({self.tag}, {self.value}, {self.props})")
    


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props )

    def to_html(self):
        if self.tag is None:
            raise ValueError("Node must have a tag")
        if self.children is None:
            raise ValueError("Node must have a children")
        children_html=""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}>{children_html}</{self.tag}>"
