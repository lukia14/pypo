from service.ModuloService import ModuloService

class ModuloController:
    def __init__(self):
        pass

    def modulo(self):
        oModuloService = ModuloService()
        return oModuloService.modulo()