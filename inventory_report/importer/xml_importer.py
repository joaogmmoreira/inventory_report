from inventory_report.importer.importer import Importer
from xml.etree import ElementTree as ET


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Árquivo inválido")
        else:
            with open(path, encoding="utf-8") as file:
                root = ET.parse(file).getroot()
                data = []

                for record in root:
                    records = {}
                    for child in record:
                        records[child.tag] = child.text
                    data.append(records)
                return data
