from setuptools import setup, find_packages # type: ignore

setup(
    name='weather-cli',
    version='0.1.0',
    author='Rajnish',
    description='A cross-platform weather CLI application',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'click>=8.0.0',
        'requests>=2.26.0',
        'tabulate>=0.8.9'
    ],
    entry_points={
        'console_scripts': [
            'weather=cli.main:cli',
        ],
    },
    python_requires='>=3.6',
)