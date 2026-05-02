from enum import Enum
from htmlnode import HTMLNode, ParentNode, LeafNode
from textdelimiter import text_to_textnodes
from textnode import text_node_to_html_node


'''
BlockType:
clase con tipos validos para bloques
'''
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"


'''
markdown_to_blocks:
Funcion que separa el texto en parrafos
'''
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

'''
block_to_block_type:
Funcion que revisa el tipo de parrafo que es
y le asigna un BlockType para referenciarlo
'''
def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH


'''
markdown to htmlnode:
Funcion que transforma un bloque de texto en bloques html validos
'''
def markdown_to_html_node(markdown):
    block_of_html_nodes = []
    blocks = markdown_to_blocks(markdown)
    for text in blocks:
        block_type = block_to_block_type(text)
        if block_type == BlockType.HEADING:
            node = heading_to_html_node(text)
        if block_type == BlockType.QUOTE:
            node = quote_to_html_node(text)
        if block_type == BlockType.CODE:
            node = code_to_html_node(text)
        if block_type == BlockType.ULIST:
            node = ulist_to_html_node
        if block_type == BlockType.OLIST:
            node = olist_to_html_node(text)
        if block_type == BlockType.PARAGRAPH:
            node = paragraph_to_html_node(text)
        block_of_html_nodes.append(node)
    return ParentNode("div", block_of_html_nodes)

def heading_to_html_node(text):
        count = 0
        for i in range(6):
            if text[i] == " ":
                text = text.strip("#")
                break
            count +=1
        return ParentNode(f"h{count}", text_to_children(text))

def quote_to_html_node(text):
    text = text.strip(">")
    return ParentNode("blockquote", text_to_children(text))

def code_to_html_node(text):
    text = text.strip("`")
    return ParentNode("pre", LeafNode("code", text))


def olist_to_html_node(text):
    olist = []
    item_list = text.split("\n")
    for item in item_list:
        if item.strip() == "":
            continue
        olist.append(ParentNode("li", text_to_children(item)))
    return ParentNode("ol", olist)


def ulist_to_html_node(text):
    ulist = []
    item_list = text.split("\n")
    for item in item_list:
        if item.strip() == "":
            continue
        ulist.append(ParentNode("li", text_to_children(item)))
    return ParentNode("ul", ulist)

def paragraph_to_html_node(text):
    return ParentNode("p", text_to_children(text))


def text_to_children(text):
    formated_text_node = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        formated_text_node.append(text_node_to_html_node(node))
    return formated_text_node
