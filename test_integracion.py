from unittest.mock import MagicMock, patch

from facturacion import calcular_total_factura


def test_integracion_calculo_factura_con_api_simulada():
    mock_response = MagicMock()
    mock_response.json.return_value = {"rates": {"PEN": 3.75}}

    with patch("facturacion.requests.get", return_value=mock_response):
        resultado = calcular_total_factura(200.0, aplicar_descuento=False)
        assert resultado == 750.00


def test_integracion_calculo_factura_con_descuento():
    mock_response = MagicMock()
    mock_response.json.return_value = {"rates": {"PEN": 3.75}}

    with patch("facturacion.requests.get", return_value=mock_response):
        resultado = calcular_total_factura(200.0, aplicar_descuento=True)
        assert resultado == 675.00