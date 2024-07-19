from setuptools import setup, find_packages


setup(
    name="build_my_py",
    version="0.1.0",

    description="A Python Tool to create and manage Python projects",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    author="Vodkas",
    author_email="vodkas3630@gmail.com",
    url="https://github.com/Glawnn/PrettyPi",
    license="MIT",
    packages=find_packages(exclude=("tests")),
    install_requires=[
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "build-my-py=build_my_py.main:main"
        ]
    }
)