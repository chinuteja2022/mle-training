from setuptools import setup, find_packages

setup(
    name="housing_project",
    version="0.2",
    description="This code is nonstandard code",
    long_description="This code is used to create a installable package",
    author="Sai Ram Teja",
    # packages=["housing_project"],
    packages=find_packages(where='src', include=['housing_project'],),
    package_dir={"": "src"},
    install_requries=[],
)
