import pytest
from domain.cliente import Cliente
from domain.produto import Produto
from domain.pedido import Pedido

# Produto com valor negativo deve lançar `ValueError`

def test_produto_valor_negativo():
    with pytest.raises(ValueError):
        Produto(codigo=1, valor=-5, tipo=1)
# Pedido com `qtd_max_produtos=0` deve lançar `ValueError`

def pedido_quantidade_maxima_0():
    with pytest.raises(ValueError):
        Pedido(cliente=c, qtd_max_produtos=0)
        
# `POST /clientes` com CPF vazio deve retornar status `400`

def test_post_cpf_inexistente(client):
    response = client.post("/clientes", json={"cpf": "", "nome": "Cliente X"})
    assert response.status_code == 400
# `PUT /produtos/{codigo}/valor` deve atualizar o valor e retornar `{"alterou": true}`

def alterar_valor_produtos(client):
    response = client.put(f"/produto/{codigo}/valor", json={"valor": 20})
    assert response.status_code == 200
    assert response.json(){"alterou": true}

# Criar um pedido e buscá-lo pelo código via `GET /lanchonete/pedidos/{cod_pedido}`
def criando_pedido_buscando_codigo():

    #Criando Cliente
    client.post("/clientes", json={"cpf": "12345678910", "nome": "Cliente"})

    #Criando Produto
    client.post("/produtos", json={"codigo": 5, "valor": 10, "tipo": 1, "desconto_percentual": 10})

    r = client.post("/lanchonete/pedidos", json={"cpf": "12345678910", "cod_produto": 5, "qtd_max_produtos": 1})
    assert r.status_code == 200
    cod_pedido = r.json()["codigo"]

    response = client.put(f"/lanchonete/pedidos/{cod_pedido}", json={"cod_pedido": 1})
    assert response.status_code == 200