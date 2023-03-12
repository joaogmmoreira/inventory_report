from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".json"):
            raise ValueError("Árquivo inválido")
        else:
            with open(path, encoding="utf-8") as file:
                opened_file = json.load(file)
                return opened_file
