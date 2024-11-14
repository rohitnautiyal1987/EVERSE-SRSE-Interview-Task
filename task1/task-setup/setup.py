from setuptools import setup, find_packages

setup(
    name="ontology_lookup",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "ontology-lookup=ontology_lookup.ontology_lookup:main",
        ],
    },
    author="Your Name",
    description="A command-line tool to fetch ontology details using the Ontology Lookup Service API.",
    python_requires='>=3.6',
)
