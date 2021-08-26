import pytest as pytest
from template_pytest.spam.enviador_de_emails import Enviador, EmailInvalido



def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'renzo@python.pro.br'])
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(destinatario,

                    'joaoribeiro@alunos.utfpr.edu.br',
                    'Cursos Python Pro',
                    'Turma do Iury')


    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['', 'renzopython'])
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(destinatario,
                        'joaoribeiro@alunos.utfpr.edu.br',
                        'Cursos Python Pro',
                        'Turma do Iury')
#teste é executado em todos os parametros

