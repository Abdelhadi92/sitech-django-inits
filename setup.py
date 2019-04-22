import setuptools

version = '0.1'

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='django-inits',
     version=version,
     scripts=['django-inits'],
     packages=setuptools.find_packages(),
     author="Abdelhadi Abu-Shamleh",
     author_email="a.abushamleh@sit-mena.com",
     description="Environment tools for Django, used to set configuration depending on the server environment.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/Abdelhadi92/django-inits",
     keywords=['django', 'environments', 'django-inits' 'settings'],
     classifiers=[
         'Environment :: Web Environment',
         'Framework :: Django',
         'License :: OSI Approved :: BSD License',
         'Operating System :: OS Independent',
         'Development Status :: 5 - Production/Stable',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2',
         'Programming Language :: Python :: 2.7',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.4',
         'Programming Language :: Python :: 3.5',
         'Programming Language :: Python :: 3.6',
         'Programming Language :: Python :: 3.7',
     ],
)