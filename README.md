## project structure/django review
- models.py defines all the object types that the database stores
- urls.py has all the urls the django webapp responds to
    - can place an integer instead of '<int:pk>' to look at specific items in the database
- views.py is all the python logic for storing data in the database, serving it, etc.
- views.py utilizes all the html in the templates folder to display information to and interact with the user
    - 'task.html' has the javascript that runs the 
- forms.py creates form templates for the views to use

## running the project
- I'd recommend creating a virtual environment to handle all the requirements
- 'python3 manage.py runserver'
    - needs a lot of requirements but python should figure out what is needed to run it
        - some requirements are in requirements.txt and requirements3.txt but a lot of those are probably unneeded 
- now the server should be running on local host and serving it's urls

## urls of note/usage of web app
- the homepage (127.0.0.1:8000 on local host) is a login page for the user
- to generate users got to /massusers and enter the amount of users to create
    - of this number 1/2 will be tested on females, 1/2 males, 1/2 ascending pictures, 1/2 descending pictures
- go to /viewallusersforadmin to get the login info on these users so participants can log in
- once a user is logged in they can go to /task to start their 3 tasks, however first we need to upload pictures to the database
- to upload pictures use the uploadFiles.py script
    - open the script and enter the file path on the computer to the MorpphingSequences
    - for example ..../MorphingSequences
    - inside MorphingSequences there should be folders of the naming convention AF_203 for example where the 2nd letter denotes sex of the subject
    - in a production scenario one must also change the url
    - you can go to /image/1 to see if images were uploaded correctly, and just change the number 1 to for example 100 to see the 100th image in the database
        - each image should belong to it's correct folder
- now that the images are uploaded a user can go to /task and complete a task
    - once they complete 3 tasks they are done
- go to /alltasks to get the results of all the tasks in csv format :)

## resetting the webapp
- the database is running the django sqlite3 database so you would probably delete project.sqlite3

## for production
- make sure to change the secret in settings.py 

## going forward
- the consent page has wrong text and doesn't redirect to the task for the user
