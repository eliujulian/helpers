import os
import openpyxl
import pandas as pd
import string

__version__ = '0.2'
__date_created__ = '2016.11.16'


def filenames_with_path(folder_path: str, limit_ending=None, excluded_starts=('~', )):
    """
    Function returns a list of all files from a folder and subfolders.
    :param folder_path: str
    :param limit_ending: str
    :param excluded_starts: tuple, default: ('~', )
    :return: list
    """
    result = []
    for dirpath, subfolder, files in os.walk(folder_path):
        for f in files:
            if f[0] in excluded_starts:
                pass
            elif not limit_ending:
                result.append(os.path.join(dirpath, f))
            elif limit_ending:
                if f.endswith(limit_ending):
                    result.append(os.path.join(dirpath, f))
    return result


def load_table_from_xlsx(file_path, sheet_name=None, skip_rows=0):
    """
    Function loads data from an excel file as list from lists
    :param file_path: path to an xlsx file
    :param sheet_name: name of the sheet. If not specified, first sheet will be read.
    :param skip_rows: skiprows at the beginning of xlsx file
    :return: list of lists.
    """
    V = list(string.ascii_uppercase)
    wb = openpyxl.load_workbook(file_path, data_only=True)

    if not sheet_name:
        sheet_name = wb.sheetnames[0]

    sh = wb.get_sheet_by_name(sheet_name)

    width = 0
    while True:
        if sh[V[width] + str(skip_rows + 1)].value:
            width += 1
        else:
            break

    length = 0 + skip_rows
    while True:
        if sh['A' + str(length + 1)].value:
            length += 1
        else:
            break

    result = []
    for v in V[:width]:
        col = []
        for h in range(1 + skip_rows, length):
            col.append(str(sh[v + str(h)].value))
        result.append(col)

    r = []
    for i, n in enumerate(result[0]):
        x = []
        for c in result:
            x.append(c[i])
        r.append(x)
    return r
