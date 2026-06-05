from flask import render_template
class ModuloView:
    def __init__(self):
        pass

    def modulo(self,listaFases):
        return render_template('trilhaModulo.html',listaFases=listaFases)