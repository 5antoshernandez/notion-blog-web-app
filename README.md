# notion-blog-web-app
A simple and customizable blog that is powered by a Notion database.

# Setup
Install dependencies in marketing/requirements.txt

Run python3 manage.py makemigrations & python3 manage.py migrate.

you need to create a secret_key and put it in the marketing/settings.py .

then in home/views.py -> you need to add your notion bearer token and your database URL to replace mine

Once completed, review home/templates/home HTML files to customize your template styling and naming.

That's it!
