def count_configurations(file_path, keyword="Lattice") -> int:
    r"""
    Count the number of configurations in the trajectory file.
    
    Parameters
    ----------
        - file_path (str) : Path to the trajectory file.
        - keyword (str) : Keyword to search in the file. Default is "Lattice".
        
    Returns:
    --------
        - int : Number of frames found in the input file.
    """
    
    # Open the file
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Count the number of configurations
    n_config = 0
    for line in lines:
        if keyword in line:
            n_config += 1
    
    return n_config