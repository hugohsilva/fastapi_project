from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_project.app import app


def test_root_deve_retonrar_ok_e_ola_mundo():
    client = TestClient(app)

    respose = client.get('/')

    assert respose.status_code == HTTPStatus.OK
