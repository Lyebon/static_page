from blockdelimiter import markdown_to_html_node
import os
import pathlib


def extract_title(markdown:str) -> str:
    split_markdown = markdown.split("\n")
    for line in split_markdown:
        if line.startswith("# "):
            strip_text = line.strip('# ')
            return strip_text
    raise Exception("does not have an h1 header title")
    

def read_file(file:str) ->str:
    with open(file) as f:
        text = f.read()
        return text

def write_file(path: pathlib.Path, template: pathlib.Path) -> None:
    with open(path, "w") as f:
        f.write(template)


def generate_page(content_path: pathlib.Path, template_path: pathlib.Path, public_path: pathlib.Path) -> None:
    print(f"Generating page from {content_path} to {public_path} using {template_path}")
    markdown = read_file(content_path)
    template = read_file(template_path)
    title = extract_title(markdown)
    html_nodes = markdown_to_html_node(markdown)
    title_template = template.replace("{{ Title }}", title)
    content = html_nodes.to_html()
    full_template = title_template.replace("{{ Content }}",content)
    image_template = full_template.replace('scr="/', 'src="{basepath}')
    final_template = image_template.replace('href="/', 'href="{content_path}')
    directory = os.path.dirname(public_path)
    os.makedirs(directory, exist_ok=True)
    write_file(public_path, final_template)

def generate_pages_recursive(dir_path_content: pathlib.Path, template_path: pathlib.Path, dest_dir_path: pathlib.Path) -> None:
    content_dir = os.listdir(dir_path_content)
    for content in content_dir:
        content_path = dir_path_content/content
        if os.path.isfile(content_path):
            public_path = content
            generate_page(content_path, template_path, public_path)
        else:
            public_path = content
            generate_pages_recursive(content_path, template_path, public_path)