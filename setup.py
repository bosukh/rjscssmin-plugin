from setuptools import setup

setup(
    name='rjscssmin-plugin',
    url='https://github.com/bosukh/rjscssmin-plugin',
    author='Ben Hong',
    author_email='benbosukhong@gmail.com',
    description='wrapper around rjsmin and rcssmin to easily use them',
    version='1.0.1',
    py_modules = ['rjscssmin-plugin'],
    zip_safe=False,
    include_package_data=True,
    license='MIT',
    install_requires=[
        'rJSmin',
	'rCSSmin',
        'htmlmin'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Markup :: HTML'
    ],
    keywords='minify css js'
)
