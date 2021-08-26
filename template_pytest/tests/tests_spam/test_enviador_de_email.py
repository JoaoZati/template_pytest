from template_pytest.spam.enviador_de_emails import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar('joaozati@gmail.com',
                    'joaoribeiro@alunos.utfpr.edu.br',
                    'Cursos Python Pro',
                    'Turma do Iury')

    assert 'joaozati@gmail.com' in resultado
