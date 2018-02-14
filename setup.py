from distutils.core import setup

setup(
    name='p_toolkit',
    version='v1.0',
    author='Amy Goldlist, Veronique Mulholland and Esteban Angel',
    packages=['src',],
    license='MIT',
    long_description=open('README.md').read(),
)



setup(

    author='J. Random Hacker',
    author_email='jrh@example.com',
    packages=['towelstuff', 'towelstuff.test'],
    scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='Useful towel-related stuff.',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.1.1",
        "caldav == 0.1.4",
    ],
)
