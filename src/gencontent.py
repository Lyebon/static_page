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


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    text = open(from_path, 'r')
    template = open(template_path, 'r')
    read_text = text.readline()
    title = extract_title(read_text)
    template.replace('Title', title)
    print(template)

main()