import re
from textnode import TextNode, TextType
'''
Split nodes delimiter:
Recibe una lista de nodos, un delimitador para separar texto y el tipo de texto a separar
Si el texto ya tiene un formato lo agrega a la lista
si no divide el texto, revisa y agrega nuevos nodos con las propiedades correctas
'''
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
                    if part == "":
                        continue
                    else:
                        nodes.append(TextNode(part, TextType.TEXT))
                else:
                    nodes.append(TextNode(part, text_type))
    return nodes

'''
Extraen la informacion de Links o Imagenes para generar el nodo de un texto plano.
devuelven una lista vacia si no encuentra nada o una lista de tuplas
'''
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
     

'''
Recibe una lista de nodos y se fija por nodos con propiedades
si el texto tiene una imagen o link y agregarlos como TextNode nuevos
'''

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        image_extract = extract_markdown_images(node.text)
        if not image_extract:
            new_nodes.append(node)
        else:
            node_text = node.text
            for part in image_extract:
                image_alt, image_link = part
                split_text = node_text.split(f"![{image_alt}]({image_link})", 1)
                if split_text[0] != "":
                    new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                node_text = split_text[1]
            if node_text != "":
                new_nodes.append(TextNode(node_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        link_extract = extract_markdown_links(node.text)
        if not link_extract:
            new_nodes.append(node)
        else:
            node_text = node.text
            for part in link_extract:
                link_alt, url_link = part
                split_text = node_text.split(f"[{link_alt}]({url_link})", 1)
                if split_text[0] != "":
                    new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                new_nodes.append(TextNode(link_alt, TextType.LINK, url_link))
                node_text = split_text[1]
            if node_text != "":
                new_nodes.append(TextNode(node_text, TextType.TEXT))
    return new_nodes

'''
Genera de un texto plano la separacion respectiva de las partes
armando TextNode validos con la oracion
'''
def text_to_textnodes(text):
    text_node = [TextNode(text, TextType.TEXT)]
    node_split = split_nodes_delimiter(text_node, "**", TextType.BOLD)
    node_split = split_nodes_delimiter(node_split, "_", TextType.ITALIC)
    node_split = split_nodes_delimiter(node_split, "`", TextType.CODE)
    node_split = split_nodes_image(node_split)
    node_split = split_nodes_link(node_split)
    return node_split


def markdown_to_blocks(markdown):
    result = []
    split_markdown = markdown.split("\n\n")
    for text in split_markdown:
        if text != "":
            result.append(text)

    return result