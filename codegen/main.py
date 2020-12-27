#!/usr/bin/env python3

import sys

import db
import define


def main():
    schema_name = sys.argv[1]
    out_fname = sys.argv[2]
    db.connect()
    fns = db.load_schema_functions(schema_name)
    print("loaded {} fns on ".format(len(fns), schema_name))
    scala_fn_defs = [
        define.get_impl_language_def(schema_name, fn)
        for fn in fns]
    scala_contents = "\n".join(scala_fn_defs)
    scala_output = define.get_impl_language_wrapping_def(
        scala_contents)
    print("writing output to {}".format(out_fname))
    with open(out_fname, "w") as f:
        f.write(scala_output)
    return


if __name__ == '__main__':
    main()
