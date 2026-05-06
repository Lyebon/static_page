from enum import Enum
from htmlnode import HTMLNode, ParentNode, LeafNode
from textdelimiter import text_to_textnodes, split_nodes_delimiter
from textnode import text_node_to_html_node, TextNode, TextType


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
        if block_type == BlockType.PARAGRAPH:
            block_of_html_nodes.append(paragraph_to_html(text))
        if block_type == BlockType.CODE:
            block_of_html_nodes.append(code_to_html(text))
        if block_type == BlockType.HEADING:
            block_of_html_nodes.append(heading_to_html(text))
        if block_type == BlockType.QUOTE:
            block_of_html_nodes.append(quote_to_html(text))
        if block_type == BlockType.OLIST:
            block_of_html_nodes.append(olist_to_html(text))
        if block_type == BlockType.ULIST:
            block_of_html_nodes.append(ulist_to_html(text))
    return ParentNode("div", block_of_html_nodes)

def code_to_html(text):
    backticks_strip = text[4:-3]
    code_block = [LeafNode("code" , backticks_strip)]
    return ParentNode("pre", code_block)

def heading_to_html(text):
    for i in range(0, 7):
        if text[i] == " ":
            strip_text = text[i+1:]
            text_node = text_to_textnodes(strip_text)
            childs = text_to_child(text_node)
            return ParentNode(f"h{i}", childs)

def quote_to_html(text):
    strip_text = text[1:]
    text_node = text_to_textnodes(strip_text)
    childs = text_to_child(text_node)
    return ParentNode("blockquote", childs)

def olist_to_html(text):
    split_text = text.split("\n")
    olist = []
    for line in split_text:
        strip_line = line[3:]
        text_node = text_to_textnodes(strip_line)
        childs = text_to_child(text_node)
        olist.append(ParentNode("li", childs))
    return ParentNode("ol", olist)


def ulist_to_html(text):
    split_text = text.split("\n")
    ulist = []
    for line in split_text:
        strip_line = line[2:]
        text_node = text_to_textnodes(strip_line)
        childs = text_to_child(text_node)
        ulist.append(ParentNode("li", childs))
    return ParentNode("ul", ulist)

def paragraph_to_html(text):
    lines = text.split("\n")
    text_join = ""
    for line in lines:
        if text_join == "":
            text_join = line
        else:
            text_join += f" {line}"
    text_node = text_to_textnodes(text_join)
    childs = text_to_child(text_node)
    return ParentNode("p", childs)

def text_to_child(text):
    child_nodes = []
    for line in text:
        node = text_node_to_html_node(line)
        child_nodes.append(node)
    return child_nodes
        
