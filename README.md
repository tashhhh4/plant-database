# plant-database
Django Web App - Practice Project


Plant Database Practice Project
-------------------------------

We will use django to write the web app.

We will use postgres as the database.

We will use Azure blob storage for the image files.
We may also try Azure file storage as an alternative.

-----------------------------------------------------

Since I am planning on making a website at NatashaLibera.com
soon anyways, I will create subdomains off of it and deploy my
staging and production environments to them.

-----------------------------------------------------

The local development environment uses docker to host
a container to run django, a container to run postgres,
and a container to run pgadmin. We might also use a
container to run some kind of mock storage for the images.

The staging environment will be deployed to "plants-staging.natashalibera.com"

The production environment will be deployed to "plants.natashalibera.com"

We will use GitHub for the origin of the repository.

We will use GitHub actions to control the deployments.

We will use Azure to host the staging and production apps.
Like the local environment, the Azure environments need to have
something to run the app, something to run the postgres database,
and something to run the image storage. PGAdmin does not necessarily have
to be hosted on Azure, since we could just run our own PGAdmin on our
local computer, and use that to connect to our remote database for the staging
website, and our remote database for the live website.

=====================================================

The app
-------

The web app, or website, will be a list of all the
plants in the database. Each plant will have a
common English name, a latin species name, and an
image of the plant. These will be displayed in a
flex element for easy responsive scaling.

=====================================================

Running the project locally
---------------------------
* Open `docker-compose.yml` in a text editor.
* Edit the enivornment values:
  - 'POSTGRES_USER=your_admin_name'
  - 'POSTGRES_PASSWORD=secure_admin_password'
  - 'PGADMIN_DEFAULT_EMAIL=your@email.com'
  - 'PGADMIN_DEFAULT_PASSWORD=your_pgadmin_app_password'

* Open `app/config/settings.py` in a text editor.
* Edit the database connection password:
  - 'PASSWORD': 'new_secure_password',

* Be in the root folder of the repo.
* Run: `docker-compose up -d`
* Run: `docker-compose exec postgres bash`
* (postgres box) Run: `psql -U your_admin_name`
* (psql) Run: `CREATE DATABASE local_plantdb`
* (psql) Run: `CREATE ROLE djangobot WITH LOGIN PASSWORD 'new_secure_password'`
* Exit the postgres box:
            exit
            exit

* Run django migrations on the "data" app:
            docker-compose exec django python manage.py showmigrations data
            docker-compose exec django python manage.py migrate data

* View the database in PGAdmin by browsing to `localhost:5000`
* Or, use PGAdmin from any other computer on the network by browsing to
  `[computer's local ip]:5000`
* Log in to the PGAdmin interface using the email/password combination
  given to the postgres container as environment variables.
* Click on "Add New Server"
* Give the server a name.
* Go to the "Connection" tab.
            Host name/address: postgres
            Port: 5432
            Username: your_admin_name
            Password: secure_admin_password
* Click "Save".