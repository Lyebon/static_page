from blockdelimiter import markdown_to_html_node
import os


def extract_title(markdown):
    split_markdown = markdown.split("\n")
    for line in split_markdown:
        if line.startswith("# "):
            strip_text = line.strip('# ')
            return strip_text
    raise Exception("does not have an h1 header title")
    

def read_file(file):
    with open(file) as f:
        text = f.read()
        return text

def write_file(path, template):
    with open(path, "w") as f:
        f.write(template)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = read_file(from_path)
    template = read_file(template_path)
    title = extract_title(markdown)
    html_nodes = markdown_to_html_node(markdown)
    title_template = template.replace("{{ Title }}", title)
    content = html_nodes.to_html()
    final_template = title_template.replace("{{ Content }}",content)
    directory = os.path.dirname(dest_path)
    os.makedirs(directory, exist_ok=True)
    write_file(dest_path, final_template)
