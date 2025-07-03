class Pagamento:
    def __init__(self, forma_de_pagamento, nota_fiscal, valor, status):
        self.forma_de_pagamento = forma_de_pagamento
        self.nota_fiscal = nota_fiscal
        self.valor = valor
        self.status = status

    def realizar_pagamento(self):
        pass

    def emitir_nota_fiscal(self):
        pass
