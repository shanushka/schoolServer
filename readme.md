Create Pipenv
-Command: Pipenv install requirements

To activate the environment
-pipenv shell

To check all the packages that are installed 
-pipenv graph 

The Migration Environment

To create a migration environment
-alembic init migrations

Where above, the init command was called to generate a migrations directory called alembic:

Creating directory /path/to/yourproject/alembic...done
Creating directory /path/to/yourproject/alembic/versions...done
Generating /path/to/yourproject/alembic.ini...done
Generating /path/to/yourproject/alembic/env.py...done
Generating /path/to/yourproject/alembic/README...done
Generating /path/to/yourproject/alembic/script.py.mako...done
Please edit configuration/connection/logging settings in
'/path/to/yourproject/alembic.ini' before proceeding.

Alembic also includes other environment templates. These can be listed out using the list_templates command:

- alembic list_templates

Create a Migration Script  

- alembic revision -m "create account table"
