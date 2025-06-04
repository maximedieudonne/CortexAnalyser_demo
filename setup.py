from setuptools import setup, find_packages

setup(
    name='cortexanalyser',
    version='0.1.0',
    description='Analyse et export de maillages cérébraux pour visualisation 3D',
    author='Ton Nom',
    author_email='ton.email@example.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'nibabel',
        'scipy',
    ],
    entry_points={
        'console_scripts': [
            'cortexanalyser=cortexanalyser.export:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.7',
)
