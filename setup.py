from setuptools import setup


def deps():
    with open('requirements.txt') as f:
        return f.readlines()

setup(
    name='clonesearch',
    version='1.0',
    long_description=__doc__,
    packages=['clonesearch'],
    include_package_data=True,
    install_requires=deps(),
    author='Anthony Grimes',
    description='Clone Github repos based on a search query.',
    license='MIT',
    url='https://github.com/Raynes/clonesearch',
    entry_points={
        'console_scripts': [
            'clones = clonesearch.__main__:entry'
            ],
        }
)
