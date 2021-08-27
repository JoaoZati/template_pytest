from template_pytest.spam.modelos import Usuario


def teste_salvar_usuario(sessao):
    usuario = Usuario(nome='Joao', email='joaozati@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def teste_listar_usuario(sessao):
    usuarios = [Usuario(nome='Renzo', email='renzo@python.pro.br'),
                Usuario(nome='Luciano', email='luciano@python.pro.br')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
