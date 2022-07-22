import os

def run(**args):
    print("[*] In dir dirlister module.")
    files = os.listdir(".")
    return str(files)
    