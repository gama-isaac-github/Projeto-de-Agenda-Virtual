from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from models.Tarefa import Tarefa
from UI.Janela import Janela

class JanelaPesquisarPorData(Janela):
    def __init__(self):
        super().__init__()
        self.quadro_de_tarefas = self.criar_quadro_de_tarefas()
        self.criar_campos_de_entrada()

    """
    Cria a janela e abre como uma toplevel
    """
    def criar_janela(self):
        janela = Toplevel()
        janela.title('Pesquisar tarefa por data de entrega')
        janela.geometry('600x500')
        janela.resizable(True, True)

        titulo = Label(janela, text=('Insira uma data de entrega'), font=('Arial', 14))
        titulo.grid(column=0, row=0, padx=5, pady=5, sticky=W)
        separador = ttk.Separator(janela, orient=HORIZONTAL)
        separador.grid(column=0, row=1, columnspan=2, padx=5, pady=5, sticky=EW)

        return janela
    
    """
    Cria os campos de entrada para pesquisar as tarefas correspondentes
    """
    def criar_campos_de_entrada(self):
        label_materia = Label(self.janela, text='Data: ', font=('Arial', 12))
        label_materia.grid(column=0, row=2, padx=5, pady=5, sticky=W)
        self.input_data = DateEntry(self.janela, date_pattern='dd/mm/yyyy')
        self.input_data.grid(column=1, row=2, padx=5, pady=5, sticky=W)

        button_pesquisar = Button(self.janela, text='Pesquisar', command=self.pesquisar_tarefas)
        button_pesquisar.grid(column=0, row=3, padx=5, pady=5, sticky=W)
    
    """
    Cria o quadro de tarefas da janela
    """
    def criar_quadro_de_tarefas(self):
        quadro_de_tarefas = Frame(self.janela, bg='gray80', relief='flat', bd=5)
        quadro_de_tarefas.grid(column=0, row=4, columnspan=2, padx=5, pady=5, sticky=NSEW)

        return quadro_de_tarefas
    
    def pesquisar_tarefas(self):
        Tarefa.quadro_de_tarefas = self.quadro_de_tarefas
        Tarefa.exibir_tarefas_por_data_de_entrega(self.input_data.get())
