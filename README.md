For this project, we will be creating a functioning REST API. REST APIs can help distribute useful information via GET requests, as well as post and alter databases in a user friendly fashion. An example project will be uploaded after the completion of the Project Night.

### The project
This project will revolve around Django and Django's rest framework. The goal of which is to create a working REST API. If you feel more comfortable with flask, feel free to trail off the beaten path to create one! Before starting, make sure to look over the requirements file and install any necessary packages. To avoid bloating of your primary working environment, you might find it useful to create a virtual environment. The requirements.txt file will have the working package versions at the time of creation.

### Is this project for you
Before you progress further, let's check if we are ready to solve this. You should
- Have a personal computer with working wifi and power cord
- Have Python 3.7 installed on your computer.
- Have [Atom](https://atom.io/) or [Sublime Text](https://www.sublimetext.com/3) installed in your computer.
- Have written & ran programs in Python from the command line
- Have some idea about lists, dictionaries and functions
- Have created a virtual environment and installing packages with `pip`

### What is not supported
This project is not tested using Jupyter Notebook, PyCharm,
Spider, or any other ide/text editor/programming environment.

### Useful Weblinks
The weblinks below can aid you as you work your way through this challenge.

- Virtual Environments & Installation

	https://pip.pypa.io/en/stable/installing/

	https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

- Database Resources

	https://www.kaggle.com/datasets

	https://toolbox.google.com/datasetsearch

	https://docs.djangoproject.com/en/2.2/ref/databases/

- Django Startup and Features

	https://docs.djangoproject.com/en/2.2/intro/tutorial01/

	https://docs.djangoproject.com/en/2.2/ref/applications/

- Django Models

	https://docs.djangoproject.com/en/2.2/ref/models/fields/

	https://docs.djangoproject.com/en/2.2/topics/db/models/#automatic-primary-key-fields

- Django REST Framework

	https://www.django-rest-framework.org/#installation

- Serialization

	https://www.django-rest-framework.org/api-guide/serializers/#modelserializer

	https://www.django-rest-framework.org/api-guide/serializers/#specifying-read-only-fields

- Views and URLS

	https://www.django-rest-framework.org/tutorial/quickstart/#views

	https://www.django-rest-framework.org/tutorial/quickstart/#urls

### Django
Django is a full web framework capable of handling both back and front end portions of a web app. The Django team has created great resources to make setting up a Django app quick and easy. It is highly recommended to use the Django polls tutorial to help you through this challenge (https://docs.djangoproject.com/en/2.2/intro/tutorial01/). This would be a great use of your second computer! The second portion utilizes the Django REST framework.  

### Setup your environment
For this portion of the project, it might help to use someone's computer that already has the projects prerequisites installed. Whether you are working with someone else's environmental manager or your own, here is what you will need.    

- A package manager such as pip. While pip is the standard that comes with downloaded Python versions, make sure that you at least have some sort of installation manager.

- The minimum required packages as stated in the requirements.txt file. Feel free to add useful packages, such as Beautiful Soup, Requests, ect., if you are creating your own databases.

### Find a Database
- Before advancing, find a database (you can also make your own!) that you wish to use for a REST API. It helps if the data is something you are interested in. Kaggle is a great resource to find databases publicly available. If you are looking for something specific, Google has a stellar database search feature.

### Create Your First App

- Create a Django app in a local directory of your choosing. Feel free to use the Django tutorial to accomplish this, but please don't call your app the standard Polls App. Create a unique application inside of your Django directory to handle your database and models. Make sure the application is configured in your settings.py file!

### Create a Django Model
- Create a Django model custom to your created or downloaded database. Feel free to take liberties like creating relational databases for your models. The model field types should match the intended fields of your database. Make sure to migrate your Django model when you are finished!

### Installing the REST framework
- If you have not used the requirements.txt file, install djangorestframework. Make sure you appropriately configure Django REST Framework in your settings.py file, not doing so will not allow Django to recognize the add on.

### Serialization
- Before creating a url or view, serialize your data. This allows Django to render data into a JSON format. Make sure you designate the table (model) and fields (features) you wish to include in your REST API.

### Create a View
- Use the standard Django REST framework to create your Django view. Django REST framework allows you to interact with your API in both JSON and a preset interactive template. If you feel like going the extra mile, make your database queryable to gather the information you need.

### Designating a URL
- Finally, designate url addresses where your page views can be found. Make sure to create a URL scheme that makes sense to how the intended user will interact with your API.

### Running your Server
- At this point it is time to test your API. This can be accomplished by the manage.py runserver command. Django's default location is localhost:8000/. From there, follow the naming scheme you created in your urls. Feel free to play with your API by using those filterable features you created!
