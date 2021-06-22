from setuptools import setup


setup(
    name='jsonfield-joinup',
    version='2.1.2',
    packages=['jsonfield'],
    license='MIT',
    include_package_data=True,
    author='Joinup',
    author_email='desarrollo@joinup.es',
    url='https://github.com/we-are-Joinup/jsonfield',
    description='A reusable Django field that allows you to store validated JSON in your model.',
    long_description=open("README.rst").read(),
    install_requires=['Django >= 1.11', 'six'],
    tests_require=['Django >= 1.11', 'six'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
    ],
)
