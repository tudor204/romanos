from romanos_class import NumeroRomano

def test_suma_romanos():
    nr1 =NumeroRomano("XXX")
    nr2 = NumeroRomano(5)

    nr3 = nr1 + nr2

    assert isinstance(nr3,NumeroRomano) == True
    assert nr3.valor ==50
    assert nr3.representacion == "L"