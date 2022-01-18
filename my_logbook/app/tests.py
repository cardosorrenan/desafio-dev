from app.utils import FileCNAB

from django.test import TestCase
from django.core.files.base import File
from django.core.files.uploadedfile import SimpleUploadedFile


class UploadFIleModelTests(TestCase):
    data = File(open('./CNAB.txt', 'rb'))
    upload_file = SimpleUploadedFile('./CNAB.txt', data.read())
    cnab_file = FileCNAB(upload_file)
    cnab_file.load_data()


    def test_create_instance(self):
        test = isinstance(self.cnab_file, FileCNAB)
        self.assertIs(test, True)


    def test_get_transactions(self):
        transactions = self.cnab_file.transactions
        test = isinstance(transactions, list) and transactions is not []
        self.assertIs(test, True)

    
    def test_get_stores(self):
        stores = self.cnab_file.stores
        test = isinstance(stores, list) and stores is not []
        self.assertIs(test, True)