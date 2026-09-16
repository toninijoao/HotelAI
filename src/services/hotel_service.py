"""
Camada de serviço do hotel.

Futuramente concentrará as regras de negócio e integrações com sistemas
externos (API de reservas, banco de dados, etc.), servindo de camada
intermediária entre o agente (LangGraph) e esses sistemas. Nesta versão
os métodos são apenas interfaces preparadas para implementação futura.
"""


class HotelService:
    def get_availability(self, check_in: str, check_out: str, room_type: str = "") -> dict:
        raise NotImplementedError("Integração com sistema de reservas ainda não implementada.")

    def get_prices(self, room_type: str = "") -> dict:
        raise NotImplementedError("Integração com sistema de preços ainda não implementada.")

    def create_reservation(self, reservation_data: dict) -> dict:
        raise NotImplementedError("Criação de reservas ainda não implementada.")
