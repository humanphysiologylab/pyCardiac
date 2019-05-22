from setuptools import setup

setup(name='pyCardiac',
      version='0.1',
      description='Basic toolkits to process Action Potential signals',
      url='https://github.com/humanphysiologylab/pyCardiac',
      author='Human Physiology Lab',
      author_email='dmitrii.smirnov@phystech.edu',
      license='MIT',
      packages=['pyCardiac'],
      zip_safe=False,
      platforms='any',
      install_requires=['numpy>=1.16.2','scipy>=1.2.1']
      )
