import pytest

from estudios_viales.catalogo import CLASES, EDADES, MOVIMIENTOS, SEXOS, factor


def test_trece_clases_y_factores():
    assert len(CLASES) == 13
    assert factor("TRA") == 3.0 and factor("MOT") == 0.5 and factor("AUT") == 1.0


def test_codigo_desconocido():
    with pytest.raises(KeyError, match="Clase desconocida: XYZ"):
        factor("XYZ")


def test_listas_fijas():
    assert MOVIMIENTOS == ("izquierda", "directo", "derecha", "vuelta U")
    assert SEXOS == ("mujer", "hombre", "sin identificar")
    assert EDADES == ("<13", "13-60", ">60")
