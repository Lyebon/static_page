from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for node in old_nodes:
        #Si el nodo es texto comun directamente se agrega a la nueva lista
        if node.text_type != TextType.TEXT:
            nodes.append(node)
        else:
        #Se separa el texto del nodo por el delimitador
            parts = node.text.split(delimiter)
            #Si la cantidad de partes es par se devuelve una Excepcion de que no esta cerrado el texto
            if len(parts)%2 == 0:
                raise Exception(f"The delimiter {delimiter} is missing")
            for i, part in enumerate(parts):
                #Si el nodo es par en la locacion de la lista se agrega un nodo nuevo de tipo texto al resultado final
                if i%2 == 0:
                    nodes.append(TextNode(part, TextType.TEXT))
                else:
                #Si el nodo es impar en la locacion de la lista se agrega el nodo con el texto y tipo de texto que pertenece
                    nodes.append(TextNode(part, text_type))
    #Se retorna la lista final de nodos delimitados
    return nodes