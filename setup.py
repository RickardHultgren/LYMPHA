try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

setup(
    name='lympha',
    version='1.0',
    author='Rickard Verner Hultgren',
    author_email='rihu0003@student.umu.se',
    packages=['lympha'],
    url='https://github.com/RickardHultgren/lympha/tree/python',
    license='LICENSE.txt',
    description='LYMPHA is a logical language for formulating and handling medical algorithms.',
)
