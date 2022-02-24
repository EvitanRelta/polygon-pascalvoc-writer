from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='polygon-pascalvoc-writer',
    version='1.0.2',
    description='For generating Pascal VOC XML image annotation files',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',

    url='https://github.com/EvitanRelta/polygon-pascalvoc-writer',
    author='EvitanRelta',
    author_email='shauntanzongzhi@gmail.com',

    keywords='polygon pascal voc pascalvoc annotation writer xml python',
    packages=['polygon_pascalvoc_writer'],
    include_package_data=True,
    install_requires=['jinja2']
)
