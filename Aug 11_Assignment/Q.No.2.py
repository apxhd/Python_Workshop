# Program to perform series of tasks


with open("old.txt", "w") as fp:
    fp.write("Hello World")

with open("old.txt", "r") as fp:
    with open("new.txt", "w") as fpr:
        fpr.write(fp.read())

with open("old.txt", "r") as ofp:
    with open("new.txt", "r") as nfp:
        if ofp.read() == nfp.read():
            print("Contents Copied")

