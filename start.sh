export SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://billy:pass12@localhost/pitches'
export FLASK_APP=run.py
export FLASK_ENV=development
export SECRET_KEY="d\x12S\xbe\xd1\x04\x9d\xf7\xc3\xf0@\xbcM|\x"
# flask run
python3 manage.py shell
# python3 manage.py server