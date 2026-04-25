from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
        else:
            parts = node.text.split(delimiter)
            if len(parts)%2 == 0:
                raise Exception(f"The delimiter {delimiter} is missing")
            for i, part in enumerate(parts):
                if i%2 == 0:
                    #even - par
                    nodes.append(TextNode(part, TextType.TEXT))
                else:
                    #odd - impar
                    nodes.append(TextNode(part, text_type))
    return nodes