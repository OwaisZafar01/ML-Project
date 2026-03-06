from setuptools import setup, find_packages

def get_requirements(file_path):
    with open(file_path, 'r') as file:
        requirements = file.read().splitlines()
    if '-e .' in requirements:
        requirements.remove('-e .')
    return requirements

setup(
    name="ML-Project",  # Project's name
    version="0.0.1",  # Version number
    author="Hafiz Muhammad Owais Zafar",  # Author's name
    author_email="owaiszafar2004@example.com",  # Author's email
    description="General Machine Learning Project",  # Short description
    packages=find_packages(),  # Automatically sari modules include kar dega
    install_requires=get_requirements('requirements.txt'),  # Dependencies list
)