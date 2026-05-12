from textnode import TextNode, TextType
import os
import shutil

def main():
    public_directory = "public"
    static_dir = "static"
    if os.path.exists(public_directory):
        shutil.rmtree(public_directory)
    os.mkdir(public_directory)
    copy_static(static_dir, public_directory)

def copy_static(static, public):
    dir_list = os.listdir(static)
    print(dir_list)
    for dir in dir_list:
        path = os.path.join(static, dir)
        if os.path.isfile(path):
            shutil.copy(path, public)
        else:
            pub_path = os.path.join(public, dir)
            os.mkdir(pub_path)
            copy_static(path, pub_path)

    
def extract_title(markdown):
    if not markdown.startwith('# '):
        raise Exception("does not have an h1 header title")
    markdown.strip('#')



main()