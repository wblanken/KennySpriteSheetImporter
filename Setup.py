# Kenny Sprite Sheet Slicer
# Setup.py
# Copyright Will Blankenship 2015

from setuptools import setup, find_packages

setup(
    name='KennySpriteSheetImporter',
    version='0.0.2',
    description='An importer for sprite sheets.',
    long_description='A simple importer for sprite sheets in the Kenny donation collection into Unity',
    url='https://github.com/wblanken/KennySpriteSheetImporter',
    author='Will Blankenship',
    author_email='blankenship.will@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5'
    ],
    keywords='Unity Import Sprite',
    packages=find_packages(),
    install_requires=['Pillow==3.0.0'],
    entry_points={
        'console_scripts': [
            'main=main:main'
        ]
    }
)
