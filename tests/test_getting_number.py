import json


def test_getting_number(client):
    response = client.post(
        '/api',
        json={
            'jsonrpc': '2.0',
            'method': 'get_number',
            'id': 1,
        }
    )

    assert json.loads(response.text)['result'] == 42
