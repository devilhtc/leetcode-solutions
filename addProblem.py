#!/Users/devilhtc/.envs/py3env/bin/python
import sys
import os

HEX_LEN = 4


def hello(a, b):
    print("hello and that's your sum:", a + b)


def createFile(filename):
    f = open(filename, "w+")
    f.close()


def createDir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    else:
        print()
        print("Directory already exists")


def toHexString(num, hexlen):
    hexStr = hex(num)
    hexStr = hexStr[:2] + "0" * (hexlen + 2 - len(hexStr)) + hexStr[2:]
    return hexStr


def createProblem(args, verbose=False):
    ext = ".py"
    if len(args) > 0 and args[0] == "-j":
        ext = ".java"
        args = args[1:]
    dirname = (
        toHexString(int(float(args[0])), HEX_LEN)
        + "_"
        + args[0].strip(".")
        + "."
        + "_".join(args[1:])
    )

    if verbose:
        print("creating directory: " + dirname)
    createDir(dirname)
    solutionFileName = dirname + "/solution" + ext
    if verbose:
        print("creating file: " + solutionFileName)
    createFile(solutionFileName)


if __name__ == "__main__":
    allArgs = sys.argv[1:]
    createProblem(allArgs, verbose=True)
