import pytest as pytest
from template_pytest.spam.db import Conexao
from template_pytest.spam.modelos import Usuario


@pytest.fixture(scope='session')
def conexao():
    # setup
    conexao_obj = Conexao()
    yield conexao_obj
    # Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.fechar()
    sessao_obj.roll_back()


def teste_salvar_usuario(sessao):
    usuario = Usuario(nome='Joao')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def teste_listar_usuario(sessao):
    usuarios = [Usuario(nome='Renzo'), Usuario(nome='Luciano')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
