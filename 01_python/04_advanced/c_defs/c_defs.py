#!/usr/bin/env python3
"""This script reads c header files and generates excel sheet with function
prototypes"""

import sys
import os
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from pycparser import c_ast, parse_file
from typing import cast, TypeAlias

from pycparser.c_parser import ParseError

Prototype: TypeAlias = tuple[str, str]


def node_tostring(node: c_ast.Node) -> str | tuple[str, str | None] | None:
    """Converts a c_ast node to a string or tuple of strings"""
    if node is None:
        return None
    elif isinstance(node, c_ast.Decl):
        return node_tostring(node.type)
    elif isinstance(node, c_ast.FuncDef):
        return node_tostring(node.decl.type)
    elif isinstance(node, c_ast.Typename):
        return node_tostring(node.type)
    elif isinstance(node, c_ast.FuncDecl):
        name = node_tostring(node.type)
        if type(name) is tuple:
            name = name[0] + (' ' + name[1]) if name[1] else ''

        params = node_tostring(node.args) if node.args else 'void'
        decl = "{}({});".format(name, params)
        return decl
    elif isinstance(node, c_ast.ParamList):
        def map_params(node):
            param = cast(tuple, node_tostring(node))
            if param[1] is None:
                return param[0]
            return ' '.join(param)

        return ", ".join(map(map_params, node.params))
    elif isinstance(node, c_ast.TypeDecl):
        _type = cast(tuple, node_tostring(node.type))
        return (_type[0], node.declname)
    elif isinstance(node, c_ast.IdentifierType):
        return (node.names[0], None)
    elif isinstance(node, c_ast.PtrDecl):
        _type = cast(tuple, node_tostring(node.type))
        return (_type[0], '*' + _type[1] or '*')
    elif isinstance(node, c_ast.ArrayDecl):
        _type = cast(tuple, node_tostring(node.type))
        const = node.dim.value if node.dim else ''
        return (_type[0], _type[1] + f'[{const}]')
    else:
        raise TypeError("Unsupported node type: {}".format(type(node)))


def generate_prototypes(filename: str) -> list[Prototype]:
    """Generates a list of function prototypes from c source code file

        Args:
            filename (str): The c code filename."""

    ast = parse_file(
        filename,
        use_cpp=True,
        cpp_path='gcc',
        cpp_args=['-E', r'-Iutils/fake_libc_include']
    )
    prototypes = []

    for node in ast.ext:
        try:
            decl = node_tostring(node)
        except TypeError:
            continue

        prototypes.append((str(node.coord), decl))

    return prototypes


def write_sheet(prototypes: list[Prototype], sheet: Worksheet):
    """Writes a list of function prototypes to an excel sheet

    Args:
        prototypes (list[Prototype]): The list of function prototypes.
        sheet (Worksheet): The excel sheet."""
    counter = 0
    cols = ['A', 'B', 'C']
    dimensions = [5, 5, 5]
    sheet.append(['Id', 'Prototype', 'Location'])

    for prototype in prototypes:
        row = ['IDX{:03}'.format(counter), prototype[1], prototype[0]]

        for i, val in enumerate(row):
            length = len(val) + 5
            if length > dimensions[i]:
                dimensions[i] = length

        sheet.append(row)
        counter += 1

    for i, col in enumerate(cols):
        sheet.column_dimensions[col].width = dimensions[i]


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <workbook_name> <...filenames>")
        print("\t<workbook_name> is the name of the output excel file: *.xlsx")
        print("\t<filenames> are the name of the c source files: *.c")
        exit(1)

    wb = Workbook()
    if wb.active:
        wb.remove(cast(Worksheet, wb.active))

    for filename in sys.argv[2:]:
        name = os.path.basename(filename)
        try:
            prototypes = generate_prototypes(filename)
        except ParseError as err:
            print(f"Failed to parse {filename}:")
            print(err)
            continue

        sheet = wb.create_sheet(name)
        write_sheet(prototypes, sheet)

    wb.save(sys.argv[1])
