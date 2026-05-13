from blockdelimiter import markdown_to_html_node

def main():
    generate_page('content/index.md', 'template.html', 'public')
    pass

def extract_title(markdown):
    split_markdown = markdown.split("\n")
    for line in split_markdown:
        if line.startswith("# "):
            strip_text = line.strip('# ')
            return strip_text
    raise Exception("does not have an h1 header title")
    

def read_file(file):
    markdown = open(file, "r")
    return markdown.read()

def write_file(file):
    pass


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = read_file(from_path)
    template = read_file(template_path)
    title = extract_title(markdown)
    html_nodes = markdown_to_html_node(markdown)
    template.replace("Title", title)
    content = html_nodes.to_html()
    template.replace("Content",content)


main()