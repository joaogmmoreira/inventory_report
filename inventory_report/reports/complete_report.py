from inventory_report.reports.simple_report import SimpleReport
# from collections import Counter


class CompleteReport(SimpleReport):

    @classmethod
    def generate(self, data):
        simple_report = super().generate(data)
        companies = {}
        for company in data:
            if company["nome_da_empresa"] in companies:
                companies[company["nome_da_empresa"]] += 1
            else:
                companies[company["nome_da_empresa"]] = 1

        companies_list = ""
        for company, quantity in companies.items():
            companies_list += f"- {company}: {quantity}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n{companies_list}"
        )
