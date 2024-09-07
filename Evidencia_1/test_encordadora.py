import pytest
from encordadora import Encordadora

def test_ajustar_patron_encordado_valores_positivos():
    cuerdas_verticales = 16
    cuerdas_horizontales = 20
    
    mi_encordadora = Encordadora()
    resultado = mi_encordadora.ajustar_patron_encordado(cuerdas_verticales, cuerdas_horizontales)

    assert resultado == (cuerdas_verticales, cuerdas_horizontales)

def test_ajustar_patron_encordado_error_cuerdas_nulas():
    cuerdas_verticales = 20
    cuerdas_horizontales = 0
    
    mi_encordadora = Encordadora()

    with pytest.raises(ValueError, match="La cantidad de cuerdas no puede ser nula ni negativa"):
        mi_encordadora.ajustar_patron_encordado(cuerdas_verticales, cuerdas_horizontales)
        
def test_ajustar_patron_encordado_error_cuerdas_negativas():
    cuerdas_verticales = -13
    cuerdas_horizontales = 25
    
    mi_encordadora = Encordadora()

    with pytest.raises(ValueError, match="La cantidad de cuerdas no puede ser nula ni negativa"):
        mi_encordadora.ajustar_patron_encordado(cuerdas_verticales, cuerdas_horizontales)

def test_tensar_cuerda_valores_invalidos_nulo():
    tension_cuerda_horizontal = 0
    tension_cuerda_vertical = 0
   
    mi_encordadora = Encordadora()
    
    with pytest.raises(ValueError, match="El valor de la tensión debe ser positivo y distinto de cero."):
        mi_encordadora.tensar_cuerda("Tensión uniforme", tension_cuerda_vertical, tension_cuerda_horizontal)
    
def test_tensar_cuerda_uniforme_valores_validos():
    # Valores iguales
    tension_cuerda_horizontal = 21
    tension_cuerda_vertical = 21
    mi_encordadora = Encordadora()
    mi_encordadora.tensar_cuerda("Tensión uniforme", tension_cuerda_vertical, tension_cuerda_horizontal)
    assert mi_encordadora.tension_vertical == tension_cuerda_vertical
    assert mi_encordadora.tension_horizontal == tension_cuerda_horizontal
    assert mi_encordadora.tipo_tension.lower() == "tensión uniforme"
    
def test_tensar_cuerda_uniforme_valores_invalidos():
    # Valores distintos
    tension_cuerda_horizontal = 16
    tension_cuerda_vertical = 24
   
    mi_encordadora = Encordadora()
    
    with pytest.raises(ValueError, match="Para tensión uniforme, los valores de tensión vertical y horizontal deben ser iguales"):
        mi_encordadora.tensar_cuerda("Tensión uniforme", tension_cuerda_vertical, tension_cuerda_horizontal)
   
def test_tensar_cuerda_diferenciada_valores_validos():
    # Valores distintos
    tension_cuerda_vertical = 50
    tension_cuerda_horizontal = 55
    mi_encordadora = Encordadora()
    mi_encordadora.tensar_cuerda("TENSIÓN DIFERENCIADA", tension_cuerda_vertical, tension_cuerda_horizontal)
    assert mi_encordadora.tipo_tension.lower() == "tensión diferenciada"
    assert mi_encordadora.tension_vertical == tension_cuerda_vertical
    assert mi_encordadora.tension_horizontal == tension_cuerda_horizontal

def test_tensar_cuerda_diferenciada_valores_invalidos():
    # Valores iguales
    tension_cuerda_horizontal = 50
    tension_cuerda_vertical = 50
   
    mi_encordadora = Encordadora()
    
    with pytest.raises(ValueError, match="Para tensión diferenciada, los valores de tensión vertical y horizontal deben ser distintos"):
        mi_encordadora.tensar_cuerda("Tensión diferenciada", tension_cuerda_vertical, tension_cuerda_horizontal)
     
def test_tensar_cuerda_tipo_tension_invalido():
    tension_cuerda_horizontal = 16
    tension_cuerda_vertical = 24
   
    mi_encordadora = Encordadora()
    
    with pytest.raises(ValueError, match="Tipo de tensión no válida. Debe ser una de tensión uniforme, tensión diferenciada."):
        mi_encordadora.tensar_cuerda("otra tensión", tension_cuerda_vertical, tension_cuerda_horizontal)

def test_cortar_cuerda_despues_de_tensarla():
    mi_encordadora = Encordadora()
    mi_encordadora.tensar_cuerda("tensión uniforme", 30, 30)
    
    resultado = mi_encordadora.cortar_cuerda()
    
    assert resultado == "Cuerda cortada y sobrante eliminado."
    assert not mi_encordadora.cuerda_tensa

def test_cortar_cuerda_sin_tensarla():
    mi_encordadora = Encordadora()

    with pytest.raises(ValueError, match="La cuerda no está tensa"):
        mi_encordadora.cortar_cuerda()
