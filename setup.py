if __import__("os").name == "nt":
    raise RuntimeError("cajuibot does not support Windows directly. Instead, you should install the Windows Subsystem for Linux (https://docs.microsoft.com/en-us/windows/wsl/install-win10) and then install plaft within that.")

from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README    

setup(
    name='cajuibot',
    version='1.0.0',
    description='Simple bot for automating Cajui',
    long_description=readme(),
    long_description_content_type= 'text/markdown',
    author='Felipe Cézar de Castro Antunes',
    author_email='cezarfelipe@gmail.com',
    url='https://github.com/felipecezar/cajuibot',
    license='GPLv3',
    install_requires=['selenium'],
    packages=['cajuibot'],
    include_package_data=True,
    entry_points={
        'console_scripts': ['cajuibot=cajuibot.__main__:main']
    }
)