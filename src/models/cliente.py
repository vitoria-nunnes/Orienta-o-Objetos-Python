class Cliente:
    def __init__(self, nome, cpf, endereco, telefone):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

    def atualizar_cadastro(self, novo_nome, novo_cpf, novo_endereco, novo_telefone):
        self.nome = novo_nome
        self.cpf = novo_cpf
        self.endereco = novo_endereco
        self.telefone = novo_telefone
