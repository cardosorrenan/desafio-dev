from enum import Enum


class TransactionsActions(Enum):
    ENTRADA = 'Entrada'
    SAIDA = 'Saída'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class TransactionsSignals(Enum):
    ENTRADA = '+'
    SAIDA = '-'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
