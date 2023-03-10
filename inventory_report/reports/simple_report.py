from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(data):

        oldest_date = min(product["data_de_fabricacao"] for product in data)

        today_date = datetime.today().isoformat()
        closest_expiration_date = min(
            product["data_de_validade"] for product in data
            if product["data_de_validade"] > today_date)

        count = Counter(product["nome_da_empresa"] for product in data)

        more_products_company = max(count, key=count.get)

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {more_products_company}"
        )
