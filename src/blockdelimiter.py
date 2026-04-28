# import enum

# class BlockType(enum):
#     pass




# def markdown_to_blocks(markdown):
#     final_block= []
#     blocks = markdown.split("\n\n")
#     for section in blocks:
#         temp = ""
#         sentences = section_manipulator(section)
#         for part in sentences:
#             if temp == "":
#                 temp = part
#             else:
#                 temp += f"\n{part}"
#         if temp != "":
#             final_block.append(temp)
#     return final_block

# def section_manipulator(section):
#     sentences = []
#     splitter = section.split("\n")
#     for part in splitter:
#         if part.strip() == "":
#             continue
#         else:
#             sentences.append(part.strip())
#     return sentences

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks