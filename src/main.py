import os
import shutil
from gencontent import generate_page

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")
    copy_static("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")


def copy_static(static, public):
    dir_list = os.listdir(static)
    for dir in dir_list:
        path = os.path.join(static, dir)
        if os.path.isfile(path):
            shutil.copy(path, public)
        else:
            pub_path = os.path.join(public, dir)
            os.mkdir(pub_path)
            copy_static(path, pub_path)


main()