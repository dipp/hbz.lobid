from setuptools import setup, find_packages
import os

version = '0.2'

setup(name='hbz.lobid',
      version=version,
      description="A client to the lobid API",
      long_description=open("README.rst").read() + "\n" +
      open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
      ],
      keywords='',
      author='Peter Reimer',
      author_email='reimer@hbz-nrw.de',
      url='',
      license='DFSL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['hbz'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'requests'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
