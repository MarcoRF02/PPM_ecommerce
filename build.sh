python -m pip install -r requirements.txt

# Run database migrations
python manage.py makemigrations --noinput
python manage.py migrate --noinput

python manage.py collectstatic --noinput --clear