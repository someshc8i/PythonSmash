#!/usr/bin/env python3

"""Main executable for PythonSmash compiler
For usage, run "./pythonsmash.py --help".
"""

import argparse
from lexer import lex


def get_arguments():
    """Set up the argument parser and return an object storing the
    argument values.
    return - An object storing argument values, as returned by
    argparse.parse_args()
    """

    parser = argparse.ArgumentParser(description="Compile ps files.")

    # The file name of the ps file to compile. The file name gets saved to the
    # file_name attribute of the returned object, but this parameter appears as
    # "filename" (no underscore) on the command line.
    parser.add_argument("file_name", metavar="filename")
    return parser.parse_args()


def compile_code(source):
    """Compile the provided source code into assembly.
    source - The C source code to compile.
    return - The asm output
    """
    tokens = lex(source)
    for token in tokens:
        print(token)
    return source


def main():
    """Load the input files and dispatch to the compile function for the main
    processing.
    The main function handles interfacing with the user, like reading the
    command line arguments, printing errors, and generating output files. The
    compilation logic is in the compile_code function to facilitate testing.
    """
    arguments = get_arguments()

    try:
        ps_file = open(arguments.file_name)
    except IOError:
        print("pythonsmash: error: no such file or directory: '{}'"
              .format(arguments.file_name))
    else:
        compile_code(ps_file.read())
        ps_file.close()


if __name__ == "__main__":
    main()
