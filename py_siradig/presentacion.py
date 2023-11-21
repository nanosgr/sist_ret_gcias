from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://siradig.afip.gob.ar/presentacion"


@dataclass
class DatoAdicionalType:
    nombre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    mes_desde: Optional[str] = field(
        default=None,
        metadata={
            "name": "mesDesde",
            "type": "Attribute",
        }
    )
    mes_hasta: Optional[str] = field(
        default=None,
        metadata={
            "name": "mesHasta",
            "type": "Attribute",
        }
    )
    valor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DetalleType:
    nombre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DireccionType:
    provincia: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
        }
    )
    cp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
        }
    )
    localidad: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
        }
    )
    calle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
        }
    )
    nro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
        }
    )
    piso: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
        }
    )
    dpto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
        }
    )


@dataclass
class IngresoAporteType:
    obra_soc: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "obraSoc",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    seg_soc: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "segSoc",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    sind: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    gan_brut: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ganBrut",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    ret_gan: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "retGan",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_inclusive": Decimal("-9999999999999.99"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    retrib_no_hab: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "retribNoHab",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    ajuste: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_inclusive": Decimal("-9999999999999.99"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    exe_no_alc: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "exeNoAlc",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    sac: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_inclusive": Decimal("-9999999999999.99"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    horas_ext_gr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "horasExtGr",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    horas_ext_ex: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "horasExtEx",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    mat_did: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "matDid",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    gastos_mov_viat: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "gastosMovViat",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    bonos_prod: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "bonosProd",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_inclusive": Decimal("-9999999999999.99"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    fallos_caja: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "fallosCaja",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_inclusive": Decimal("-9999999999999.99"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    con_sim_nat: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "conSimNat",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_inclusive": Decimal("-9999999999999.99"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    remun_exenta_ley27549: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "remunExentaLey27549",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_inclusive": Decimal("-9999999999999.99"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    suplem_partic_ley19101: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "suplemParticLey19101",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_inclusive": Decimal("-9999999999999.99"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    teletrabajo_exento: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "teletrabajoExento",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_inclusive": Decimal("-9999999999999.99"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    mes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PeriodoType:
    mes_desde: Optional[str] = field(
        default=None,
        metadata={
            "name": "mesDesde",
            "type": "Attribute",
        }
    )
    mes_hasta: Optional[str] = field(
        default=None,
        metadata={
            "name": "mesHasta",
            "type": "Attribute",
        }
    )
    monto_mensual: Optional[str] = field(
        default=None,
        metadata={
            "name": "montoMensual",
            "type": "Attribute",
        }
    )


class SiNoSimpleType(Enum):
    S = "S"
    N = "N"


@dataclass
class ArrayDatosAdicionalesType:
    dato_adicional: List[DatoAdicionalType] = field(
        default_factory=list,
        metadata={
            "name": "datoAdicional",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_occurs": 1,
        }
    )


@dataclass
class ArrayDetallesType:
    detalle: List[DetalleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_occurs": 1,
        }
    )


@dataclass
class ArrayIngresosAportesType:
    ing_ap: List[IngresoAporteType] = field(
        default_factory=list,
        metadata={
            "name": "ingAp",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_occurs": 1,
        }
    )


@dataclass
class ArrayPeriodosType:
    periodo: List[PeriodoType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_occurs": 1,
        }
    )


@dataclass
class CargaFamiliaType:
    tipo_doc: Optional[int] = field(
        default=None,
        metadata={
            "name": "tipoDoc",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    nro_doc: Optional[str] = field(
        default=None,
        metadata={
            "name": "nroDoc",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
            "max_length": 11,
        }
    )
    apellido: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
            "max_length": 50,
        }
    )
    nombre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "max_length": 50,
        }
    )
    fecha_nac: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "fechaNac",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
        }
    )
    mes_desde: Optional[int] = field(
        default=None,
        metadata={
            "name": "mesDesde",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
        }
    )
    mes_hasta: Optional[int] = field(
        default=None,
        metadata={
            "name": "mesHasta",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
        }
    )
    parentesco: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
        }
    )
    vigente_proximos_periodos: Optional[SiNoSimpleType] = field(
        default=None,
        metadata={
            "name": "vigenteProximosPeriodos",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
        }
    )
    fecha_limite: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "fechaLimite",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
        }
    )
    porcentaje_deduccion: Optional[int] = field(
        default=None,
        metadata={
            "name": "porcentajeDeduccion",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
        }
    )


@dataclass
class EmpleadoType:
    cuit: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
            "min_exclusive": 9999999999,
            "max_inclusive": 99999999999,
        }
    )
    tipo_doc: Optional[int] = field(
        default=None,
        metadata={
            "name": "tipoDoc",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    apellido: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
            "max_length": 50,
        }
    )
    nombre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "max_length": 50,
        }
    )
    direccion: Optional[DireccionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
        }
    )


@dataclass
class AjusteType:
    cuit: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_exclusive": 9999999999,
            "max_inclusive": 99999999999,
        }
    )
    denominacion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "max_length": 200,
        }
    )
    desc_basica: Optional[str] = field(
        default=None,
        metadata={
            "name": "descBasica",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
            "max_length": 300,
        }
    )
    desc_adicional: Optional[str] = field(
        default=None,
        metadata={
            "name": "descAdicional",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "max_length": 300,
        }
    )
    monto_total: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "montoTotal",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    detalles: Optional[ArrayDetallesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
        }
    )
    tipo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ArrayCargasFamiliaType:
    carga_familia: List[CargaFamiliaType] = field(
        default_factory=list,
        metadata={
            "name": "cargaFamilia",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_occurs": 1,
        }
    )


@dataclass
class ConceptoType:
    tipo_doc: Optional[int] = field(
        default=None,
        metadata={
            "name": "tipoDoc",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    nro_doc: Optional[str] = field(
        default=None,
        metadata={
            "name": "nroDoc",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "max_length": 11,
        }
    )
    denominacion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "max_length": 200,
        }
    )
    desc_basica: Optional[str] = field(
        default=None,
        metadata={
            "name": "descBasica",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
            "max_length": 300,
        }
    )
    desc_adicional: Optional[str] = field(
        default=None,
        metadata={
            "name": "descAdicional",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "max_length": 300,
        }
    )
    monto_total: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "montoTotal",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("9999999999999.99"),
        }
    )
    periodos: Optional[ArrayPeriodosType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
        }
    )
    detalles: Optional[ArrayDetallesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
        }
    )
    tipo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EmpleadorEntidadType:
    cuit: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
            "min_exclusive": 9999999999,
            "max_inclusive": 99999999999,
        }
    )
    denominacion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
            "max_length": 200,
        }
    )
    ingresos_aportes: Optional[ArrayIngresosAportesType] = field(
        default=None,
        metadata={
            "name": "ingresosAportes",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
        }
    )


@dataclass
class ArrayAjustesType:
    ajuste: List[AjusteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_occurs": 1,
        }
    )


@dataclass
class ArrayDeduccionesType:
    deduccion: List[ConceptoType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_occurs": 1,
        }
    )


@dataclass
class ArrayOtrosEmpEntType:
    emp_ent: List[EmpleadorEntidadType] = field(
        default_factory=list,
        metadata={
            "name": "empEnt",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_occurs": 1,
        }
    )


@dataclass
class ArrayRetPerPagosType:
    ret_per_pago: List[ConceptoType] = field(
        default_factory=list,
        metadata={
            "name": "retPerPago",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "min_occurs": 1,
        }
    )


@dataclass
class PresentacionType:
    periodo: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
        }
    )
    nro_presentacion: Optional[int] = field(
        default=None,
        metadata={
            "name": "nroPresentacion",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
        }
    )
    fecha_presentacion: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "fechaPresentacion",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
        }
    )
    empleado: Optional[EmpleadoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
            "required": True,
        }
    )
    cargas_familia: Optional[ArrayCargasFamiliaType] = field(
        default=None,
        metadata={
            "name": "cargasFamilia",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
        }
    )
    gan_liq_otros_emp_ent: Optional[ArrayOtrosEmpEntType] = field(
        default=None,
        metadata={
            "name": "ganLiqOtrosEmpEnt",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
        }
    )
    deducciones: Optional[ArrayDeduccionesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
        }
    )
    ret_per_pagos: Optional[ArrayRetPerPagosType] = field(
        default=None,
        metadata={
            "name": "retPerPagos",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
        }
    )
    ajustes: Optional[ArrayAjustesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
        }
    )
    datos_adicionales: Optional[ArrayDatosAdicionalesType] = field(
        default=None,
        metadata={
            "name": "datosAdicionales",
            "type": "Element",
            "namespace": "http://siradig.afip.gob.ar/presentacion",
        }
    )


@dataclass
class Presentacion(PresentacionType):
    class Meta:
        name = "presentacion"
        namespace = "http://siradig.afip.gob.ar/presentacion"
