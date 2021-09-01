from setuptools import setup, find_packages

with open("README.md", 'rt', encoding='UTF8') as fh:
    long_description = fh.read()


setup(
    name="MakePPTX",
    version="0.0.1",
    author="김민규",
    author_email="rlaalsrb4175@gmail.com",
    description="Making big size PPTX",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Indian966/MakePPTX",
    packages=find_packages('code', exclude=['test']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)