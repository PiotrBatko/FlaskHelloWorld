import json


def test_getting_text(client):
    response = client.post(
        '/api',
        json={
            'jsonrpc': '2.0',
            'method': 'get_text',
            'id': 1,
        }
    )

    assert json.loads(response.text)['result'] == 'Lorem ipsum dolor sit amet'
