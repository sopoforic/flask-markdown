"""
Flask-Markdown
--------------

This is a small module to a markdown processing filter into
your flask.

Links
`````

* `documentation <http://packages.python.org/Flask-Markdown>`_

"""
from setuptools import setup


setup(
    name='Flask-Markdown',
    version='1.0.0',
    url='http://github.com/sopoforic/flask-markdown',
    license='BSD',
    author='Dan Colish, Tracy Poff',
    author_email='dcolish@gmail.com, tracy.poff@gmail.com',
    description='Small extension to make using markdown easy',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'markdown',
        ],
    test_suite="nose.collector",
    tests_require=[
        'nose',
        ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
)
