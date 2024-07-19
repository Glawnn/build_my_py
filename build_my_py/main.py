
import argparse
from build_my_py.parsers import add_subparser_create, add_subparser_build, add_subparser_test, add_subparser_format, add_subparser_lint
import os

class App:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description="A Python Tool to create and manage Python projects")
        subparsers = self.parser.add_subparsers(dest="mode")
        add_subparser_create(subparsers)
        add_subparser_build(subparsers)
        add_subparser_test(subparsers)
        add_subparser_format(subparsers)
        add_subparser_lint(subparsers)
    
    def run(self):
        args = self.parser.parse_args()
        print(vars(args))


def main():
    app = App()
    app.run()
    
#     """ create new folder and setup my python project"""
#     curent_path = os.getcwd()
#     project_name = input("Enter the name of your project: ")
#     os.mkdir(project_name)
#     os.mkdir(f"{project_name}/tests")
#     os.mkdir(f"{project_name}/{project_name}")

#     def generate_setup():

#         return f"""
# from setuptools import setup, find_packages

# setup(
#     name="{project_name}",
#     version="0.1.0",

#     description="A Python Tool to create and manage Python projects",
#     long_description="toto",
#     long_description_content_type='text/markdown',
#     author="Vodkas",
#     author_email="",

#     entry_points={{
#         "console_scripts": [
#             "{project_name.replace('_', '-')}={project_name}.main:main"
#         ]
#     }},
#     packages=find_packages(exclude=("tests")),
#     install_requires=[
#     ],
# )

# """

#     def generate_main():
#         return f"""
# def main():
#     print("Hello, World!")
    
# if __name__ == "__main__":
#     main()
# """



if __name__ == "__main__":
    main()