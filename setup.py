from setuptools import setup, find_packages


setup(
    name='pony-express',
    version='1.0.0',
    license='MIT',
    author='Ben Lopatin, Andrew McCloud',
    author_email='ben@wellfire.co',
    url='http://github.com/bennylope/django-firstclass/',
    packages=find_packages(exclude=['tests']),
    install_requires=open('requirements.txt').readlines(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
