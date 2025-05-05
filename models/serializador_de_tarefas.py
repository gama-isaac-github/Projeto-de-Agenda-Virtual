import pickle
import os

def salvar_tarefas(lista_de_tarefas, arquivo):
    with open(arquivo, 'wb') as file:
        pickle.dump(lista_de_tarefas, file=file)

def carregar_tarefas(arquivo):
    if os.path.getsize(arquivo) > 0:
        with open(arquivo, 'rb') as file:
            return pickle.load(file=file)
