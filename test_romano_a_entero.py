from old_main import romano_a_entero,RomanNumberError
import pytest 

def romano_a_entero_I():
    assert romano_a_entero("I") == 1

def romano_a_entero_MDCCXIII():
    assert romano_a_entero("MDCCXIII") == 1713

def romano_a_entero_MDCCXIII():
    assert romano_a_entero("IV") == 4

def test_romano_a_entero_no_repetir_mas_de_tres():
    with pytest.raises( RomanNumberError ) as exception:
        romano_a_entero("LIII")
    assert str(exception.value) == "No se puede repetir el valor mas de tres veces"

def test_romano_a_entero_no_repetir_caracteres_especiales():
    with pytest.raises (RomanNumberError) as exceptionInfo:
        romano_a_entero("DD")
    assert str(exceptionInfo.value) == "Los caracteres D,L y V no se pueden repetir"
def test_romano_a_entero_restasI():
    with pytest.raises (RomanNumberError) as exceptionInfo:
        romano_a_entero("IL")
    assert str(exceptionInfo.value) == "I solo se puede restar de V y X"

def test_romano_a_entero_restasX():
    with pytest.raises (RomanNumberError) as exceptionInfo:
        romano_a_entero("XM")
    assert str(exceptionInfo.value) == "X solo se puede restar de L y C"

def test_romano_a_entero_si_se_repiten_no_se_pueden_restar_IXC():
    with pytest.raises (RomanNumberError) as exceptionInfo:
        romano_a_entero("IIX")
    assert str(exceptionInfo) == "el valor no puede restarse"



