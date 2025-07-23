SECRET_KEY = 'pudim'
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
SGBD = 'mysql+mysqlconnector',
usuario = 'root',
senha = 'Lf132639',
servidor = 'localhost',
database = 'pypo'
)