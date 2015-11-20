# Script Name	: check-file-exists.py
# Author		: Shailendra Patel
# Created		:
# Last Modified	:
# Version		:

# Description	: Batch rename file extensions.

import os,sys

if len(sys.argv) == 4:
    work_dir = sys.argv[1]
    old_ext = sys.argv[2]
    new_ext = sys.argv[3]

    files = os.listdir(work_dir)
    for filename in files:
        file_ext = os.path.splitext(filename)[1]
        if old_ext == file_ext:
            newfile = filename.replace(old_ext, new_ext)
            os.rename(os.path.join(work_dir, filename), os.path.join(work_dir, newfile))
else:
    print("Usage: ", str(sys.argv[0]), "directory old-ext new-ext")
