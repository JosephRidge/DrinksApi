# Creating your Django project
 - mkdir drink && cd drink
 - pipenv install django
 - activate python env -> `pipev shell`
 - Create django project -> ` django-admin startproject drink`
 - open terminjal and run `python manage.py runserver`
 - launch vscode (if you are usaing vscode) the  :
    *  ctrl + P ( opens a search section on vscode )
    *  search >python intepreter then select it then select '*Enter path option*'
    * on terminal window - open via vscode run `pipenv --venv` it will print out a path, copy it and paste it at the search section open on your vscode then p[ress enter/

- run `python manage.py migrate` : applies all table migrations


# Building The API 
- Install djangorestframework  : `pip install djangorestframework`

## Simple API CheckList : 
  - [x] Models
  - [x] Views ( create methods /funtions attcahed to the target HTTP CRUD verbs)
  - [x] Urls (create End points)
  - [x] Serializers
  - [x] Admin Panel Setup & Update   
  - [x] Addition of capability to attain json query using `urlpatterns = format_suffix_patterns(urlpatterns) # Allows you to query wit the .json line
`

# NOTE: 
 - The REST Architecture is used here.  