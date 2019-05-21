from setuptools import setup

setup(
    name='polygon-pascalvoc-writer',
    version='1.1',
    description='Simple module to write Pascal VOC xml files. Currently supports boundingBoxes and polygons.',
    url='https://github.com/EvitanRelta/polygon-pascalvoc-writer',
    author='EvitanRelta',
    license='MIT',
    keywords='polygon pascal voc annotation writer xml',
    packages=['polygon_pascalvoc_writer'],
    include_package_data=True,
    install_requires=['jinja2'],
)
