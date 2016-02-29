from setuptools import setup, find_packages

setup(
    name = "boids",
    version = "1.0 ",
    packages = find_packages(exclude=['*test']),
    license = "Apache",
    package_data={
        '': ['*.yml']
    },
    author_email = 'paul.s.brookes@gmail.com',
    install_requires = ['numpy', 'matplotlib', 'nose', 'argparse'],
    scripts = ['scripts/boids']
)
