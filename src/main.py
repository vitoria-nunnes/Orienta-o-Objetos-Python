from datetime import datetime

from models.produto import Produto

produto = Produto(
    nome="Arroz",
    peso=1.5,
    valor=6.0,
    codigo=1,
)

print(produto.__dict__)

produto.atualizar_valor(7.0)

print(produto.__dict__)

produto.consultar_codigo()

from models.cliente import Cliente

cliente = Cliente(
    nome="Maria",
    cpf="086.038.255-99",
    endereco="Avenida Miguel Frias e Vasconcelos - 1200",
    telefone="48-99112-8819",
)

print(cliente.__dict__)

cliente.atualizar_cadastro(
    novo_nome="Fernanda",
    novo_cpf="05665013170",
    novo_endereco="Servidao Feijo Vieira - 186",
    novo_telefone="71-98627-7617",
)

print(cliente.__dict__)

from models.estoque import Estoque

estoque = Estoque(
    quantidade=500,
    validade=20,
)

print(estoque.__dict__)

from models.usuario import Usuario

usuario = Usuario(
    email="elefantinhochaw@gmail.com",
    senha="euamosuhi10",
)

print(usuario.__dict__)


from models.carrinho import Carrinho

carrinho = Carrinho(
    valor=12.99,
    quantidade=10,
)

print(carrinho.__dict__)

from models.historico import Historico

historico = Historico(
    data=datetime.now(),
    quantidade=15,
)

print(historico.__dict__)

from models.pedido import Pedido

pedido = Pedido(
    orcamento=True,  # or False
    status_entrega="Pedido em Separação",
)

print(pedido.__dict__)
