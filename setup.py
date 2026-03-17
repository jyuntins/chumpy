from setuptools import setup
from runpy import run_path

def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#")
        ]

def get_version():
    namespace = run_path("chumpy/version.py")
    return namespace["version"]

setup(
    name="chumpy",
    version=get_version(),
    packages=["chumpy"],
    author="Matthew Loper",
    author_email="matt.loper@gmail.com",
    url="https://github.com/mattloper/chumpy",
    description="chumpy",
    license="MIT",
    install_requires=read_requirements(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
    ],
)