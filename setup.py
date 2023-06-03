from setuptools import setup
  
setup(
    name='namusi',
    version='0.0.1',
    description='AutoScript TEM SQA Toolkit',
    author='Jan Zatloukal',
    author_email='zatloukal.jan@gmail.com',
    packages=['namusi'],
    install_requires=[
        'pygame'
    ],
    py_modules=["namusi"],
    entry_points={"console_scripts": ["namusi = namusi.__main__:main"]},
)