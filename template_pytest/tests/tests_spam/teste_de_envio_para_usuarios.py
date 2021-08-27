from unittest.mock import Mock

import pytest as pytest

from template_pytest.spam.enviador_de_emails import Enviador
from template_pytest.spam.main import EnviadorDeSpam
from template_pytest.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [    [
            Usuario(nome='Renzo', email='renzo@python.pro.br'),
            Usuario(nome='Luciano', email='luciano@python.pro.br')
         ],
         [
            Usuario(nome='Renzo', email='renzo@python.pro.br')
         ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('joaozati@gmail.com',
                                   'Curso Python Pro',
                                   'Confira os módulos fantásticos')
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Renzo', email='renzo@python.pro.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('joaozati@gmail.com',
                                   'Curso Python Pro',
                                   'Confira os módulos fantásticos')
    assert enviador.enviar.assert_called_once_with(
        'joaozati@gmail.com'
        'renzo@python.pro.br'
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
