SECRET_KEY = 'pudim'
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
SGBD = 'mysql+mysqlconnector',
usuario = 'root',
senha = 'ifsp',
servidor = 'localhost',
database = 'pypo'
)