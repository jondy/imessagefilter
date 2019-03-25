from os import path
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = '0.2.1'

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()


setup(
    name='imessagefilter',

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    version=__version__,
    description='A python package implements interface IMessageFilter for COM',
    long_description=long_description,

    url='https://github.com/jondy/imessagefilter',
    author='Jondy Zhao',
    author_email='jondy.zhao@gmail.com',

    platforms=['Windows'],

    # For a list of valid classifiers, see
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Support platforms
        'Operating System :: Microsoft :: Windows',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],

    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a string of words separated by whitespace, not a list.
    keywords='COM IMessageFilter',

    packages=['imessagefilter'],
    package_dir={'imessagefilter': '.'},
    package_data={
        'imessagefilter': [
            'README.md', 'LICENSE', 'msgfilter.c', 'msgfilter.dll'
        ],
    },
)
