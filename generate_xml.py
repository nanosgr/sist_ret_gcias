from lxml import etree as xml

def GenerateXML( sqlQuery:list, organismo:str ):
    # Creamos la raíz del esquema para este caso es Empleados.
    empleados = xml.Element("Empleados")
    # Creamos el tag (etiqueta) que usamos para cada uno de los empleados a ser declarados.
    # En esta parte iteramos el diccionario
    # print(organismo)
    for registro in sqlQuery:
        empleado = xml.SubElement(empleados, "Empleado")
        xml.SubElement(empleado, 'Nombre').text = registro[0] #nombre
        xml.SubElement(empleado, 'Cuil').text = registro[1] #cuil
        xml.SubElement(empleado, 'RemuneracionBruta').text = registro[2] #str(registro.TotalRemunerativo)
        xml.SubElement(empleado, 'SueldoBasico').text = registro[3] #str(round((registro.TotalNoRemunerativo - 30000), 2)) # La parte no remunerativa
        if organismo == 'FEMPINRA':
            xml.SubElement(empleado, 'AporteNoRemunerativo').text = registro[3] # str(round((float(registro.TotalNoRemunerativo - 30000) / 100), 2))
        xml.SubElement(empleado, 'Sexo').text = registro[5] #Sexo
        xml.SubElement(empleado, 'NroDoc').text = registro[6] #NroDoc
        xml.SubElement(empleado, 'TipDoc').text = registro[7] #TipDoc
        if organismo == 'FEMPINRA':
            xml.SubElement(empleado, 'Categoria').text = "1"

    tree = xml.ElementTree(empleados)

    return tree

    # with open(fileName, "wb") as files:
    #     tree.write(files, encoding="utf-8", pretty_print=True, xml_declaration=True)