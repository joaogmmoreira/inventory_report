from inventory_report.inventory.product import Product


def test_cria_produto():
    id = 12345
    nome_da_empresa = "ACME Inc."
    nome_produto = "Martelo"
    data_fabricacao = "2022-01-01"
    data_validade = "2023-01-01"
    numero_serie = "ABC123XYZ"
    instrucoes_armazenamento = "Armazenar em local seco e arejado"

    produto = Product(
        id=id,
        nome_da_empresa=nome_da_empresa,
        nome_do_produto=nome_produto,
        data_de_fabricacao=data_fabricacao,
        data_de_validade=data_validade,
        numero_de_serie=numero_serie,
        instrucoes_de_armazenamento=instrucoes_armazenamento
    )

    assert produto.id == id
    assert produto.nome_da_empresa == nome_da_empresa
    assert produto.nome_do_produto == nome_produto
    assert produto.data_de_fabricacao == data_fabricacao
    assert produto.data_de_validade == data_validade
    assert produto.numero_de_serie == numero_serie
    assert produto.instrucoes_de_armazenamento == instrucoes_armazenamento
