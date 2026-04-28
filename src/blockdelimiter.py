from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    if block[0] == "#":
        for i in range(0, 6):
            if block[i] == "#" and block[i+1] == " ":
                return BlockType.HEADING
    elif block[0] == "`":
        for i in range(0,3):
            if block[i] == "`" and block[-i] == "`":
                return BlockType.CODE
    elif block[0] == ">" and block[1] != "":
        return BlockType.QUOTE
    elif block[0] == "-" and block[1] == " ":
        return BlockType.UNORDERED_LIST
    elif block[0] == "1" and block[1] == "." and block[2] == " ":
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH