from setuptools import setup

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(name='htb.py',
      author='AlienX',
      url='',
      project_urls={
        "Documentation": "https://github.com/AlienX2001/htb.py/blob/main/Documentation.md",
        "Issue tracker": "https://github.com/AlienX2001/htb.py/issues",
      },
      version="0.1",
      license='MIT',
      description='A Python wrapper for the HackTheBox API',
      include_package_data=True,
      install_requires=requirements,
      python_requires='>=3.5.3',
)
