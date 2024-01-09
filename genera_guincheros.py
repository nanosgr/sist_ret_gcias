import mysql.connector
from typing import Annotated
from fastapi import Depends
from sqlalchemy import text, select
from sqlalchemy.orm import Session
from generate_xml import GenerateXML
from database import get_db

mydb = mysql.connector.connect(
    host="192.168.24.121",
    user="root",
    password="root",
    database="idits"
)

sqlQuery = """select qry.Nombre, qry.Cuil, convert(sum(qry.RemuneracionBruta), char) as RemuneracionBruta, convert((sum(qry.NoRemunerativo) - 30000), char) as NoRemunerativo, convert(sum(qry.SueldoBasico), char) as SueldoBasico, qry.Sexo, qry.NroDoc, qry.TipDoc   
from (select concat(se.apellido, ', ', se.nombre) as Nombre, replace(se.id, '-', '') as Cuil, 
(sr.remunerativo) as RemuneracionBruta, 
ifnull(sr.no_remunerativo, 0) as NoRemunerativo,
ifnull((select src.importe from idits.sld_recibo_concepto src where ((src.periodo = sr.periodo) and (src.empleado = sr.empleado) and (src.concepto = '10'))), 0) as SueldoBasico, 
se.sexo as Sexo, se.numero_documento as NroDoc, se.tipo_documento as TipDoc, sr.periodo as periodo, se.convenio as convenio 
from idits.sld_empleado se  
inner join idits.sld_recibo sr 
on sr.empleado = se.id 
where se.fecha_egreso is null) as qry 
where qry.periodo in ('2023_12', '2023_SAC_2_CUOTA') 
and qry.convenio = 'GUINCHEROS' 
group by qry.Nombre, qry.Cuil, qry.Sexo, qry.NroDoc, qry.TipDoc
order by 1"""

# sqlQuery = 'select * from sld_empleado'


# db = Annotated[Session, Depends(get_db)]
# sqlResult = Session.execute(db, text(sqlQuery))

empresas = 'IDITS'
interface = 'Fempinra'
periodo = '2023_12'


fileName = f'./{empresas}_{interface}_{periodo}.xml'
mycursor = mydb.cursor()

mycursor.execute(sqlQuery)

myresult = mycursor.fetchall()

arbol = GenerateXML(myresult, 'FEMPINRA')

with open(fileName, "wb") as files:
    arbol.write(files, encoding="utf-8", pretty_print=True, xml_declaration=True)

mycursor.close()