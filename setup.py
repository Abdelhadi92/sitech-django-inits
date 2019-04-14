import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='django-init',
     version='0.1',
     scripts=['django-init'],
     packages=setuptools.find_packages(),
     author="Abdelhadi Abu-Shamleh",
     author_email="abushamleh92@gmail.com",
     description="Environment tools for Django, used to set configuration depending on the server environment.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/Abdelhadi92/django-init",
     keywords=['django', 'environments', 'django-init' 'settings', 'Abdelhadi Abu-Shamleh'],
     python_requires='!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
     classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules'
     ],
)