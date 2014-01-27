from setuptools import setup, find_packages


setup(
    name = 'vaccine',
    version = '0.0.1',
    author = 'Daniel Duckworth',
    author_email = 'duckworthd@gmail.com',
    description = "A simple dependency injection framework",
    license = 'BSD',
    keywords = 'di dependency injection',
    url = 'http://github.com/duckworthd/vaccine',
    packages = find_packages(),
    classifiers = [
      'Development Status :: 4 - Beta',
      'License :: OSI Approved :: BSD License',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
    ],
    install_requires = [     # dependencies
    ],
)
