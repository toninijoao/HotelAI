"""
Ferramenta futura: consulta de disponibilidade de quartos.

Ainda não implementada nesta versão. Futuramente deverá se conectar ao
sistema de reservas do hotel através de src/services/hotel_service.py.
"""

from langchain_core.tools import tool


@tool
def consultar_disponibilidade(check_in: str, check_out: str, tipo_quarto: str = "") -> str:
    """Consulta a disponibilidade de quartos para um período. Ainda não implementado."""
    raise NotImplementedError(
        "Consulta de disponibilidade ainda não foi implementada nesta versão."
    )
