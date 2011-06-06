from setuptools import setup
from setuptools import find_packages


version = '0.1'
name='plonetheme.html5_hotpink'


setup(
    name=name, version=version,
    description="Diazo theme for Plone",
    long_description=open("README.rst").read(),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        ],
    keywords='plone diazo theme',
    author='Rok Garbas',
    author_email='rok@garbas.si',
    url='https://github.com/garbas/'+name,
    license='BSD',
    packages=find_packages(),
    namespace_packages=['plonetheme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.app.theming',
        ],
    entry_points="""
        [z3c.autoinclude.plugin]
        target = plone
        """,
    )
