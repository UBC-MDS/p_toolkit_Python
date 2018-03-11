from distutils.core import setup

setup(
    name='p_toolkit',
    version='v1.0',
    author='Amy Goldlist, Veronique Mulholland and Esteban Angel',
    packages=['p_toolkit'],
    license='MIT',
    description='A toolkit for adjusting and visualizing p values.',
    url = ['https://github.com/UBC-MDS/p_toolkit_Python'],
    download_url = 'https://github.com/UBC-MDS/p_toolkit_Python/archive/3.1.tar.gz',
    long_description=open('README.md').read(),
    keywords = ['testing','multiple-testing','p-values'],
    install_requires=[]
)
