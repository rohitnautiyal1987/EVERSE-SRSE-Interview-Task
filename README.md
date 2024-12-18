# EVERSE-SRSE-Interview-Task
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is structured to create a Python package for ontology lookup. The package will allow you to run a command-line script to query ontologies using an ID.

## Project Directory Structure
```
EVERSE-SRSE-Interview-Task/    
|-- task1/
|   |-- __init__.py
|   `-- ontology_lookup.py
|-- setup.py
|-- README.md
`-- requirements.txt
```

### 1. Create the `setup.py` File

The `setup.py` file defines the package metadata and configuration, making it executable from the command line.

### 2. Create `ontology_lookup.py` in `task1/`

This is the main script that will handle the ontology lookup process.

### 3. Create a `requirements.txt` File

Include any dependencies in this file. For example:


### 4. Build and Install the Package

Follow these steps to build and install the package:

1. In the terminal, navigate to the root directory of your project (where `setup.py` is located).
    ```bash
   cd EVERSE-SRSE-Interview-Task
2. Build the package.
    ```bash
   python setup.py sdist bdist_wheel
4. Install the package locally.
    ```bash
   pip install .
### 5. Usage
Once installed, you can use the following command from the command line to execute the script.
```bash
 ontology-lookup <ontology_id>

