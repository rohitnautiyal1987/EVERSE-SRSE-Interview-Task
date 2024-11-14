# Set up your project with the following directory structure:
EVERSE-SRSE-Interview-Task/                          # Source directory
├── task1/
│   ├── __init__.py
│   ├── ontology_lookup.py                           # Main script
├── setup.py                                         # Package metadata
├── README.md
├── requirements.txt                                # Python dependencies

1. Create the setup.py File : This file defines the package and makes it executable from the command line.

2. Create ontology_lookup.py. # Main script

3. Create a requirements.txt file include any dependencies in this file (in this case, just requests).

4. Build and Install the Package in the terminal, navigate to the root directory of your project (where setup.py is located) and run:
# In the terminal, navigate to the root directory of your project (where setup.py is located) and run:
# Build the package
python setup.py sdist bdist_wheel
# Install the package locally
pip install .

# Once installed, you can use the command ontology-lookup <ontology_id> from the command line to execute the code.
