Running Locally 

Clone the repository:

git clone https://github.com/akagi128/django-url-shortener.git
cd django-url-shortener

Create and activate a virtual environment:

python3 -m venv env
source env/bin/activate

Install Django:

pip install django

Run migrations:

python manage.py migrate

Start the development server:

python manage.py runserver 8080

Open http://127.0.0.1:8080/ in your browser.
