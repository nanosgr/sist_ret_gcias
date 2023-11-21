from lxml import etree as xml

def GenerateXML(fileName, sqlQuery, ):
    # Creamos la raíz del esquema para este caso es Empleados.
    empleados = xml.Element("Empleados")
    # Creamos el tag (etiqueta) que usamos para cada uno de los empleados a ser declarados.
    # En esta parte iteramos el diccionario
    for registro in sqlQuery:
        empleado = xml.SubElement(empleados, "Empleado")
        xml.SubElement(empleado, 'Nombre').text = registro[0]
        xml.SubElement(empleado, 'Cuil').text = registro[1]
        xml.SubElement(empleado, 'RemuneracionBruta').text = registro[2]
        xml.SubElement(empleado, 'SueldoBasico').text = registro[3]
        # print(round((float(registro[3]) / 100), 2))
        xml.SubElement(empleado, 'AporteNoRemunerativo').text = str(round((float(registro[3]) / 100), 2))
        xml.SubElement(empleado, 'Sexo').text = registro[4]
        xml.SubElement(empleado, 'NroDoc').text = registro[5]
        xml.SubElement(empleado, 'TipDoc').text = registro[6]
        xml.SubElement(empleado, 'Categoria').text = "1"

    tree = xml.ElementTree(empleados)

    with open(fileName, "wb") as files:
        tree.write(files, encoding="utf-8", pretty_print=True, xml_declaration=True)