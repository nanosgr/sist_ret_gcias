from analisis_facturas import analisis_facturacion

if __name__ == "__main__":
    desde = '2023-10-01'
    hasta = '2023-10-31'
    archivo = '/home/sebastian/Documentos/win_files/Estudio/MendozaBalloons/pasajeros Oct2023.xlsx'

    analisis_facturacion(desde, hasta, archivo)