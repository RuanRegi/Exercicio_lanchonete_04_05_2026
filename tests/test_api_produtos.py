def alterar_valor_produtos(client):
    response = client.put(f"/produto/{codigo}/valor", json={"valor": 20})
    assert response.status_code == 400
