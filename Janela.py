from abc import ABC, abstractmethod
from tkinter import *

class Janela(ABC):
    def __init__(self):
        self.janela = self.criar_janela()

    @abstractmethod
    def criar_janela(self):
        pass