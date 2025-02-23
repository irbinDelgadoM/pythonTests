import http.client
import os
import unittest
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import pytest
from flask import json

BASE_URL = os.environ.get("BASE_URL", "http://localhost:5000")
DEFAULT_TIMEOUT = 5  # Timeout en segundos


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add_positive_numbers(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "4")

    def test_api_add_positive_number_with_negative_number(self):
        url = f"{BASE_URL}/calc/add/2/-2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "0")

    def test_api_add_negative_number_with_positive_number(self):
        url = f"{BASE_URL}/calc/add/-2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "0")

    def test_api_add_positive_number_with_zero(self):
        url = f"{BASE_URL}/calc/add/1/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "1")

    def test_api_add_zero_with_zero(self):
        url = f"{BASE_URL}/calc/add/0/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "0")

    def test_api_add_positive_number_with_decimal_number(self):
        url = f"{BASE_URL}/calc/add/3/1.5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "4.5")

    def test_api_add_negative_numbers(self):
        url = f"{BASE_URL}/calc/add/-2/-5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "-7")

    def test_api_add_string_with_number(self):
        num1 = "2"
        num2 = 2
        url = f"{BASE_URL}/calc/add/\"{num1}\"/{num2}"
        try:
            # Intentar abrir la URL
            urlopen(url, timeout=DEFAULT_TIMEOUT)

            # Si el servidor no devuelve error, marcar el test como fallido
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")

        except HTTPError as e:
            # Verificar que el código de respuesta es 400 Bad Request
            self.assertEqual(e.code, http.client.BAD_REQUEST,
                             f"Se esperaba un error 400 Bad Request en la solicitud a {url}")

    def test_api_add_number_with_string(self):
        num1 = 2
        num2 = "2"
        url = f"{BASE_URL}/calc/add/{num1}/\"{num2}\""
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST,
                             f"Se esperaba un error 400 Bad Request en la solicitud a {url}")

    def test_api_add_strings(self):
        num1 = "2"
        num2 = "2"
        url = f"{BASE_URL}/calc/add/\"{num1}\"/\"{num2}\""
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST,
                             f"Se esperaba un error 400 Bad Request en la solicitud a {url}")

    def test_api_add_empty_string_with_number(self):
        num1 = ""
        num2 = 2
        url = f"{BASE_URL}/calc/add/{num1}/{num2}"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.NOT_FOUND,
                             f"Se esperaba un error 404 Not Found en la solicitud a {url}")

    def test_api_add_number_with_empty_parameter(self):
        url = f"{BASE_URL}/calc/add/2/"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.NOT_FOUND,
                             f"Se esperaba un error 404 Not Found en la solicitud a {url}")

    def test_api_add_empty_strings(self):
        url = f"{BASE_URL}/calc/add//"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.NOT_FOUND,
                             f"Se esperaba un error 404 Not Found en la solicitud a {url}")

    def test_api_add_empty_string_with_string(self):
        num2 = "2"
        url = f"{BASE_URL}/calc/add//\"{num2}\""
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.NOT_FOUND,
                             f"Se esperaba un error 404 Not Found en la solicitud a {url}")

    def test_api_subtract_positive_numbers(self):
        url = f"{BASE_URL}/calc/substract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "2")

    def test_api_subtract_identical_numbers(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "0")

    def test_api_subtract_positive_number_with_negative_number(self):
        url = f"{BASE_URL}/calc/substract/2/-2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "4")

    def test_api_subtract_negative_number_with_positive_number(self):
        url = f"{BASE_URL}/calc/substract/-2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "-4")

    def test_api_subtract_negative_numbers(self):
        url = f"{BASE_URL}/calc/substract/-2/-2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "0")

    def test_api_subtract_positive_number_with_zero(self):
        url = f"{BASE_URL}/calc/substract/1/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "1")

    def test_api_subtract_positive_number_with_decimal_number(self):
        url = f"{BASE_URL}/calc/substract/5/3.5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "1.5")

    def test_api_subtract_decimal_number_with_positive_number(self):
        url = f"{BASE_URL}/calc/substract/3.5/5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "-1.5")

    def test_api_subtract_zero_with_positive_number(self):
        url = f"{BASE_URL}/calc/substract/0/1"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "-1")

    def test_api_subtract_string_with_number(self):
        num1 = "2"
        num2 = 2
        url = f"{BASE_URL}/calc/substract/\"{num1}\"/{num2}"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST,
                             f"Se esperaba un error 400 Bad Request en la solicitud a {url}")

    def test_api_subtract_number_with_string(self):
        num1 = 2
        num2 = "2"
        url = f"{BASE_URL}/calc/substract/{num1}/\"{num2}\""
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST,
                             f"Se esperaba un error 400 Bad Request en la solicitud a {url}")

    def test_api_subtract_strings(self):
        num1 = "2"
        num2 = "2"
        url = f"{BASE_URL}/calc/substract/\"{num1}\"/\"{num2}\""
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST,
                             f"Se esperaba un error 400 Bad Request en la solicitud a {url}")

    def test_api_subtract_empty_parameter_with_number(self):
        num2 = 2
        url = f"{BASE_URL}/calc/substract//{num2}"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.NOT_FOUND,
                             f"Se esperaba un error 404 Not Found en la solicitud a {url}")

    def test_api_subtract_string_with_empty_parameter(self):
        num1 = "2"
        url = f"{BASE_URL}/calc/substract/{num1}/"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.NOT_FOUND,
                             f"Se esperaba un error 404 Not Found en la solicitud a {url}")

    def test_api_subtract_empty_parameters(self):
        url = f"{BASE_URL}/calc/substract//"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.NOT_FOUND,
                             f"Se esperaba un error 404 Not Found en la solicitud a {url}")

    def test_api_multiply_positive_numbers(self):
        url = f"{BASE_URL}/calc/multiply/4/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "12")

    def test_api_multiply_positive_number_with_zero(self):
        url = f"{BASE_URL}/calc/multiply/4/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "0")

    def test_api_multiply_zero_with_decimal_number(self):
        url = f"{BASE_URL}/calc/multiply/0/1.5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "0.0")

    def test_api_multiply_decimal_numbers(self):
        url = f"{BASE_URL}/calc/multiply/4.25/3.15"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "13.3875")

    def test_api_multiply_zero_with_zero(self):
        url = f"{BASE_URL}/calc/multiply/0/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "0")

    def test_api_multiply_positive_number_with_one(self):
        url = f"{BASE_URL}/calc/multiply/4/1"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "4")

    def test_api_multiply_positive_number_with_decimal_number(self):
        url = f"{BASE_URL}/calc/multiply/1/3.5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "3.5")

    def test_api_multiply_one_with_one(self):
        url = f"{BASE_URL}/calc/multiply/1/1"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "1")

    def test_api_multiply_negative_number_with_positive_number(self):
        url = f"{BASE_URL}/calc/multiply/-4/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "-12")

    def test_api_multiply_positive_number_with_negative_number(self):
        url = f"{BASE_URL}/calc/multiply/4/-3.1"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "-12.4")

    def test_api_multiply_negative_decimal_numbers(self):
        url = f"{BASE_URL}/calc/multiply/-4.25/-3.1"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "13.175")

    def test_api_multiply_string_parameter_with_number(self):
        num1 = "2"
        num2 = 2
        url = f"{BASE_URL}/calc/multiply/\"{num1}\"/{num2}"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST,
                             f"Se esperaba un error 400 Bad Request en la solicitud a {url}")

    def test_api_multiply_number_with_string_parameter(self):
        num1 = 2
        num2 = "2"
        url = f"{BASE_URL}/calc/multiply/{num1}/\"{num2}\""
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST,
                             f"Se esperaba un error 400 Bad Request en la solicitud a {url}")

    def test_api_multiply_string_parameters(self):
        num1 = "2"
        num2 = "2"
        url = f"{BASE_URL}/calc/multiply/\"{num1}\"/\"{num2}\""
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST,
                             f"Se esperaba un error 400 Bad Request en la solicitud a {url}")

    def test_api_multiply_empty_parameter_with_number(self):
        num2 = 2
        url = f"{BASE_URL}/calc/multiply//{num2}"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.NOT_FOUND,
                             f"Se esperaba un error 404 Not Found en la solicitud a {url}")

    def test_api_multiply_number_with_empty_parameter(self):
        num1 = 2
        url = f"{BASE_URL}/calc/multiply/{num1}/"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.NOT_FOUND,
                             f"Se esperaba un error 404 Not Found en la solicitud a {url}")

    def test_api_multiply_empty_parameters(self):
        url = f"{BASE_URL}/calc/substract//"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.NOT_FOUND,
                             f"Se esperaba un error 404 Not Found en la solicitud a {url}")

    def test_api_multiply_string_parameters2(self):
        num1 = "abc"
        num2 = "2"
        url = f"{BASE_URL}/calc/multiply/{num1}/\"{num2}\""
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST,
                             f"Se esperaba un error 400 Bad Request en la solicitud a {url}")

    def test_api_multiply_number_with_string_parameters(self):
        num1 = 2
        num2 = "dcba"
        url = f"{BASE_URL}/calc/multiply/{num1}/{num2}"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST,
                             f"Se esperaba un error 400 Bad Request en la solicitud a {url}")

    def test_api_divide_positive_numbers(self):
        url = f"{BASE_URL}/calc/divide/10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "5.0")

    def test_api_divide_zero_by_positive_number(self):
        url = f"{BASE_URL}/calc/divide/0/5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "0.0")

    def test_api_divide_positive_number_by_one(self):
        url = f"{BASE_URL}/calc/divide/10/1"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "10.0")

    def test_api_divide_negative_number_by_positive_number(self):
        url = f"{BASE_URL}/calc/divide/-10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "-5.0")

    def test_api_divide_positive_number_by_negative_number(self):
        url = f"{BASE_URL}/calc/divide/10/-5.0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "-2.0")

    def test_api_divide_negative_numbers(self):
        url = f"{BASE_URL}/calc/divide/-10.0/-2.0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "5.0")

    def test_api_divide_decimal_numbers(self):
        url = f"{BASE_URL}/calc/divide/7.5/2.5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "3.0")

    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/10/0"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST,
                             f"Se esperaba un error 400 Bad Request en la solicitud a {url}")

    def test_api_divide_string_by_number(self):
        num1 = "2"
        num2 = 2
        url = f"{BASE_URL}/calc/divide/\"{num1}\"/{num2}"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.INTERNAL_SERVER_ERROR,
                             f"Se esperaba un error 500 Internal Server Error en la solicitud a {url}")

    def test_api_divide_number_by_string(self):
        num1 = 2
        num2 = "2"
        url = f"{BASE_URL}/calc/divide/{num1}/\"{num2}\""
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.INTERNAL_SERVER_ERROR,
                             f"Se esperaba un error 500 Internal Server Error en la solicitud a {url}")

    def test_api_divide_strings(self):
        num1 = "2"
        num2 = "2"
        url = f"{BASE_URL}/calc/divide/\"{num1}\"/\"{num2}\""
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.INTERNAL_SERVER_ERROR,
                             f"Se esperaba un error 500 Internal Server Error en la solicitud a {url}")

    def test_api_divide_empty_parameter_by_number(self):
        num2 = 2
        url = f"{BASE_URL}/calc/divide//{num2}"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.NOT_FOUND,
                             f"Se esperaba un error 404 Not Found en la solicitud a {url}")

    def test_api_divide_number_by_empty_parameter(self):
        num1 = 2
        url = f"{BASE_URL}/calc/divide/{num1}/"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.NOT_FOUND,
                             f"Se esperaba un error 404 Not Found en la solicitud a {url}")

    def test_api_divide_empty_parameters(self):
        url = f"{BASE_URL}/calc/divide//"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.NOT_FOUND,
                             f"Se esperaba un error 404 Not Found en la solicitud a {url}")

    def test_api_divide_strings2(self):
        num1 = "abc"
        num2 = "2"
        url = f"{BASE_URL}/calc/divide/{num1}/\"{num2}\""
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.INTERNAL_SERVER_ERROR,
                             f"Se esperaba un error 500 Internal Server Error en la solicitud a {url}")

    def test_api_divide_number_by_string2(self):
        num1 = 2
        num2 = "dcba"
        url = f"{BASE_URL}/calc/divide/{num1}/{num2}"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.INTERNAL_SERVER_ERROR,
                             f"Se esperaba un error 500 Internal Server Error en la solicitud a {url}")

    def test_api_divide_strings3(self):
        num1 = "abcd"
        num2 = "dcba"
        url = f"{BASE_URL}/calc/divide/{num1}/{num2}"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.INTERNAL_SERVER_ERROR,
                             f"Se esperaba un error 500 Internal Server Error en la solicitud a {url}")

    def test_api_power_positive_numbers(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "8")

    def test_api_power_decimal_number_to_number(self):
        url = f"{BASE_URL}/calc/power/2.3/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "12.166999999999998")

    def test_api_power_positive_number_to_zero(self):
        url = f"{BASE_URL}/calc/power/5/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "1")

    def test_api_power_zero_to_positive_number(self):
        url = f"{BASE_URL}/calc/power/0/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "0")

    def test_api_power_zero_to_zero(self):
        url = f"{BASE_URL}/calc/power/0/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "1")

    def test_api_power_negative_number_to_positive_number(self):
        url = f"{BASE_URL}/calc/power/-2.3/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "-12.166999999999998")

    def test_api_power_positive_number_to_negative_number(self):
        url = f"{BASE_URL}/calc/power/2.3/-3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "0.08218952905399854")

    def test_api_power_negative_numbers(self):
        url = f"{BASE_URL}/calc/power/-2/-3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "-0.125")

    def test_api_power_positive_number_to_one(self):
        url = f"{BASE_URL}/calc/power/5/1"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "5")

    def test_api_power_positive_number_to_decimal_number(self):
        url = f"{BASE_URL}/calc/power/9/0.5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "3.0")

    def test_api_power_zero_to_negative_decimal(self):
        url = f"{BASE_URL}/calc/power/0/-2"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.INTERNAL_SERVER_ERROR,
                             f"Se esperaba un error 500 Internal Server Error en la solicitud a {url}")

    def test_api_power_string_parameter_to_number(self):
        num1 = "abcd"
        num2 = 3
        url = f"{BASE_URL}/calc/power/{num1}/{num2}"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST,
                             f"Se esperaba un error 400 Bad Request en la solicitud a {url}")

    def test_api_power_number_to_string_parameter(self):
        num1 = 3
        num2 = "dcba"
        url = f"{BASE_URL}/calc/power/{num1}/{num2}"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST,
                             f"Se esperaba un error 400 Bad Request en la solicitud a {url}")

    def test_api_power_strings(self):
        num1 = "abcd"
        num2 = "dcba"
        url = f"{BASE_URL}/calc/power/{num1}/{num2}"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST,
                             f"Se esperaba un error 400 Bad Request en la solicitud a {url}")

    def test_api_power_number_to_empty_parameter(self):
        url = f"{BASE_URL}/calc/power/3/"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.NOT_FOUND,
                             f"Se esperaba un error 404 Not Found en la solicitud a {url}")

    def test_api_power_empty_parameter_to_number(self):
        url = f"{BASE_URL}/calc/power//7"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.NOT_FOUND,
                             f"Se esperaba un error 404 Not Found en la solicitud a {url}")

    def test_api_power_empty_parameters(self):
        url = f"{BASE_URL}/calc/power//"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.NOT_FOUND,
                             f"Se esperaba un error 404 Not Found en la solicitud a {url}")

    def test_api_sqrt_positive_number(self):
        url = f"{BASE_URL}/calc/sqrt/16"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "4.0")

    def test_api_sqrt_decimal_number(self):
        url = f"{BASE_URL}/calc/sqrt/11.34"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "3.3674916480965473")

    def test_api_sqrt_one(self):
        url = f"{BASE_URL}/calc/sqrt/1"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "1.0")

    def test_api_sqrt_zero(self):
        url = f"{BASE_URL}/calc/sqrt/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "0.0")

    def test_api_sqrt_negative_number(self):
        url = f"{BASE_URL}/calc/sqrt/-4"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST,
                             f"Se esperaba un error 400 Bad Request en la solicitud a {url}")

    def test_api_sqrt_empty_parameter(self):
        url = f"{BASE_URL}/calc/sqrt/"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.NOT_FOUND,
                             f"Se esperaba un error 404 Not Found en la solicitud a {url}")

    def test_api_sqrt_string_parameter(self):
        url = f"{BASE_URL}/calc/sqrt/abc"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST,
                             f"Se esperaba un error 400 Bad Request en la solicitud a {url}")

    def test_api_log10_positive_number(self):
        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "2.0")

    def test_api_log10_one(self):
        url = f"{BASE_URL}/calc/log10/1"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "0.0")

    def test_api_log10_negative_number(self):
        url = f"{BASE_URL}/calc/log10/-1"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST,
                             f"Se esperaba un error 400 Bad Request en la solicitud a {url}")

    def test_api_log10_zero(self):
        url = f"{BASE_URL}/calc/log10/0"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST,
                             f"Se esperaba un error 400 Bad Request en la solicitud a {url}")

    def test_api_log10_string_parameter(self):
        url = f"{BASE_URL}/calc/log10/abc"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST,
                             f"Se esperaba un error 400 Bad Request en la solicitud a {url}")

    def test_api_log10_empty_parameter(self):
        url = f"{BASE_URL}/calc/log10/"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"La solicitud a {url} no devolvió un error como se esperaba.")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.NOT_FOUND,
                             f"Se esperaba un error 404 Not Found en la solicitud a {url}")

if __name__ == "__main__":
    unittest.main()
