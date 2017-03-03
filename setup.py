from setuptools import setup

setup(
    name='rjscssmin-plugin',
    author='Ben Hong',
    author_email='benbosukhong@gmail.com',
    description='wrapper around rjsmin and rcssmin to easily use them',
    version='1.0.0',
    py_modules = ['rjscssmin-plugin'],
    license='MIT',
    install_requires=[
        'rJSmin',
	'rCSSmin',
        'htmlmin'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
    keywords='minify css js'
)
