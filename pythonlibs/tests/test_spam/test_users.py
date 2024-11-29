import pytest

from pythonlibs.spam.connection_db import Connection
from pythonlibs.spam.model_user import User


def test_save_user():
    # criando uma conexão:
    connection = Connection()
    # gerar uma sessão:
    session = connection.generate_session()
    # criando um usuário:
    user = User(name='michel')
    # salvando usuário
    session.save(user)
    # confere se o usuário foi salvo (deve ter um id)
    assert isinstance(user.id, int)
    # reset na sessão
    session.roll_back()
    # fechando a sessao e a conexão para liberar recursos
    session.close()
    connection.close()


def test_list_user():
    connection = Connection()
    session = connection.generate_session()
    # criando vários usuários:
    users = [User(name='michel'), User(name='carol')]
    # Salvando os usuários:
    for user in users:
        session.save(user)
    # verificando se estão em uma lista:
    assert users == session.to_list()
    session.roll_back()
    session.close()
    connection.close()


# Realizando testes com a fixture do pytest para
# evitar repetição de código:
@pytest.fixture()
# vira uma função geradora
def connection():
    # setup
    connection_obj = Connection()
    yield connection_obj
    # tear down
    connection_obj.close()


@pytest.fixture()
def session(connection):
    session_obj = connection.generate_session()
    yield session_obj
    session_obj.roll_back()
    session_obj.close()


# conexão e sessão são abertas e fechadas
# através da fixture
def test_save_user_com_fixture(session):
    user = User(name='michel')
    session.save(user)
    assert isinstance(user.id, int)


def test_list_user_com_fixture(session):
    users = [User(name='michel'), User(name='carol')]
    for user in users:
        session.save(user)
    assert users == session.to_list()
