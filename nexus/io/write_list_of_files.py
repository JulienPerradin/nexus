import os
from collections import OrderedDict
from natsort import natsorted

def write_list_of_files(dirpath : str) -> None:
    r"""
    Write a list of the all-in-one unwrapped clusters file to a text file.
    """
    
    # Create the list of files
    ordered_files = OrderedDict()
    for root, dirs, files in os.walk(dirpath):
        files = natsorted(files)
        for file in files:
            if file.endswith("all-in-one.xyz"):
                path = os.path.join(root, file)
                ordered_files[path] = None
                
    # Write the list of files to a text file
    with open(os.path.join(dirpath, "list.txt"), "w") as f:
        for file in ordered_files:
            f.write(file + "\n")