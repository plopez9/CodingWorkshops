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


### Django
Django is a full web framework capable of handling both back and front end portions of a web app. The Django team has created great resources to make setting up a Django app quick and easy. It is highly recommended to use the Django polls tutorial to help you through this challenge (https://docs.djangoproject.com/en/2.2/intro/tutorial01/). This would be a great use of your second computer! The second portion utilizes the Djano Rest framework in the installed apps portion of your settings.py file.  

### Setup your environment
For this portion of the project, it might help to use someone's computer that already has the projects prerequisites installed. Environments can be tricky especially when dealing with multiple versions of the same packages. Whether you are working with someone else environmental manager or your own, here is what you will need.    

- A package manager such as pip. While pip is the standard that comes with downloaded Python versions, make sure that you at least have some sort of installation manager. A link to the pip documentation can be seen below.

		https://pip.pypa.io/en/stable/installing/

- As mentioned previously, virtual environments can be very useful in keeping your main environments light. A large problem with not using virtual environments is the use of conflicting versions of individual packages. By using a virtual environment you can guarantee a stable platform that has been vetted for this particular challenge. Documentation for creating a virtual environment, using pip, can be seen below.

    https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

- The minimum required packages as stated in the requirements.txt file. Feel free to add useful packages, such as Beautiful Soup, Requests, ect., if you are creating your own databases. This can be done by running the following command in the projects Roote directory.

    pip install -r requirements.txt

- After stepping into your newly created environment, running the command below will list your

  pip list

### Create a Django app
- Enter the directory you wish to create your Django app. Starting your app can be as simple as running a single command. The folks at Django has already created the architecture you will be using for your future Webapp. Follow the tutorial instructions in the Django documentation (lised below) up until the Creating the Polls app section.

  https://docs.djangoproject.com/en/2.2/intro/tutorial01/

- If you see the congratulations page on your local port http://127.0.0.1:8000/, you will know you installed things correctly.

### Create Your First App

- In the Django tutorial, follow the instructions to run the startapp script in the Creating the Polls App section. Please don't call your app Polls or advance further in the Django tutorial. If done correctly, you should see the addition of your app directory inside your project. Take a second to thumb through the newly created .py files, as we will be using them later.

  https://docs.djangoproject.com/en/2.2/intro/tutorial01/

- In order for Django to recognize your created app, you must first register it in your settings.py file. This can be found in the documentation below. In depth documentation on how to configure and install your app can be seen in the "Projects and applications" and "For application users" section in the documentation.

	https://docs.djangoproject.com/en/2.2/ref/applications/

### Find a Database
- Before advancing, find a database (you can also make your own!) that you wish to use for your REST api. It helps if the data is something you are interested in. Kaggle is a great resource to find databases publicly available. If you are looking for something specific, Google has a stellar database search feature.

  https://www.kaggle.com/datasets

  https://toolbox.google.com/datasetsearch

- The database you just created will eventually replace the db.sqlite3 file in your projects directory. Make sure you update the NAME parameter in the DATABASES section of your settings.py file. The startproject script creates your app preconfigured to handle a SQLite database. To run PostgreSQL, or any other of the pre-approved database options, refer to the documentation below.

  https://docs.djangoproject.com/en/2.2/ref/databases/

### Create Models
- Once your database has been stored and your settings.py file is updated, migrate your table using the command below.

	python manage.py migrate

- In your models.py file, located in your app folder, you will update class fields for each of your database tables. Django makes you explicitly characterize your database into classes (tables) and class fields (features) for each feature in your created database. There is a way for Django to "guess" and do this for you automatically. However, for the sake of this project we will avoid using it. The link to creating a model can be seen below, in the Django documentation, in the Models section. Don't worry about activating the model for now. Similarly, the documentation on how to appropriately designate character fields is listed second. If you really want to get fancy, try making your tables into a relational database by linking your fields together. The documentation to do this is in the third link under the Relationships section.

	https://docs.djangoproject.com/en/2.2/intro/tutorial02/

 	https://docs.djangoproject.com/en/2.2/ref/models/fields/

	https://docs.djangoproject.com/en/2.2/topics/db/models/#automatic-primary-key-fields

- Once your models have been constructed run the makemigrations command. Then commit them with the migrate command.

	python manage.py makemigrations [APP NAME]

	python manage.py migrate

### Installing the REST framework
- Install django REST framework using pip install. Note: if you used the requiremnts.txt django REST framework has already been installed for you.

	pip install djangorestframework

- With the rest framework installed, you will need to update your settings.py INSTALLED_APPS section and main project URLS. Django REST framework's documentation outlines this well in the Installation section. When designating a file path for your API, try to be strategic on how your user will interact with it. Aka you would not want it to be the main page or the root file path. An example of an appropriate path has been illustrated below.  

	https://www.django-rest-framework.org/#installation

	path("[AppName]/", include("[appName].urls")),

### Serialization
- Before creating a url or view for our REST framework, we must first serialize our data. This allows Django to render our data into a json format. To do this create a serializers.py file in your app directory and follow the ModelSerializer section in the Django REST documentation. Make sure you designate the table (model) and fields (features) you wish to include in your REST API.

	https://www.django-rest-framework.org/api-guide/serializers/#modelserializer

- If you do not want users to have the ability to alter your models, make sure to designate read_only_fields. This is documented in the Specifying read only fields section.

	https://www.django-rest-framework.org/api-guide/serializers/#specifying-read-only-fields

### Create a View
- Django REST framework already has built in views to interact with your API. This can be in either pure json or an actual interactive page. The views.py file is how you indicate to your app what you want to display in the browser. An example of the class based views is in the Django REST framework tutorial. Keep in mind that the django.contrib.auth.models and tutorial.quickstart.serializers are simply your models and serializers. Instead they can be expressed as shown below. The brackets are simply place holders for the descriptions inside of them.

	https://www.django-rest-framework.org/tutorial/quickstart/#views

	from .models import [Class Model 1], [Class Model 2], [ect.]
	from .serializers import [Class Serializer 1], [Class Serializer 2], [ect.]

- We can also make our framework queryable by augmenting our queryset. To do this lets make a get_queryset function that will augment the queryset variable. Under your View class pass the following function.

	def get_queryset(self):
		queryset = [Class Model 1].objects.all()

		[feature] = self.request.query_params.get(["[feature]", None])
		### repeat this for as many features you want queryable

		if [feature] is not None:
			queryset = queryset.filter([feature] = [feature])

		### repeat this for the remaining features

		return queryset

### Designating a URL
- Finally the url pages will designate where in the browser your pages can be found. It is important to note that there will be two urls.py pages. The first is imbedded in your second project folder (where your settings.py file should be). In this file there will already be some code written. We will simply add our path under the admin pathway. This code registers the app urls to be recognized by the Django project.

	urlpatterns = [
			path("", include("[App Folder].urls")),
			path('admin/', admin.site.urls),
	]

- The second urls.py file is located in your app directory. This handles the urls for the localized app. The documentation in Django REST frameworks illustrates how to create a default routing scheme.

	https://www.django-rest-framework.org/tutorial/quickstart/#urls

### Running your Server
- At this point it is time to test your API. This can be accomplished by the manage.py runserver command. The default location for your project is localhost:8000/. From there follow the naming scheme you created in your urls. Feel free to play with your API by using those filterable features you created.

 	python manage.py runserver
