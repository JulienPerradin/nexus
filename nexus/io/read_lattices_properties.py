import numpy as np

def read_lattices_properties(box, file_path, keyword="Lattice") -> None:
    r"""
    Create the Box object for each frame in the trajectory file.
    
    Parameters
    ----------
        - box (Box) : Box object to store the lattice properties.
        - file_path (str) : Path to the trajectory file containing the lattice properties.
        
    Returns:
    --------
        - None.
    """
    # Open the file once to read the data
    with open(file_path, "r") as f:
        data = f.readlines()
    f.close()
    
    # Saving the lattice properties only
    lattices = [line for line in data if keyword in line]
    
    # Iterate through the lattices and add them to the Box object
    for line in lattices:
        current_lattice = line.split('\"')[1]
        lx = float(current_lattice.split()[0])
        ly = float(current_lattice.split()[4])
        lz = float(current_lattice.split()[8])
        
        # Add the lattice to the Box object creating a new frame
        box.add_box(lx, ly, lz)