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
