<h2>Running Locally </h2>

<h3><b>Clone the repository:</b></h3>

git clone https://github.com/akagi128/django-url-shortener.git

cd django-url-shortener

<h3><b>Create and activate a virtual environment:</b></h3>

python3 -m venv env

source env/bin/activate

<h3>Install Django:</h3>

pip install django

<h3>Run migrations:</h3>

python manage.py migrate

<h3><b>Start the development server:</b></h3>

python manage.py runserver 8080

Open http://127.0.0.1:8080/ in your browser.
