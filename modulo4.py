from principal import*
from menu import*
from modulo1 import*
from modulo2 import*
from modulo3 import*
from modulo5 import*
from modulo6 import* 
pagos=[]


def registrar_pago(cliente,monto,moneda,tipo_pago):
    pago={
        "Cliente":cliente,
        "Monto":monto,
        "Moneda":moneda,
        "Tipo de pago":tipo_pago,
        "Fecha_pago":None
    }
    pagos.append(pago)
    
def buscar_pagos(cliente=None,fecha=None,tipo_pago=None,moneda=None):
    resultados=[]
    for pago in pagos:
        if cliente and pago["Cliente"]!=cliente:
            continue
        if fecha and pago["Fecha del pago"]!=fecha:
            continue
        if tipo_pago and pago["Tipo de pago"]!=tipo_pago:
            continue
        if moneda and pago["Moneda"]!=moneda:
            continue
        resultados.append(pago)
        return resultados