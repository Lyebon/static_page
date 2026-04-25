

class HTMLNode():
    # Nodo de HTML:
    # TAG: contiene la bandera que se va a usar (p, h1, h2, etc)
    # VALUE: El texto que contine el nodo
    # CHILDREN: Un nodo interno denominado children que puede ser un LeafNode, 
    # PROPS: Diccionario que representa los atributos del nodo para configurarlo en el lenguaje del browser
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # Methodo no implementado
    def to_html(self):
        raise NotImplementedError()
    
    # Implementacion a HTML de la configuracion pasada en el prop
    def props_to_html(self):

        #Resultado acumulable
        result=""

        # Si PROPS no contiene nada devolvemos el resultado que es el string vacio
        if self.props is None or self.props == {}:
            return result
        
        # Iteramos key por key dandole formato y agregandolo al resultado final
        for prop in self.props:
            word = f' {prop}="{self.props[prop]}"'
            result += word
        
        # Devolvemos el resultado final
        return result

    # Representacion visible para debuggear del Nodo
    def __repr__(self):
        return (f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")


class LeafNode(HTMLNode):
    # Nodo hoja, el final de la ramificacion
    # No contiene ningun hijo y finaliza la rama del arbol
    # (Contiene igualmente un TAG, VALUE y PROPS como parametros
    # para la creacion, interpretacion y configuracion del contenido)
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)
        
    # Metodo que le da formato de HTML al valor del nodo segun el TAG, VALUE y PROP(El prop tiene su propio methodo en el nodo padre)
    def to_html(self):
        
        # Si VALUE no tiene valor elevamos un error que informa la falta de datos
        if self.value is None:
            raise ValueError("All leaf node must have a value")
        
        # Si no hay un TAG que le de formato devolvemos el texto puro
        if self.tag is None:
            return f"{self.value}"
        
        # Devolvemos un string en formato HTML con los valores ordenados
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    # Representacion visible para debuggear del Nodo
    def __repr__(self):
        return (f"HTMLNode({self.tag}, {self.value}, {self.props})")
    


class ParentNode(HTMLNode):
    # Subclase Padre
    # No contiene VALUE y envuelve otros nodos dentro de si mismo
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props )

    # Metodo que le da formato de HTML al valor del nodo segun el TAG, CHILDREN y PROP
    def to_html(self):
        
        # Si el TAG esta vacio se eleva un Error de Valor avisando que no tiene TAG
        if self.tag is None:
            raise ValueError("Node must have a tag")
        
        # Si CHILDREN esta vacio se eleva un Error de Valor avisando que no tiene Nodos Children
        if self.children is None:
            raise ValueError("Node must have a children")
        
        children_html=""

        # Iteracion por todos los CHILDRENS
        for child in self.children:
            
            # Ingresar cada CHILDREN ya formateado a HTML
            children_html += child.to_html()
        
        # Devulve todo ya formateado a HTML con el tag del ParentNode
        return f"<{self.tag}>{children_html}</{self.tag}>"
