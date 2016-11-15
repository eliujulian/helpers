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


### Dependencies

None outside the standard library.