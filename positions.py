from endpoints import Endpoints


class Security:
    def __init__(self, security_id, name, symbol, currency, exchange, description, long_description,
                 is_fractional_allowed, is_short_allowed):
        self.id = security_id
        self.name = name
        self.symbol = symbol
        self.currency = currency
        self.exchange = exchange
        self.description = description
        self.long_description = long_description
        self.is_fractional_allowed = is_fractional_allowed
        self.is_short_allowed = is_short_allowed


def get_holdings(client):
    endpoint = Endpoints.user_portfolio
    response = client.make_request(endpoint=endpoint)
    json_response = response.json()
    securities = ''
