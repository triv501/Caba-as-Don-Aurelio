# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from cliente.py")

def nuevo():
    formulario = SQLFORM(db.cliente)
    if formulario.process().accepted:
        response.flash = 'Ok!!'
    elif formulario.errors:
        response.flash = 'Tienes errores en los datos'
    else:
        response.flash = 'Por fabor llena los datos del cliente'
    return dict(Nuevo_cliente = formulario)

def ver_clientes():
    grid = SQLFORM.grid(db.cliente)
    return dict(grid=grid)
