## helpers

Various helpers I used in different projects.

### file_handling.py

**filenames_with_path(folder_path: str, limit_ending=None, excluded_starts=('~', ))**

* param: folder_path: str,
 
    path of a directory
* param: limit_ending: str, 

    only includes files with a specified ending. If none is specified all files are included
    
* param: excluded_starts: tuple, default: ('~', )
 
    specify this to exclude files with a special start character like '~' (temporary files)
 

* returns: List of all filenames in that directory and subdirectory in a flattend list. Filenames include full path.

**load_table_from_xlsx(file_path, sheet_name=None, skip_rows=0)**

* returns: List of List. Each inner list represents one row of the table from the xlsx table.

### Dependencies

openpyxl