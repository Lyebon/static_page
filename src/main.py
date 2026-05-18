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
    docs = Path("docs")
    if os.path.exists(docs):
        shutil.rmtree(docs)
    os.mkdir(docs)
    copy_static(Path("static"), public)
    generate_pages_recursive(Path("content"), "template.html", docs, basepath)


def copy_static(static, docs):
    dir_list = os.listdir(static)
    for dir in dir_list:
        path = os.path.join(static, dir)
        if os.path.isfile(path):
            shutil.copy(path, docs)
        else:
            pub_path = os.path.join(docs, dir)
            os.mkdir(pub_path)
            copy_static(path, pub_path)


main()
