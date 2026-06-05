from flask import redirect, session, flash, url_for
from dao.ModuloDao import ModuloDao
from dao.FaseDao import FaseDao
from dao.ProgressoDao import ProgressoDao
from views.ModuloView import ModuloView
class ModuloService:
    def __init__(self):
        pass

    def modulo(self):
        if not self.verificarLogin():
            return redirect('login')
        idUsuario = session['usuario_logado']
        oModuloDao = ModuloDao()
        oModuloView = ModuloView()
        oFaseDao = FaseDao()
        oProgressoDao = ProgressoDao()
        progresso = oProgressoDao.getProgresso(idUsuario)
        if progresso:
            idFase = progresso.idFase
        else:
            idFase = 1
        idModulo = oFaseDao.getFase(idFase).idModulo
        listaFases = oModuloDao.getModulo(idModulo).fase
        if listaFases:
            print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
            print(listaFases)
            return oModuloView.modulo(listaFases)
        else:
            flash('Módulo não encontrado','danger')
            return redirect('/principal')
        
                        
#funções auxiliares
    def verificarLogin(self):
        if 'usuario_logado' not in session or session['usuario_logado'] is None:
            flash('Faça login para acessar esta página', 'danger')
            return False
        return True