from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from models.Tarefa import Tarefa
from UI.Janela import Janela

class JanelaCriarTarefa(Janela):
    def __init__(self):
        super().__init__()
        self.criar_campos_de_entrada()

    """
    Cria e abre a janela como uma toplevel
    """
    def criar_janela(self):
        # Cria essa janela como TopLevel, pois ela é secundária
        janela = Toplevel()
        janela.title('Registrar Tarefa')
        janela.geometry('500x400')
        janela.resizable(True, True)

        titulo = Label(janela, text='Registre uma nova tarefa:', font=('Arial', 14))
        titulo.grid(column=0, row=0, padx=5, pady=5, sticky=W)
        separador = ttk.Separator(janela, orient=HORIZONTAL)
        separador.grid(column=0, row=1, columnspan=4, padx=5, pady=5, sticky=EW)

        return janela
    
    """
    Cria os campos de entrada de informações para registro de tarefa
    """
    def criar_campos_de_entrada(self):
        # ! Os campos de entrada foram criados como atributos de instância para que seus conteúdos possam ser resgatados diretamente em outras partes da classe sem a necessidade de passagem por argumento de função
        # cria o input de matéria
        label_materia = Label(self.janela, text='Matéria: ', font=('Arial', 12)).grid(column=0, row=2, padx=5, pady=5, sticky=W)
        self.input_materia = ttk.Combobox(self.janela)
        self.input_materia['values'] = Tarefa.materias
        self.input_materia.grid(column=1, row=2, padx=5, pady=5, sticky=W)

        # cria o input da data de entrega
        label_data_de_entrega = Label(self.janela, text='Data de entrega: ', font=('Arial', 12)).grid(column=0, row=3, padx=5, pady=5, sticky=W)
        self.input_data_de_entrega = DateEntry(self.janela, date_pattern='dd/mm/yyyy')
        self.input_data_de_entrega.grid(column=1, row=3, padx=5, pady=5, sticky=W)

        # cria o input da descrição
        label_descricao = Label(self.janela, text='Descrição: ', font=('Arial', 12)).grid(column=0, row=4, padx=5, pady=5, sticky=W)
        self.input_descricao = Entry(self.janela)
        self.input_descricao.grid(column=1, row=4, padx=5, pady=5, sticky=EW)

        # cria o input do valor
        label_valor = Label(self.janela, text='Valor (pontos): ', font=('Arial', 12)).grid(column=0, row=5, padx=5, pady=5, sticky=W)
        self.input_valor = ttk.Spinbox(self.janela, from_=0.0, to=10.0)
        self.input_valor.grid(column=1, row=5, padx=5, pady=5, sticky=W)

        # cria o input do tipo
        self.input_tipo = StringVar()
        label_tipo = Label(self.janela, text='Tipo: ', font=('Arial', 12)).grid(column=0, row=6, padx=5, pady=5, sticky=W)
        button_t1 = ttk.Radiobutton(self.janela, text='T1', variable=self.input_tipo, value='T1').grid(column=1, row=6, padx=5, pady=5, sticky=E)
        button_t2 = ttk.Radiobutton(self.janela, text='T2', variable=self.input_tipo, value='T2').grid(column=2, row=6, padx=5, pady=5, sticky=W)
        button_t3 = ttk.Radiobutton(self.janela, text='T3', variable=self.input_tipo, value='T3').grid(column=3, row=6, padx=5, pady=5, sticky=W)

        # cria o input da data de realização
        label_data_de_realizacao = Label(self.janela, text='Data para ser feita: ', font=('Arial', 12)).grid(column=0, row=7, padx=5, pady=5, sticky=W)
        self.input_data_de_realizacao = DateEntry(self.janela, date_pattern='dd/mm/yyyy')
        self.input_data_de_realizacao.grid(column=1, row=7, padx=5, pady=5, sticky=W)

        # cria o botão que irá registrar a tarefa
        botao_registrar_tarefa = Button(self.janela, text='Registrar tarefa', command=self.registrar_tarefa)
        botao_registrar_tarefa.grid(column=1, row=8, padx=5, pady=5, sticky=E)

    """
    Método chamado ao clicar no botão de registrar tarefa, resgata as informações dos campos de entrada e passa para o construtor da tarefa nova
    """
    def registrar_tarefa(self):
        materia = self.input_materia.get()
        data_de_entrega = self.input_data_de_entrega.get()
        descricao = self.input_descricao.get()
        valor = self.input_valor.get()
        tipo = self.input_tipo.get()
        data_de_realizacao = self.input_data_de_realizacao.get()

        Tarefa.quadro_de_tarefas = self.janela
        nova_tarefa = Tarefa(materia, data_de_entrega, descricao, valor, tipo, data_de_realizacao)
