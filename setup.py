from setuptools import setup


def get_requirements():
    """Reads the installation requirements from test-requirements.pip"""
    with open("test-requirements.pip") as f:
        lines = f.read().split("\n")
        lines_without_comments = [line for line in lines if not line.startswith('#') and not line == '']
        return lines_without_comments


setup(install_requires=get_requirements())
