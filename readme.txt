HervM/Shaheq Shakeel

__MACOS SETTING_UP_WEBSERVICES __
To run web server on Mac Os you will need virtual environment for python (venvosx):
from root project directory (aka ./yxefoodbank) in terminal write
    mkdir venvosx  
    cd venvosx 
    virtualenv -p python3 .    
    source ./bin/activate
    cd ..    
    python manage.py runserver

To get out of virtual environment:
from terminal write
    CTRL+C
    deactivate

On next launch you only need to use commands:
    source ./bin/activate
    cd ..    
    pip3 install -r requirements.txt
    python manage.py runserver

__WINDOWS SETTING_UP_WEBSERVICES__ (as shown in video)
> ctrl+~ (to go into terminal for visual studio code)
> switch to cmd
Run this line of code into the cmd into the CMD 
venv\Scripts\activate
pip install -r requirements.txt
pip install pillow 
pip install stripe
manage.py runserver


__WEB_BROWSER__
website runs at default 127.0.0.1:8000/

__DIR__
./templates holds all our files that each page on our website uses
./base/templates holds all our pages that are not associated with account management
./account/templates currently only hold register.html page

__CREATING NEW APP__
How to create a new app from root directory
python manage.py startapp store


__PASSING CHANGES TO THE DATABASE__
python manage.py makemigrations
python manage.py migrate       
