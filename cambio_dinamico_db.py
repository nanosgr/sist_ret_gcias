from datetime import date
from enum import Enum
from decimal import Decimal
from typing import Optional, List
from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String, BLOB, Date, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from starlette.requests import Request

class Sexo(Enum):
    M = 'M'
    F = 'F'
    X = 'X'

class EstadoCivil(Enum):
    SOL = 'SOLTERO'
    CAS = 'CASADO'
    CON = 'CONCUBINATO'
    DIV = 'DIVORCIADO'
    SEP = 'SEPARADO'
    VIU = 'VIUDO'

class Jornada(Enum):
    COM = 'COMPLETA'
    PAR = 'PARCIAL'
    RED = 'REDUCIDA'
    MED = 'MEDIA'

class Liquidacion(Enum):
    M = 'MENSUAL'
    Q = 'QUINCENA'

def custom_openapi():
    header = {
            "required": True,
            "schema": {
              "title": "X-Database-Name",
              "type": "string"
            },
            "name": "X-Database-Name",
            "in": "header"
          }
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema

    paths = openapi_schema["paths"]
    for url, methods in paths.items():
        for method in methods:
            if methods[method].get("parameters"):
                methods[method]["parameters"].append(header)
            else:
                methods[method]["parameters"] = [header]

    return app.openapi_schema

app = FastAPI()
app.openapi = custom_openapi

# Define the base database connection string
DATABASE_URL_TEMPLATE = "mysql+pymysql://root:root@192.168.24.121/{db_name}"

# Create a declarative base class
Base = declarative_base()

# Define the User schema
class SldEmpleado(BaseModel):
    id: Optional[str] = None
    apellido: Optional[str] = None
    nombre: Optional[str] = None
    cuil: Optional[str] = None
    grupo: Optional[str] = None
    estado: Optional[str] = None
    tarea: Optional[str] = None
    fecha_ingreso: Optional[date] = None
    fecha_egreso: Optional[date] = None
    fecha_antiguedad: Optional[date] = None
    antiguedad: Optional[int] = None
    sexo: Optional[Sexo] = None
    fecha_nacimiento: Optional[date] = None
    nacionalidad: Optional[str] = None
    estado_civil: Optional[EstadoCivil] = 'SOLTERO'
    tipo_documento: Optional[str] = None
    numero_documento: Optional[str] = None
    direccion: Optional[str] = None
    localidad: Optional[str] = None
    provincia: Optional[str] = None
    cpa: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    foto: Optional[bytes] = None
    orden: Optional[int] = None
    convenio: Optional[str] = None
    categoria: Optional[str] = None
    sueldo: Optional[Decimal] = None
    adicional: Optional[Decimal] = None
    auxiliar: Optional[Decimal] = None
    dias: Optional[Decimal] = None
    horas: Optional[Decimal] = None
    porcentaje: Optional[Decimal] = None
    jornada: Optional[Jornada] = 'COMPLETA' # Field(COM = 'COMPLETA')
    proporcional: Optional[bool] = False
    liquidacion: Optional[Liquidacion] = 'MENSUAL'
    moneda: Optional[str] = None
    vacaciones: Optional[int] = None
    obra_social: Optional[str] = None
    sindicato: Optional[str] = None
    proyecto: Optional[str] = None
    empresa: Optional[str] = None
    lugar_trabajo: Optional[str] = None
    banco: Optional[str] = None
    cuenta: Optional[str] = None
    cbu: Optional[str] = None
    grupo_de_conceptos: Optional[str] = None
    observaciones: Optional[str] = None

    class Config:
        orm_mode = True

# Define the User model
class sld_empleado(Base):
    __tablename__ = 'sld_empleado'

    id = Column(String, primary_key=True)
    apellido = Column(String(20))
    nombre = Column(String(25))
    cuil = Column(String(25))
    grupo = Column(String(20))
    estado = Column(String(20))
    tarea = Column(String(50))
    fecha_ingreso = Column(Date)
    fecha_egreso = Column(Date)
    fecha_antiguedad = Column(Date)
    antiguedad = Column(Integer)
    sexo = Column(String(1))
    fecha_nacimiento = Column(Date)
    nacionalidad = Column(String(25))
    estado_civil = Column(String(20))
    tipo_documento = Column(String(5))
    numero_documento = Column(String(15))
    direccion = Column(String(100))
    localidad = Column(String(40))
    provincia = Column(String(20))
    cpa = Column(String(10))
    telefono = Column(String(100))
    email = Column(String(100))
    foto = Column(BLOB)
    orden = Column(Integer)
    convenio = Column(String(20))
    categoria = Column(String(20))
    sueldo = Column(Float)
    adicional = Column(Float)
    auxiliar = Column(Float)
    dias = Column(Float)
    horas = Column(Float)
    porcentaje = Column(Float)
    jornada = Column(String(20))
    proporcional = Column(Boolean)
    liquidacion = Column(String(15))
    moneda = Column(String(5))
    vacaciones = Column(Integer)
    obra_social = Column(String(20))
    sindicato = Column(String(20))
    proyecto = Column(String(20))
    empresa = Column(String(30))
    lugar_trabajo = Column(String(50))
    banco = Column(String(40))
    cuenta = Column(String(40))
    cbu = Column(String(25))
    grupo_de_conceptos = Column(String(20))
    observaciones = Column(String(50))

class SldSindicato(BaseModel):
    id : Optional[str] = None
    descripcion : Optional[str] = None
    aporte_porcentaje : Optional[Decimal] = None
    aporte_importe : Optional[Decimal] = None
    retencion_porcentaje : Optional[Decimal] = None
    retencion_importe : Optional[Decimal] = None
    orden : Optional[int] = None

    class Config:
        orm_mode = True

class sld_sindicato(Base):
    __tablename__ = 'sld_sindicato'

    id = Column(String(20), primary_key=True)
    descripcion = Column(String(100))
    aporte_porcentaje = Column(Float)
    aporte_importe = Column(Float)
    retencion_porcentaje = Column(Float)
    retencion_importe = Column(Float)
    orden = Column(Integer)

database_url = DATABASE_URL_TEMPLATE.format(db_name='masterestudio').replace("'", "")
engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to dynamically get the database session
def get_db(request: Request):
    db_name = request.headers.get('X-Database-Name')
    if not db_name:
        raise HTTPException(status_code=400, detail="X-Database-Name header missing")

    database_url = DATABASE_URL_TEMPLATE.format(db_name=db_name).replace("'", "")
    # # database_url = database_url.replace("'", "")
    engine = create_engine(database_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    # # Base.metadata.create_all(bind=engine)
    # print("conectando a la base de datos: " + db_name)
    db = SessionLocal()
    # db.connection(execution_options={"schema_translate_map": {"masterestudio": db_name}})
    try:
        yield db
    finally:
        db.close()

@app.get("/employees", response_model=List[SldEmpleado])
def get_employees(db: SessionLocal = Depends(get_db)):
    return db.query(sld_empleado).filter(sld_empleado.fecha_egreso == None).order_by('orden').all()    

@app.get("/unions", response_model=List[SldSindicato])
def get_unions(db: SessionLocal = Depends(get_db)):
    return db.query(sld_sindicato).order_by('orden').all()

# Now use the get_db dependency in your endpoints
# @app.post("/users/", response_model=UserCreate)
# def create_user(user: UserCreate, db: SessionLocal = Depends(get_db)):
#     # Your existing create_user logic here
#     pass

# Repeat the use of Depends(get_db) for other endpoints
# In this example, the get_db dependency function reads the X-Database-Name header from the incoming request. 
# It uses this header to format the DATABASE_URL_TEMPLATE with the correct database name, creates a new SQLAlchemy engine and session for that database, 
# and then yields the session for use in the endpoint.

# When making requests to the FastAPI application, the client should include the X-Database-Name header with the name of the target database:

# POST /users/ HTTP/1.1
# Host: localhost:8000
# Content-Type: application/json
# X-Database-Name: dynamic_db_name

# {
#     "username": "john_doe",
#     "email": "john@example.com"
# }

# HTTP

# Please note that this approach creates a new SQLAlchemy engine for each request, which can be resource-intensive. In a production environment, 
# you would want to optimize this by reusing engine instances for the same database or implementing a connection pool.

# Additionally, be cautious with this approach as it can expose your application to security risks if not properly handled. 
# Ensure that the databases are properly isolated and that access is controlled to prevent unauthorized database switching.