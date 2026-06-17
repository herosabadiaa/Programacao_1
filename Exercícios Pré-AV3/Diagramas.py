from datetime import *
#Diagrama 1
class Veiculo:
    def __init__(self, placa, ano):
        self.placa = placa
        self.ano = ano
class Moto(Veiculo):
    def __init__(self, placa, ano):
        super().__init__(placa, ano)
class Caminhao(Veiculo):
    def __init__(self, peso_kg, placa, ano):
        self.peso_kg = peso_kg
        super().__init__(placa, ano)

cm1 = Caminhao(12, "2SAK1", 2023)
print(cm1.peso_kg)
#Diagrama 2 - Nada Prático
class Cliente2:
    def __init__(self, nome, data_nascimento, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Prato2:
    def __init__(self, nome, ingredientes, modo_preparo, preco):
        self.nome = nome
        self.ingredientes = ingredientes
        self.modo_preparo = modo_preparo
        self.preco = preco

class Pedido2:
    def __init__(self, data_pedido, desconto, cliente, pratos, valor_total):
        self.data_pedido = data_pedido
        self.desconto = desconto
        self.cliente = cliente
        self.pratos = pratos
        self.valor_total = valor_total

c1_2 = Cliente2("Joao", date(1980, 12, 3), "219234710")
p1_2 = Prato2("Teste", ["I1", "I2", "I3"], "teste", 100)
p2_2 = Prato2("Teste", ["I1", "I2", "I3"], "teste", 200)
pedido1_lista = [p1_2,p2_2]
vt1 = 0
desconto1 = 15/100
for i in pedido1_lista:
    vt1 += i.preco
vt1 -= vt1*desconto1
pedido1_2 = Pedido2(date(2026,6,17), desconto1 , c1_2, pedido1_lista, vt1)
print(pedido1_2.valor_total)



#Diagrama 3

class Cliente3:
    def __init__(self, nome, data_nascimento, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Prato3:
    def __init__(self, nome, ingredientes, modo_preparo, preco):
        self.nome = nome
        self.ingredientes = ingredientes
        self.modo_preparo = modo_preparo
        self.preco = preco

class ItemDoPedido3:
    def __init__(self, prato, quantidade):
        self.prato = prato
        self.quantidade = quantidade
        self.valor_prato = prato.preco

class Pedido3:
    def __init__(self, data_pedido, desconto, cliente, itens):
        self.data_pedido = data_pedido
        self.desconto = desconto
        self.cliente = cliente
        self.itens = itens
    
    def valor_total(self):
        valor_total = 0
        for i in self.itens:
            valor_total += i.valor_prato * i.quantidade
        valor_total -= valor_total*self.desconto
        return valor_total
    
c1 = Cliente3("Joao", date(1980, 12, 3), "219234710")
p1 = Prato3("Teste", ["I1", "I2", "I3"], "teste", 100)
p2 = Prato3("Teste", ["I1", "I2", "I4"], "teste", 50)
idp1 = ItemDoPedido3(p1, 1)
idp2 = ItemDoPedido3(p2, 3)
pedido1 = Pedido3(date(2026,6,17), 15/100, c1, [idp1, idp2])

print(pedido1.valor_total())