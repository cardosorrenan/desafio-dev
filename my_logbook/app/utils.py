from enum import Enum
from datetime import datetime   
import pytz
import re


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


class FileCNAB():

    def __init__(self, File):
        self.file = File
        self.filename = File.name
        self.content_type = File.content_type
        self.size = float(File.size)
        self.entries = 0
        self.transactions = []
        self.stores = []


    def clean_field_value(self, value_str):
        value_int = int(value_str)/100
        value_norm = value_int/100
        return value_norm


    def clean_field_datetime(self, date_str, time_str):
        tmz_local = pytz.timezone("America/Fortaleza")
        datetime_naive = datetime.strptime(f"{date_str} {time_str}", "%Y%m%d %H%M%S")
        datetime_local = tmz_local.localize(datetime_naive, is_dst=None)
        datetime_utc = datetime_local.astimezone(pytz.utc)
        return datetime_utc


    def clean_field_string(self, str):
        str = re.sub(' +', ' ', str)
        str = " ".join(str.split())
        return str


    def get_unique_stores(self, stores):
        return [dict(p) for p in set(tuple(i.items()) for i in stores)]


    def load_data(self):
        file_decode = self.file.read().decode("utf-8")
        self.transactions = file_decode.splitlines()
        self.entries = len(self.transactions)
        self.load_stores()
        self.load_transactions()


    def load_stores(self):   
        store_cleaned = list()
        for t in self.transactions:
            store = dict()
            store['owner'] = self.clean_field_string(t[48:62])
            store['name'] = self.clean_field_string(t[62:81])
            store_cleaned.append(store)
        self.stores = self.get_unique_stores(store_cleaned)


    def load_transactions(self):
        transactions_cleaned = list()
        for t in self.transactions:
            transaction = dict()
            transaction['type'] = int(t[0])
            transaction['value'] = self.clean_field_value(t[9:19])
            transaction['cpf'] = t[19:30]
            transaction['card'] = t[30:42]
            transaction['datetime'] = self.clean_field_datetime(t[1:9], t[42:48])
            transaction['store'] = self.clean_field_string(t[62:81])
            transactions_cleaned.append(transaction)
        self.transactions = transactions_cleaned
        

    def file_origin_fields(self):
        return { 'filename': self.filename, 
                 'content_type': self.content_type, 
                 'size': self.size,
                 'entries': self.entries }

    def store_fields(self):
        pass


    def __dict__(self):
        return f'{self.filename} {self.content_type} {self.size}'
        