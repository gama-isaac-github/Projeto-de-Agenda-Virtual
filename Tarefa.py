from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from models.serializador_de_tarefas import salvar_tarefas, carregar_tarefas
import PIL.Image
import time
import pickle

class Tarefa:
    # lista static com todas as tarefas
    lista_de_tarefas = []
    quadro_de_tarefas = None # Quadro onde as tarefas serão exibidas
    materias = ('APF', 'Arte', 'Biologia', 'Educação Física', 'Espanhol', 'Filosofia', 'Física', 'Geografia', 'História', 'IP', 'Inglês', 'ICM', 'Matemática', 'Português', 'Literatura', 'Redação', 'Química', 'Sociologia')
    ok_icon = None # Imagem do botão de concluir tarefa

    def __init__(self, materia, data_de_entrega, descricao, valor, tipo, data_de_realizacao):
        self.materia = materia
        self.data_de_entrega = data_de_entrega
        self.descricao = descricao
        self.valor = valor
        self.tipo = tipo
        self.data_de_realizacao = data_de_realizacao
        self.widget_tarefa = Frame(Tarefa.quadro_de_tarefas, bg='gray100', relief='raised', bd=5)
        Tarefa.lista_de_tarefas.append(self)

        salvar_tarefas(Tarefa.lista_de_tarefas, 'tarefas.pkl')

    def __getstate__(self):
        atributos = self.__dict__.copy()

        # Ignora os atributos gráficos
        if 'widget_tarefa' in atributos:
            del atributos['widget_tarefa']
        if 'ok_icon' in atributos:
            del atributos['ok_icon']

        return atributos

    """
    Cria o widget que representa a tarefa no quadro
    """
    def adicionar_tarefa_no_quadro(self):
        self.widget_tarefa = Frame(Tarefa.quadro_de_tarefas, bg='gray100', relief='raised', bd=5)

        # configura o gerenciador de geometria de grid para o Frame
        for i in range(0, 10):
            self.widget_tarefa.columnconfigure(i, weight=1)
        
        # adiciona o botão de concluir tarefa
        if Tarefa.ok_icon is None:
            Tarefa.ok_icon = PIL.Image.open('Assets/ok_icon.png').resize((15, 15))
            Tarefa.ok_icon = ImageTk.PhotoImage(Tarefa.ok_icon)
        botao_de_conclusao = ttk.Button(self.widget_tarefa, image=Tarefa.ok_icon, command=self.concluir_tarefa)
        botao_de_conclusao.grid(column=0, row=0, padx=3, pady=6)

        # adiciona a label de matéria
        label_materia = Label(self.widget_tarefa, text=self.materia, font=('Arial', 10), background='gray100')
        label_materia.grid(column=1, row=0, sticky=EW, padx=3, pady=3)
        separador = ttk.Separator(self.widget_tarefa, orient=VERTICAL)
        separador.grid(column=2, row=0, sticky=NS, padx=5, pady=3)

        # adiciona a label da descrição
        label_descricao = Label(self.widget_tarefa, text=self.descricao, font=('Arial', 10), background='gray100')
        label_descricao.grid(column=3, row=0, sticky=EW, padx=3, pady=3)
        separador = ttk.Separator(self.widget_tarefa, orient=VERTICAL)
        separador.grid(column=4, row=0, sticky=NS, padx=5, pady=3)

        # adiciona a label da data de entrega
        label_data_de_entrega = Label(self.widget_tarefa, text=f'Entrega: {self.data_de_entrega}', font=('Arial', 10), background='gray100')
        label_data_de_entrega.grid(column=5, row=0, sticky=EW, padx=3, pady=3)
        separador = ttk.Separator(self.widget_tarefa, orient=VERTICAL)
        separador.grid(column=6, row=0, sticky=NS, padx=5, pady=3)

        # adiciona a label do valor e tipo
        label_valor = Label(self.widget_tarefa, text=f'Valor: {self.valor} - {self.tipo}', font=('Arial', 10), background='gray100')
        label_valor.grid(column=7, row=0, sticky=EW, padx=3, pady=3)
        separador = ttk.Separator(self.widget_tarefa, orient=VERTICAL)
        separador.grid(column=8, row=0, sticky=NS, padx=5, pady=3)

        # adiciona a label de data para ser feita
        label_data_de_realizacao = Label(self.widget_tarefa, text=f'Será feita em: {self.data_de_realizacao}', font=('Arial', 10), background='gray100')
        label_data_de_realizacao.grid(column=9, row=0, sticky=EW, padx=3, pady=3)

        self.widget_tarefa.pack(anchor=W, fill=X)

    """
    Método que marca uma tarefa como concluída, é chamado pelo botão de conclusão da tarefa
    """
    def concluir_tarefa(self):
        Tarefa.lista_de_tarefas.remove(self) # remove a tarefa da lista
        self.widget_tarefa.destroy() # destrói o widget da tarefa

        salvar_tarefas(Tarefa.lista_de_tarefas, 'tarefas.pkl')

        del self # apaga o próprio objeto da tarefa

    """
    Método static que exibe todas as tarefas ainda existentes em um Frame, chamando o método de instância adicionar_tarefa_no_quadro() de cada uma
    """
    @classmethod
    def exibir_todas_as_tarefas(cls):
        for tarefa in cls.quadro_de_tarefas.winfo_children(): # Para cada tarefa contida no quadro atual, limpa o quadro
            tarefa.pack_forget()

        for tarefa in cls.lista_de_tarefas:
            tarefa.adicionar_tarefa_no_quadro()

    """
    Método static que exibe em um Frame apenas as tarefas marcadas para serem feitas hoje
    """
    @classmethod
    def exibir_tarefas_do_dia(cls):
        data_atual = time.localtime() # extrai a data atual

        for tarefa in cls.quadro_de_tarefas.winfo_children():
            tarefa.pack_forget()

        for tarefa in cls.lista_de_tarefas:
            # extrai a data de realização da tarefa e converte para uma struct time
            data_da_tarefa  = time.strptime(tarefa.data_de_realizacao, '%d/%m/%Y')
            if data_atual.tm_mday == data_da_tarefa.tm_mday and data_atual.tm_mon == data_da_tarefa.tm_mon and data_atual.tm_year == data_da_tarefa.tm_year:
                tarefa.adicionar_tarefa_no_quadro()
    
    """
    Método static que exibe em um Frame apenas as tarefas cuja data de realização é igual a uma data informada
    """
    @classmethod
    def exibir_tarefas_por_data_de_entrega(cls, data):
        for tarefa in cls.quadro_de_tarefas.winfo_children():
            tarefa.pack_forget()

        for tarefa in cls.lista_de_tarefas:
            if tarefa.data_de_entrega == data:
                tarefa.adicionar_tarefa_no_quadro()

    """
    Método static que exibe em um Frame apenas as tarfeas de uma matéria específica
    """
    @classmethod
    def exibir_tarefas_por_materia(cls, materia):
        for tarefa in cls.quadro_de_tarefas.winfo_children():
            tarefa.pack_forget()

        for tarefa in cls.lista_de_tarefas:
            if tarefa.materia == materia:
                tarefa.adicionar_tarefa_no_quadro()