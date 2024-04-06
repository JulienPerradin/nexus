# Import the package
import clstr

# Load trajectory data
trajectory = "/home/perraju/Documents/thesis/test-NS3/3000at/B-part/positions_xyz/pos60B.xyz"

# Initialize settings
settings = clstr.settings.Settings(extension="SiOz")

# Set project name
name = "test-NS3-pos60B"
settings.name_of_the_project.set_value(name)

# Set extension
settings.extension.set_value("SiOz")

# Set export directory
settings.export_directory.set_value(f"tests/results/{name}")

# Set path to XYZ file
settings.path_to_xyz_file.set_value(trajectory)

# Set number of atoms
settings.number_of_atoms.set_value(3000)

# Set header
settings.header.set_value(2)

# Set structure
settings.structure.set_value([
                {"element": "Si", "alias": 2, "number": 750},
                {"element": "O" , "alias": 1, "number": 1750},
                {"element": "Na" , "alias": 3, "number": 500}
            ])

# Set temperature
settings.temperature.set_value(300) 

# Set pressure
settings.pressure.set_value(13.598809341600003)

# Set to print cluster positions
settings.print_clusters_positions.set_value(False)

# Set range of frames
settings.range_of_frames.set_value([4, 6])

# Set cluster settings
settings.cluster_settings.set_cluster_parameter("connectivity", ["Si", "O", "Si"])
settings.cluster_settings.set_cluster_parameter("criteria", "bond")
settings.cluster_settings.set_cluster_parameter("polyhedra", [[4, 4], [5, 5], [6, 6]])

# Execute the main function with the provided settings
clstr.main(settings)
