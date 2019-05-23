from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

import pyCardiac

setup(name='pyCardiac',
      version='0.1',
      description='Basic toolkits to process Action Potential signals',
      long_description=readme(),
      classifiers=[
                   'Development Status :: 3 - Alpha',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 3.0',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Topic :: Scientific/Engineering :: Medical Science Apps.',
                   ],
      keywords='Cardiac analysis',
      url='https://github.com/humanphysiologylab/pyCardiac',
      author='Human Physiology Lab',
      author_email='dmitrii.smirnov@phystech.edu',
      license='MIT',
      packages=['pyCardiac'],
      zip_safe=False,
      platforms='any',
      install_requires=['numpy>=1.16.2','scipy>=1.2.1'],
      include_package_data=True
      )
