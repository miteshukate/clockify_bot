from setuptools import setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["requests>=2"]

setup(
    name='Clockify_Bot',
    version='0.0.1',
    packages=['Clockify_Bot'],
    url='',
    license='MIT',
    author='mitesh.ukate',
    author_email='miteshukate@gmail.com',
    install_requires=requirements,
    description='Clockify Bot'
)
