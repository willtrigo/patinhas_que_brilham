# Patinhas que brilham

Website for a ONG of pets.

## How to develop?

1. Clone the repository
2. Create a virtualenv with Python 3.7
3. Active the virtualenv
4. Install the requirements
5. Set one instance with the .env
6. Run the collectstatic
7. Run the tests

```console
git clone https://github.com/willtrigo/patinhas_que_brilham.git patinhas_que_brilham
cd patinhas_que_brilham
python3.7 -m venv .patinhas_que_brilham
source .patinhas_que_brilham/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py collectstatic
python manage.py test
```

## How to do the deploy?

1. Set a instant in the heroku
2. Send the configurations to the heroku
3. Set a SECRET_KET safety key for the instance
4. Set DEGUB=False
5. Send the code to heroku

```console
heroku create myinstant
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=False
git push heroku master --force
```
