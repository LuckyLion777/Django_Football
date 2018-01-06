# Setup
## Install Mezzanine

    $ pip install mezzanine


## Setup the postgres db 

Adpated from http://www.rosslaird.com/blog/building-a-project-with-mezzanine/

###  Install the necessary components

        $ sudo apt-get install postgresql postgresql-client libpq-dev

###  Run the database, modify password

        $ sudo -u postgres psql postgres
        postgres=# \password postgres 

###  Create new user and db for user

        $ sudo -u postgres createuser --superuser $USER
        $ sudo -u postgres psql 
        postgres=# \password [enter your username] 
        $ createdb $USER
        $ createdb football-data

###  Important Postgres commands

        $ pg_dump -Fc dbname > db.dump 
        $ createdb newdb #must be a new name 
        $ pg_restore -d newdb db.dump
        $ dropdb olddb

## Setup code path

When deploying via git, fabric expects the code to reside in a "bare" repo under
/home/<user>git/<project>.git

        $ mkdir -R ~/git && cd ~/git
        $ git clone <repo> # change name if necessary

## Setup virtual environment

        $ virtualenv --no-site-packages football-data

## Setup football-data

###  Create a database

        $ python manage.py createdb

### Fill in `SECRET_KEY` and `NEVERCACHE_KEY` in local_settings.py

###  Run the web server

        $ python manage.py runserver

### Create the homepage
1. Log into the admin
2. Go to Content -> Pages
3. Click the top "Add ..." dropdown and choose "Home page"
4. Fill out content
5. Add images for intro slideshow
6. "Breakout content" is the main part of the site, and the button will appear
at the bottom
7. Before saving click the "Meta data" section and set the url to /
8. Save

### Add other pages, such as "Contact", "Privacy Policy", "T&Cs", 
1. Log into admin panel -> "Pages"
2. Click Add -> "Rich text page"
3. Add the content
4. Be sure to mention the applicable menus it should appear in
5. Optionally, specify a URL

### Add other pages, such as "Contact", "Privacy Policy", "T&Cs", 

### Setup the article tags
1. Tags need to be made from Admin panel -> Blog posts -> New blog post
2. Create the "news" tag for general news, accessible from the top of the site
and the left side-bar
3. Create the "game-mode" tag for game mode articles, accessible when logged in

### Adding news / gamemode content
* Use the admin panel, select "Add Blog post"
* Give the article a name, and be sure to appropriately tag it as "news" or
"game-mode" so it shows up in the proper place
* When adding videos, be sure to use the "Embed" iframe availabe from Youtube or
other providers, e.g. "
<iframe width="560" height="315" src="https://www.youtube.com/embed/IoXX6BWAR1g" frameborder="0" allowfullscreen></iframe>"

### Setup the menus
* 3 different menus exist in the application
* Top menu: "News", "Contact", "Register" / "Login" ("Logout")
* Side menu when logged in: "Edit Profile", "Connections", "News", "Game Mode", 
"Vuvuzela", "Fanzone", "Jobs"
* Bottom menu: "News", "Contact", "Register" / "Login", "Privacy Policy", 
"Terms & Conditions"
