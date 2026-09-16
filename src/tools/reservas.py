"""
Ferramenta futura: criação/gestão de reservas.

Ainda não implementada nesta versão. Futuramente deverá se conectar ao
sistema de reservas do hotel através de src/services/hotel_service.py.
"""

from langchain_core.tools import tool

@tool
def criar_reserva(check_in: str, check_out: str, tipo_quarto: str, hospedes: int) -> str:
    """Cria uma pré-reserva/reserva. Ainda não implementado nesta versão."""
    raise NotImplementedError(
        "Criação de reservas ainda não foi implementada."
    )