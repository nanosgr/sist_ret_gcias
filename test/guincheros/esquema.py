from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional


@dataclass
class Empleados:
    empleado: List["Empleados.Empleado"] = field(
        default_factory=list,
        metadata={
            "name": "Empleado",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Empleado:
        nombre: Optional[str] = field(
            default=None,
            metadata={
                "name": "Nombre",
                "type": "Element",
                "required": True,
            }
        )
        cuil: Optional[str] = field(
            default=None,
            metadata={
                "name": "Cuil",
                "type": "Element",
                "required": True,
                "pattern": r"[0-9_]{11}",
            }
        )
        remuneracion_bruta: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "RemuneracionBruta",
                "type": "Element",
                "required": True,
            }
        )
        sueldo_basico: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "SueldoBasico",
                "type": "Element",
                "nillable": True,
            }
        )
        sexo: Optional[str] = field(
            default=None,
            metadata={
                "name": "Sexo",
                "type": "Element",
                "required": True,
                "pattern": r"[MF]",
            }
        )
        nro_doc: Optional[str] = field(
            default=None,
            metadata={
                "name": "NroDoc",
                "type": "Element",
                "required": True,
                "pattern": r"[0-9_]{8}",
            }
        )
        tip_doc: Optional[str] = field(
            default=None,
            metadata={
                "name": "TipDoc",
                "type": "Element",
                "required": True,
                "pattern": r"DU|LE|CI|LC|PA|EX",
            }
        )
