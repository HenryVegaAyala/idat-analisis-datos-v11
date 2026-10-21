class Cliente:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def comprar(self, monto):
        if self.saldo >= monto:
            self.saldo = self.saldo - monto
            print(f"Compra realizada por de manera exitosa. Saldo restante: {self.saldo}")
        else:
            print("Saldo insuficiente para realizar la compra.")

cliente = Cliente("Luis", 1000)
print(f"Saldo inicial {cliente.saldo}")
cliente.comprar(300) # Esta accion está comprando una zapatilla
print(f"Saldo actual {cliente.saldo}")