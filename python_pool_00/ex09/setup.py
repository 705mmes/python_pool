from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    author="neo Dansmatrix",
    author_email="smunio@student.42mulhouse.fr",
    description="A small example package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/705mmes/python_pool.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    python_requires=">=3.10",
    project_urls={
        "Homepage": "https://github.com/705mmes/python_pool.git",
        "Issues": "https://github.com/705mmes/python_pool.git",
    },
)
