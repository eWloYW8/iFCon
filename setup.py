from setuptools import setup, find_packages

setup(
    name='iFCon',
    version='3.0',
    description='A tool for handling iFAction resource files (iFCon files)',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='eWloYW8',
    author_email='thenextone200612@gmail.com',
    url='https://github.com/eWloYW8/iFCon',
    license='GPLv3',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'iFCon=iFCon.iFCon:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)