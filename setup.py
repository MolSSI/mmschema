import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name="mmschema",
        version="1",
        description="A schema for classical & molecular mechanics",
        author="",
        url="https://github.com/MolSSI/mmschema",
        license="",
        packages=setuptools.find_packages(),
        install_requires=[
            "jsonschema",
        ],
        extras_require={
            "docs": [
                "sphinx==1.2.3",  # autodoc was broken in 1.3.1
                "sphinxcontrib-napoleon",
                "sphinx_rtd_theme",
                "numpydoc",
            ],
            "tests": [
                "pytest",
            ],
        },
        tests_require=[
            "pytest",
        ],
        zip_safe=True,
    )
