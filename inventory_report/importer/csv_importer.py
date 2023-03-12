from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".csv"):
            raise ValueError("Árquivo inválido")
        else:
            with open(path, encoding="utf-8") as file:
                opened_file = csv.DictReader(file)
                return list(opened_file)
