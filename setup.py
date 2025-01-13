from setuptools import setup, find_packages

setup(
    name="pyressim",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "scipy",
        "matplotlib",
        "pyvista",
        "setuptools"
    ],
    author="Mario",
    description="PyResSim: A Next-Gen Reservoir Simulator",
    url="https://github.com/yourusername/pyressim",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)