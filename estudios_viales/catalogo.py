"""Catálogo de clases de vehículo, movimientos y categorías de peatones.

Los factores de equivalencia son provisionales (valores de arranque, no normados)
y se calibran con datos de campo. Cada resultado guarda PARAMETROS_VERSION.
"""
from dataclasses import dataclass

PARAMETROS_VERSION = "2026-11-04"


@dataclass(frozen=True)
class Clase:
    codigo: str
    nombre: str
    grupo: str  # particular | pasajeros | carga | otro
    factor: float


CLASES: dict[str, Clase] = {
    c.codigo: c
    for c in (
        Clase("AUT", "Auto", "particular", 1.0),
        Clase("TAX", "Taxi", "particular", 1.0),
        Clase("CAM", "Pick-up o van", "particular", 1.0),
        Clase("MOT", "Moto", "particular", 0.5),
        Clase("BIC", "Bici", "particular", 0.3),
        Clase("MIC", "Scooter o patín", "particular", 0.3),
        Clase("CRT", "Camión de ruta", "pasajeros", 2.0),
        Clase("CPE", "Camión de personal o empresa", "pasajeros", 2.0),
        Clase("COT", "Otro camión (escolar, foráneo)", "pasajeros", 2.0),
        Clase("RAB", "Rabón (2 ejes)", "carga", 2.0),
        Clase("TOR", "Tortón (3 ejes o más)", "carga", 2.5),
        Clase("TRA", "Tráiler", "carga", 3.0),
        Clase("OTR", "Otro", "otro", 2.0),
    )
}

MOVIMIENTOS = ("izquierda", "directo", "derecha", "vuelta U")
SEXOS = ("mujer", "hombre", "sin identificar")
EDADES = ("<13", "13-60", ">60")
CONDICIONES = ("movilidad reducida", "carriola", "bici por banqueta")


def factor(codigo: str) -> float:
    try:
        return CLASES[codigo].factor
    except KeyError:
        raise KeyError(f"Clase desconocida: {codigo}") from None
