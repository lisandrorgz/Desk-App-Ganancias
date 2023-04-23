from src.clases.ValidationClass import Validations as Val
from src.clases.RegPageclass import RegPage as Reg
import pytest



@pytest.mark.parametrize("nombre, fecha, comentario, ganancia", 
    [
        (123, True, 50.0, "asd"), # Destructive Path
        ("Michael", True, 50.0, "asd"), # Alternative Path
        ("", "", "", 9999999999999999999999999999999999999999), # Valores limites
        ("", "", "", 0), # Valores limites
        ("", "", "", -1) # Valores limites
    ]

)
def test_validaciones(nombre, fecha, comentario, ganancia):
    assert Val.validaciones(nombre, fecha, comentario, ganancia) == False

@pytest.mark.parametrize("nombre, fecha, comentario, ganancia, dbturno", 
    [
        (123, True, 50.0, "asd", None), # Destructive Path
        ("Michael", True, 50.0, "asd", None), # Alternative Path
        ("", "", "", 9999999999999999999999999999999999999999, None), # Valores limites
        ("", "", "", 0, None), # Valores limites
        ("", "", "", -1, None) # Valores limites
    ]
)
def test_registro(nombre, fecha, comentario, ganancia, dbturno):
    assert Reg.guardar_un_dia(nombre, fecha, comentario, ganancia) == False