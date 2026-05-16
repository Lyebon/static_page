import os
import shutil
import sys
from gencontent import generate_pages_recursive
from pathlib import Path


def main():
    if len(sys.argv)>1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    public = Path("public")
    if os.path.exists(public):
        shutil.rmtree(public)
    os.mkdir(public)
    copy_static(Path("static"), public)
    generate_pages_recursive(Path("content"), "template.html", public)


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