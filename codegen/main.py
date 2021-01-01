#!/usr/bin/env python3

import argparse

import db
import define
from typez import DefineLang


parser = argparse.ArgumentParser()
parser.add_argument("--lang", type=DefineLang, help="output language")
parser.add_argument("--schema", type=str, help="db schema name")
# parser.add_argument("-o", type="str", nargs=1, help="output file")


def main():
    args = parser.parse_args()
    db.connect()
    fns = db.load_schema_functions(args.schema)
    output = define.get_def_file_contents(args.schema, args.lang, fns)
    print(output)
    # print("writing output to {}".format(out_fname))
    # with open(out_fname, "w") as f:
    #     f.write(scala_output)
    return


if __name__ == '__main__':
    main()
