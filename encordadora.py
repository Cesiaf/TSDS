# encordadora.py

import unicodedata

import unicodedata

class Encordadora:
    
    def __init__(self):
        self._cuerda_tensa = False
        self._tension_vertical = 0
        self._tension_horizontal = 0
        self._tipo_tension = ""
        
    # Atributos de la clase    
    
    @property
    def cuerda_tensa(self):
        return self._cuerda_tensa
    
    @cuerda_tensa.setter
    def cuerda_tensa(self, value):
        self._cuerda_tensa = value
    
    @property
    def tension_vertical(self):
        return self._tension_vertical
    
    @tension_vertical.setter
    def tension_vertical(self, value):
        if value <= 0:
            raise ValueError("La tensión vertical debe ser positiva y distinta de cero.")
        self._tension_vertical = value
    
    @property
    def tension_horizontal(self):
        return self._tension_horizontal
    
    @tension_horizontal.setter
    def tension_horizontal(self, value):
        if value <= 0:
            raise ValueError("La tensión horizontal debe ser positiva y distinta de cero.")
        self._tension_horizontal = value

    @property
    def tipo_tension(self):
        return self._tipo_tension
    
    @tipo_tension.setter
    def tipo_tension(self, value):
        tipos_validos = ["tensión uniforme", "tensión diferenciada"]
        tipo_tension_normalizado = self.normalizar_texto(value)
        tipos_validos_normalizados = [self.normalizar_texto(t) for t in tipos_validos]

        if tipo_tension_normalizado not in tipos_validos_normalizados:
            raise ValueError(f"Tipo de tensión no válida. Debe ser una de {', '.join(tipos_validos)}.")
        
        self._tipo_tension = value
    
    # Métodos de la clase 
    
    def ajustar_patron_encordado(self, cuerdas_verticales, cuerdas_horizontales):
        if cuerdas_verticales <= 0 or cuerdas_horizontales <= 0:
            raise ValueError("La cantidad de cuerdas no puede ser nula ni negativa")
        return cuerdas_verticales, cuerdas_horizontales
    
    def normalizar_texto(self, texto):
        # Convertir texto a minúsculas y eliminar acentos
        texto = texto.lower()
        texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
        return texto

    def tensar_cuerda(self, tipo_tension, tension_vertical, tension_horizontal):
        tipo_tension_normalizado = self.normalizar_texto(tipo_tension)
        tipos_validos = ["tensión uniforme", "tensión diferenciada"]
        tipos_validos_normalizados = [self.normalizar_texto(t) for t in tipos_validos]

        if tipo_tension_normalizado not in tipos_validos_normalizados:
            raise ValueError(f"Tipo de tensión no válida. Debe ser una de {', '.join(tipos_validos)}.")
        
        if tension_vertical <= 0 or tension_horizontal <= 0:
            raise ValueError("El valor de la tensión debe ser positivo y distinto de cero.")
        
        if tipo_tension_normalizado == self.normalizar_texto("tensión uniforme"):
            if tension_vertical != tension_horizontal:
                raise ValueError("Para tensión uniforme, los valores de tensión vertical y horizontal deben ser iguales.")
        
        if tipo_tension_normalizado == self.normalizar_texto("tensión diferenciada"):
            if tension_vertical == tension_horizontal:
                raise ValueError("Para tensión diferenciada, los valores de tensión vertical y horizontal deben ser distintos.")
        
        self.tipo_tension = tipo_tension
        self.tension_vertical = tension_vertical
        self.tension_horizontal = tension_horizontal
        self.cuerda_tensa = True
        
    def __str__(self):
        if self.cuerda_tensa:
            return (f"Encordadora con tensión {self.tipo_tension}. "
                    f"Tensión vertical: {self.tension_vertical} kg, "
                    f"Tensión horizontal: {self.tension_horizontal} kg.")
        else:
            return "Encordadora sin cuerda tensada."
        
    def __len__(self):
        if self.cuerda_tensa:
            return int(self.tension_vertical + self.tension_horizontal)
        else:
            return 0

    def cortar_cuerda(self):
        if not self.cuerda_tensa:
            raise ValueError("La cuerda no está tensa")
            
        self.cuerda_tensa = False
        return "Cuerda cortada y sobrante eliminado."

    