# Nexus - Cluster Analysis Toolkit

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description and features

`nexus-cat` is a package designed to find clusters of connected polyhedra in an atomistic simulation trajectory. It provides functionality to analyze properties of the clusters such as the average cluster size, biggest cluster, gyration radius, and correlation length.

## Installation

To install `nexus-cat`, first clone this repository as you please, for example with SSH:

```bash
git clone git@github.com:JulienPerradin/nexus.git
```
Then you can use pip, it will install dependencies and the main package in your Python environment:

```bash
pip install nexus-cat==0.1.3
```


## Usage

As a first example you can run the script `launch-nexus-quick-test.py`:

```bash
cd nexus-cat/ 
python examples/launch-nexus-quick-test.py
```

This script will run the analysis on a small 1008 atoms SiO2 glass (300K, 10GPa)

Please refer to the documentation for more information on how to use the package. You will also find more examples in the `examples` folder.

## Documentation

The documentation is available [here](https://github.com/JulienPerradin/nexus-cat/tree/main/doc)

## Contributing

Contributions to NEXUS-CAT are welcome! You can contribute by submitting bug reports, feature requests, new extension requests, or pull requests through GitHub.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Contact

For questions or inquiries, you can contact us at (julien.perradin@umontpellier.fr).
