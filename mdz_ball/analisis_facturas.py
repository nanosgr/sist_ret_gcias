import openpyxl
import os
import datetime

def analisis_facturacion(fecha_desde: datetime, fecha_hasta: datetime, nombre_archivo: str):
    print(f'Vamos a analizar desde el {fecha_desde} hasta el {fecha_hasta}')

    wb = openpyxl.load_workbook(nombre_archivo)
    wsFacturacion = wb['Facturacion']
    wsPasajeros = wb['Pasajeros']

    for i in range(2, wsFacturacion.max_row + 1):
        cbte = dict(
            comprobante=wsFacturacion.cell(column=1, row=i).value,
            cantidad_pasajeros=wsFacturacion.cell(column=7, row=i).value,
            precio_total=wsFacturacion.cell(column=8, row=i).value,
            efectivo=wsFacturacion.cell(column=9, row=i).value,
            transferencia=wsFacturacion.cell(column=10, row=i).value,
            mercado_pago=wsFacturacion.cell(column=12, row=i).value,
            px_unitario=wsFacturacion.cell(column=13, row=i).value)
        analisis_pasajeros(cbte, wsPasajeros)

    return

def analisis_pasajeros(comprobante: dict, wsPasajeros: openpyxl.worksheet):
    for i in range(2, wsPasajeros.max_row + 1):
        comprobante_pasajero = wsPasajeros.cell(column=11, row=i).value
        if not comprobante_pasajero.find(comprobante['comprobante']):
            print(f'{wsPasajeros.cell(column=5, row=i).value}')

    return
