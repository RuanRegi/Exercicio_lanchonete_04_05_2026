def test_deve_cancelar_pedido_com_sucesso(client):
    client.post("/clientes", json={"cpf": "11122233344"})

    client.post("/produtos", json={"codigo": 1, "nome": "X-Burger", "preco": 10})

    client.post("/lanchonete/pedidos", json={
        "cpf": "12345678900",
        "produtos": [1]
    })

    response = client.post("/lanchonete/pedidos/1/cancelar")

    assert response.status_code == 200

    data = response.json()

    assert data["ok"] is True
    assert data["mensagem"] == "Pedido cancelado com sucesso"

def test_nao_deve_cancelar_pedido_inexistente(client):
    response = client.post("/lanchonete/pedidos/999/cancelar")

    assert response.status_code == 400

    data = response.json()

    assert data["detail"] == "Pedido não encontrado ou não pode ser cancelado"

def test_nao_deve_cancelar_pedido_finalizado(client):
    client.post("/clientes", json={"cpf": "11122233344"})
    client.post("/produtos", json={"codigo": 1, "nome": "X-Burger", "preco": 10})

    client.post("/lanchonete/pedidos", json={
        "cpf": "12345678900",
        "produtos": [1]
    })

    client.patch("/lanchonete/pedidos/1/finalizar")

    response = client.post("/lanchonete/pedidos/1/cancelar")

    assert response.status_code == 400

def test_deve_listar_pedidos_cancelados(client):
    client.post("/clientes", json={"cpf": "11122233344"})
    client.post("/produtos", json={"codigo": 1, "nome": "X-Burger", "preco": 10})

    client.post("/lanchonete/pedidos", json={
        "cpf": "11122233344",
        "produtos": [1]
    })

    client.post("/lanchonete/pedidos/1/cancelar")

    response = client.get("/lanchonete/pedidos/cancelados")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]["esta_cancelado"] is True

