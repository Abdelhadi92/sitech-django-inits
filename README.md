# Django Initialization Tool
Environment tools for Django, used to set configuration depending on the server environment.

## Installation
 Run the [pip](https://pip.pypa.io/en/stable/) command to install the latest version:
 
```bash
  pip install git+https://github.com/sitmena/sitech-django-inits.git
```

## Usage

 - Go to the root of your project and create new directory called "__environments__".
 
 - In "__environments__" directory  create new file called "**\_\_init\_\_.py**".

 - In the  "**\_\_init\_\_.py**" define the details of your environments in "**ENVIRONMENTS**" dictionary.
 - Define the settings files 


<br />
environments/__init__.py

```bash
ENVIRONMENTS = {  
    'Development': {  
	    'path': 'dev',  
	},  
	'Production': {  
		'path': 'prod',  
	},  
}
```

<br />
environments/dev/settings_local.py

```bash
DEBUG = True

DATABASES = {  
	'default': {  
      'ENGINE': 'django.db.backends.mysql',  
	  'NAME': 'example',  
	  'USER': 'root',  
	  'PASSWORD': 'root',  
	  'HOST': '127.0.0.1',  
	  'PORT': '3306',  
  }  
}
```

<br />
environments/prod/settings_local.py

```bash
DEBUG = False

DATABASES = {  
	'default': {  
      'ENGINE': 'django.db.backends.mysql',  
	  'NAME': 'example',  
	  'USER': 'user1#$%^%',  
	  'PASSWORD': '%$%23118',  
	  'HOST': '54.1.4.62',  
	  'PORT': '3306',  
  }  
}
```
- Go to terminal and run the following command:

    
```bash
 django-inits
```

## Commands

```bash
 django-inits
```

```bash
 django-inits --env=[Development] --overwrite=[no,yes,all]
```

    

