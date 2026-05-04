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
        pass
