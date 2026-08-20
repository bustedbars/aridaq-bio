from setuptools import setup, find_packages

setup(
    name="aridaq-bio",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["numpy>=1.24.0", "pandas>=2.0.0"],
)
