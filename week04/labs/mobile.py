# Creamos una clase genérica, clase universal donde incluye caractéristicas comunes a unos objetos

class Mobile:
    '''
    Docstring: clase Mobile
    Definir la clase con argumentos , ram, display, precio, camara, bateria
    '''
    def __init__(self, ram, display, price, camara, bateria):
        self.ram = ram
        self.display = display
        self.price = price
        self.camara = camara
        self.bateria = bateria
       
    # Creamos métodos para configurar los atributos de la clase
    def set_ram(self, ram):
        self.ram = ram
        return self.ram
        
    def set_display(self, display):
        self.display = display
        return self.display
        
    def set_price(self, price):
        self.price = price
    
    def set_camara(self, camara):
        self.camara = camara
        
    def set_bateria(self, bateria):
        self.bateria = bateria
    
    # Creamos métodos para recoger la info de los atributos de la clase
    def get_ram(self):
        return self.ram
    
    def get_display(self):
        return self.display


# Cuando creamos subclases , comparte elementos comunes a todos los objetos más los específicos de esta subclase
class Samsung(Mobile):
    # Inicializamos la clase Samsung
    def __init__(self, ram, display, price, camara, bateria, performance):
        Mobile.__init__(self, ram, display, price, camara, bateria)
        # inicializa la clase Mobile
        self.performance = performance

    def set_perfomance(self, performance):
        self.perfomance = performance

    def get_perfomance(self):
        return self.performance

    
# Creamos la subclase Apple, con el argumento posicional "detalle"
class Apple(Mobile):
    # Inicializamos la clase Apple
    def __init__(self, ram, display, price, camara, bateria, detalle):
        Mobile.__init__(self, ram, display, price, camara, bateria)
        # inicializa la clase Mobile
        self.detalle = detalle

    def set_detalle(self, detalle):
        self.detalle = detalle

    def get_detalle(self):
        return self.detalle
