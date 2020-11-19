from setuptools import setup

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(name='htb.py',
      author='AlienX',
      url='',
      project_urls={
        "Documentation": "",
        "Issue tracker": "",
      },
      version="0.1",
      license='MIT',
      description='A Python wrapper for the HackTheBox API',
      long_description='',
      long_description_content_type="text/x-rst",
      include_package_data=True,
      install_requires=requirements,
      python_requires='>=3.5.3',
)