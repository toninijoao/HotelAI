"""
Ferramenta futura: consulta de preços de diárias/quartos.

Ainda não implementada nesta versão. Futuramente deverá se conectar ao
sistema de preços do hotel através de src/services/hotel_service.py.
"""

from langchain_core.tools import tool


@tool
def consultar_precos(tipo_quarto: str = "", check_in: str = "", check_out: str = "") -> str:
    """Consulta os preços de um tipo de quarto para um período. Ainda não implementado."""
    raise NotImplementedError(
        "Consulta de preços ainda não foi implementada nesta versão."
    )
