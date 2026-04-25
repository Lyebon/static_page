from enum import Enum

class TextType(Enum):
    #Tipos de texto validos
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    # Nodo de texto con los valores de Texto, Tipo de texto y URL opcional
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    # Verificador de igualdad para testear la funcionalidad
    def __eq__(self, other):
        return (self.text == other.text
                and self.text_type == other.text_type
                and self.url == other.url)
    
    # Revision del contenido del nodo para poder debuggear si algo sale mal
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"