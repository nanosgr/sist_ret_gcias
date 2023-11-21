import mysql.connector
from text_xml import GenerateXML

mydb = mysql.connector.connect(
    host="192.168.24.121",
    user="root",
    password="root",
    database="idits"
)

mycursor = mydb.cursor()

mycursor.execute("""select qry.Nombre, qry.Cuil, convert(sum(qry.RemuneracionBruta), char) as RemuneracionBruta, convert(sum(qry.SueldoBasico), char) as SueldoBasico, qry.Sexo, qry.NroDoc, qry.TipDoc   
from (select concat(se.apellido, ', ', se.nombre) as Nombre, replace(se.id, '-', '') as Cuil, 
sr.remunerativo as RemuneracionBruta, sr.no_remunerativo as RemuneracionNR, 
ifnull((select src.importe from idits.sld_recibo_concepto src where src.periodo = sr.periodo and src.empleado = sr.empleado and src.concepto = '990'), 0) as SueldoBasico,
se.sexo as Sexo, se.numero_documento as NroDoc, se.tipo_documento as TipDoc, sr.periodo as periodo, se.convenio as convenio 
from idits.sld_empleado se  
inner join idits.sld_recibo sr 
on sr.empleado = se.id 
where se.fecha_egreso is null) as qry 
where qry.periodo in ('2023_09') 
and qry.convenio = 'GUINCHEROS' 
group by qry.Nombre, qry.Cuil, qry.Sexo, qry.NroDoc, qry.TipDoc
order by 1""")

myresult = mycursor.fetchall()

GenerateXML("guincheros_2023_09.xml", myresult)

mycursor.close()