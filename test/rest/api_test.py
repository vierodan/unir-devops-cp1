import http.client
import os
import unittest
from urllib.request import urlopen
import json
import urllib.error
import pytest

from urllib.request import urlopen
from flask import json


BASE_URL = "http://localhost:5000"
BASE_URL_MOCK = "http://localhost:9090"
DEFAULT_TIMEOUT = 2  # in secs

@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/1/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "3", "ERROR ADD"
        )

    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "2", "ERROR SUBTRACT"
        )

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "6", "ERROR MULTIPLY"
        )

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/6/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        actual_result = response.read().decode().strip()  # Elimina el carácter de nueva línea
        self.assertEqual(
            actual_result, "3.0", "ERROR DIVIDE"
        )

        url = f"{BASE_URL}/calc/divide/6/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("La división por cero debería lanzar una excepción HTTPError")
        except urllib.error.HTTPError as e: # type: ignore
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )
            response_body = e.read().decode()
            expected_error = {"error": "division by zero"}
            self.assertEqual(
                json.loads(response_body), expected_error, "ERROR DIVIDE BY ZERO"
            )


    def test_api_sqrt(self):
        url = f"{BASE_URL_MOCK}/calc/sqrt/64"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "8", "ERROR SQRT"
        )

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
