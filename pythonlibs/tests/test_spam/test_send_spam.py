import pytest
from pythonlibs.spam.send_email import send_email, InvalidEmail


def test_create_send_email():
    send = send_email()
    assert send is not None


def test_destinaario():
    send = send_email()
    result = send.send(
        'michel@dbqp.com.br',
        'carol@dbqp.com.br',
        'Curso de python',
        'Primeira turma aberta.'
    )
    assert 'carol@dbqp.com.br' in result


@pytest.mark.parametrize(
    'destinatarios',
    ['diana@dbqp.com.br', 'carol@dbqp.com.br']
)
def test_varios_destinatarios(destinatarios):
    send = send_email()
    result = send.send(
        'michel@dbqp.com.br',
        destinatarios,
        'Curso de python',
        'Primeira turma aberta.'
    )
    assert destinatarios in result


@pytest.mark.parametrize(
    'destinatarios',
    ['', 'carol.com.br']
)
def test__destinatarios_invalidos(destinatarios):
    send = send_email()
    # gerenciador de contexto
    with pytest.raises(InvalidEmail):
        send.send(
            'michel@dbqp.com.br',
            destinatarios,
            'Curso de python',
            'Primeira turma aberta.'
        )
