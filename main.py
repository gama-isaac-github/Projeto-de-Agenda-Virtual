from UI.JanelaPrincipal import *
from models.Tarefa import Tarefa
from models.serializador_de_tarefas import salvar_tarefas, carregar_tarefas
import os
import pickle

if __name__ == '__main__':
    janela_principal = JanelaPrincipal()
    Tarefa.quadro_de_tarefas = janela_principal.quadro_de_tarefas

    Tarefa.lista_de_tarefas = carregar_tarefas('tarefas.pkl')

    Tarefa.exibir_todas_as_tarefas()

    janela_principal.mainloop()