# My first Website developed in Django

Flask is more of what we call a "micro" web framework. It is much "lower level" than Django is. This allows for more customization and control for the developer.

Django is much more of a higher-level framework, and imposes a set structure on the developer.

Thus, with Flask you can create systems your way, which is probably not most efficient, fastest, or secure way. With Django, you are a bit more constrained, but you are going to most likely do it the best way possible. As with almost all questions people ask me regarding which to use, the answer is: Try a few, and choose the one you like best. In the end, Django and Flask can be used to make the exact same websites!

### System spec:
- Django version: 2.2
- Python version: 3.7

### Based on:
https://www.youtube.com/watch?v=FNQxxpM1yOs&list=PLQVvvaa0QuDeA05ZouE4OzDYLHY-XH-Nd

## How to install Django (Windows and Linux):
[Documentation](https://docs.djangoproject.com/en/2.2/topics/install/)

### How to install Django on Windows:

- To install Python on your machine go to https://python.org/downloads/. The website should offer you a download button for the latest Python version. Download the executable installer and run it. Check the box next to Add Python 3.x to PATH and then click Install Now.
- After installation, open the command prompt and check that the Python version matches the version you installed by executing:
```bash
python --version
```
- pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org. Just make sure to upgrade pip:
```bash
python -m pip install -U pip
```
- Install virtualenv and virtualenvwrapper. virtualenv and virtualenvwrapper provide a dedicated environment for each Django project you create. While not mandatory, this is considered a best practice and will save you time in the future when you’re ready to deploy your project. 
Navigate to project directory and simply type:
```bash
pip install virtualenvwrapper-win
```
- Then create a virtual environment for your project:
```bash
pip install virtualenv
```
- Install Django. Django can be installed easily using pip within your virtual environment. 
In the command prompt, ensure your virtual environment is active, and execute the following command:
```bash
pip install django
```
- After the installation has completed, you can verify your Django installation by executing following command in the command prompt:
```bash
django-admin --version
```

## Creating a project:
- From the command line, cd into a directory where you’d like to store your code, then run the following command:
```bash
django-admin startproject mysite
```
- This will create a mysite directory in your current directory. If it didn’t work, see [Problems running django-admin.](https://docs.djangoproject.com/en/2.2/faq/troubleshooting/#troubleshooting-django-admin)
- Let’s look at what startproject created:
```bash
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```
**These files are:**

- The outer **mysite/** root directory is just a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
- **manage.py**: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in [django-admin and manage.py.](https://docs.djangoproject.com/en/2.2/ref/django-admin/)
- The inner **mysite/** directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).
- **mysite/__init__.py**: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read [more about packages](https://docs.python.org/3/tutorial/modules.html#tut-packages) in the official Python docs.
- **mysite/settings.py**: Settings/configuration for this Django project. [Django settings](https://docs.djangoproject.com/en/2.2/topics/settings/) will tell you all about how settings work.
- **mysite/urls.py**: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in [URL dispatcher.](https://docs.djangoproject.com/en/2.2/topics/http/urls/)
- **mysite/wsgi.py**: An entry-point for WSGI-compatible web servers to serve your project. See [How to deploy with WSGI](https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/) for more details.

### The development server:
Let’s verify your Django project works. Change into the outer mysite directory, if you haven’t already, and run the following commands:
```bash
python manage.py runserver
```
You’ll see the following output on the command line:
```bash
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

July 02, 2019 - 15:50:53
Django version 2.2, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

