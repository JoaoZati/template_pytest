import pytest as pytest

from template_pytest.spam.db import Conexao


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
