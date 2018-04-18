from distutils.core import setup

setup(
    name='POC_Frame_Images',
    version='0.1.0',
    author='T K Sourab',
    author_email='sourabhtk37@gmail.com',
    packages=['solution'],
    url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='Retrieves images for each video frame and points of interest',
    long_description=open('README.txt').read(),
    install_requires=[
        "Pillow==5.1.0",
        "simplekml==1.3.0"
    ],
)
