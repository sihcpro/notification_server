import sys
import re
import subprocess
from ast import literal_eval
from setuptools import setup, find_packages


def run_command(command):
    p = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False
    )
    results = p.communicate()
    if p.returncode != 0:
        raise ValueError("Command did not return success code [0].")

    return results


def get_version(source: str):
    try:
        git_tag, _ = run_command(["git", "rev-parse", "--short", "HEAD"])
        git_tag = git_tag.decode("utf-8").replace("\n", "")
        if not re.match(r"^[a-f0-9]{7}$", git_tag):
            raise ValueError("Not a valid git tag: {}".format(git_tag))
    except ValueError:
        git_tag = "nogit"

    with open(source) as f:
        for line in f:
            variable, _, expr = line.partition("=")
            variable, expr = variable.strip(), expr.lstrip()
            if variable == "__version__" and expr:
                return "{}+{}".format(literal_eval(expr), git_tag)

    raise ValueError("__version__ not found")


def get_requirements(source: str = "requirements.txt"):
    requirements = []
    with open(source) as f:
        for line in f:
            package, _, comment = line.partition("#")
            package = package.strip()
            if package:
                requirements.append(package)

    return requirements


sys.path.insert(0, "./src")
version = get_version("src/notification_server/__init__.py")
# tests_require = get_requirements("requirements.dev.txt")
install_requires = get_requirements("requirements.txt")
long_description = open("README.md").read()

packages = find_packages("src")
# or can use
# `packages=find_packages(exclude=['sandbox', 'tests*'])`
# as setup argument

setup(
    name="notification_server",
    version=version,
    author="Sihc",
    author_email="tvquocchi@gmail.com",
    package_dir={"notification_server": "src/notification_server"},
    packages=packages,
    url="",
    license="No License",
    description="",
    long_description=long_description,
    install_requires=install_requires,
    # tests_require=tests_require,
    zip_safe=False,
    platforms="any",
    include_package_data=True,
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Stable" "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
