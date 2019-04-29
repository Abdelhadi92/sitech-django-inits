# Django Initialization Tool
Environment tools for Django, used to set configuration depending on the server environment.

## Installation
 Run the [pip](https://pip.pypa.io/en/stable/) command to install the latest version:
 
```bash
  pip install git+https://github.com/sitmena/sitech-django-inits.git
```

## Usage

 - Go to the root of your project and create new directory called "__environments__".
 
 - In "__environments_" directory  create new file called "**\_\_init\_\_.py**".

 - In the  "**\_\_init\_\_.py**" define the details of your environments in "**ENVIRONMENTS**" dictionary.
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

## Commands

```bash
 django-inits
```

```bash
 django-inits --env=[Development] --overwrite=[no,yes,all]
```

    

