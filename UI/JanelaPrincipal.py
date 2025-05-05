from tkinter import *
from tkinter import ttk
from UI.JanelaCriarTarefa import JanelaCriarTarefa
from UI.JanelaPesquisarMateria import JanelaPesquisarMateria
from UI.JanelaPesquisarPorData import JanelaPesquisarPorData
from models.Tarefa import Tarefa
from UI.Janela import Janela

class JanelaPrincipal(Janela):
    def __init__(self):
        super().__init__()
        self.quadro_de_tarefas = self.criar_quadro_de_tarefas()
        self.criar_barra_de_menus()
    
    """
    Instancia o objeto Tk() da janela, o configura e retorna
    """
    def criar_janela(self):
        janela = Tk()
        janela.title('Agenda virtual')
        janela.geometry('800x600')
        janela.resizable(True, True)
        janela.option_add('*tearOff', FALSE)

        janela.columnconfigure(0, weight=1)
        janela.columnconfigure(1, weight=1)
        janela.columnconfigure(2, weight=1)

        return janela

    """
    Cria a barra de menu que fica em cima da janela
    """
    def criar_barra_de_menus(self):
        # cria a barra de menu na janela
        barra_de_menu = Menu(self.janela) 

        # cria os menus
        menu_tarefas = Menu(barra_de_menu)
        menu_exibir = Menu(barra_de_menu)

        # adiciona os menus na barra
        barra_de_menu.add_cascade(menu=menu_tarefas, label='Tarefa')
        barra_de_menu.add_cascade(menu=menu_exibir, label='Exibir')

        # adiciona as opções de cada menu
        menu_tarefas.add_command(label='Registrar tarefa', command=JanelaCriarTarefa)
        menu_exibir.add_command(label='Todas as tarefas', command=self.exibir_todas_as_tarefas)
        menu_exibir.add_command(label='Tarefas para hoje', command=self.exibir_tarefas_do_dia)
        menu_exibir.add_command(label='Pesquisar tarefa por matéria', command=JanelaPesquisarMateria)
        menu_exibir.add_command(label='Pesquisar tarefa por data de entrega', command=JanelaPesquisarPorData)

        self.janela['menu'] = barra_de_menu # fixa a barra de menu na janela

    """
    Cria o Frame onde as tarefas serão exibidas
    """
    def criar_quadro_de_tarefas(self):
        label_tarefas = Label(self.janela, text='Tarefas pendentes: ', font=('Arial', 14)).grid(column=0, row=0, padx=5, pady=5, sticky=W)
        separador = ttk.Separator(self.janela, orient=HORIZONTAL).grid(column=0, row=1, columnspan=3, padx=5, pady=5, sticky=EW)
        quadro_de_tarefas = Frame(self.janela, bg='gray80', relief='flat', bd=5)
        quadro_de_tarefas.grid(column=0, row=2, columnspan=3, padx=10, pady=10, sticky=NSEW)

        return quadro_de_tarefas

    def mainloop(self):
        self.janela.mainloop()

    """
    Cria as funções dos menus
    """
    def exibir_todas_as_tarefas(self):
        Tarefa.quadro_de_tarefas = self.quadro_de_tarefas
        Tarefa.exibir_todas_as_tarefas()

    def exibir_tarefas_do_dia(self):
        Tarefa.quadro_de_tarefas = self.quadro_de_tarefas
        Tarefa.exibir_tarefas_do_dia()
