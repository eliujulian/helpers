import os


__version__ = '0.1'
__date_created__ = '2016.11.14'


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
