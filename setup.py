from setuptools import setup, find_packages

setup(
    name="fluxion",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "scipy",
        "matplotlib",
        "pyvista"
    ],
    author="Mario",
    description="Fluxion: A Next-Gen Reservoir Simulator",
    url="https://github.com/yourusername/fluxion",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)