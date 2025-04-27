class Produto:
    def __init__(self, nome, peso, valor, codigo):
        self.nome = nome
        self.peso = peso
        self.valor = valor
        self.codigo = codigo

    def atualizar_valor(self, novo_valor):
        self.valor = novo_valor

    def verificar_estoque(self):
        print("verificar_estoque")

    def consultar_codigo(self):
        print(f"Código do produto: {self.codigo}")
