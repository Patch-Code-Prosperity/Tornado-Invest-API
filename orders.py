from endpoints import Endpoints


def get_orders(client):
    """
    Gets all orders
    :param client:
    :return: is_market_open (bool)
    not_placed_orders (list of something)
    placed_orders (list of order objects)
    order object: includes: execution_status: 'pending'
    """
    endpoint = Endpoints.orders
    response = client.make_request(endpoint=endpoint)
    return response.json()


def place_order(security_id, input_type, type, operation, shares, cash_amount=None, limit_price='', stop_price='', override_closed=False, is_from_optimizer=False, override_warnings=None, platform='ios', client_identifier=None):
    """
    Places an order for a security
    :param cash_amount: optional, required if input_type is dollars
    :param security_id:
    :param input_type: "shares" or "dollars"
    :param type: "market" or "limit"
    :param operation:
    :param shares: int (maybe or float)
    :param limit_price: empty string if type is market else float
    :param stop_price:
    :param override_closed:
    :param is_from_optimizer:
    :param override_warnings:
    :param platform:
    :param client_identifier:
    :return:
    """
    endpoint = Endpoints.place_order
    data = {
        'order': {
            'security_id': security_id,
            'input_type': input_type,
            'type': type,
            'operation': operation,
            'shares': shares,
            'limit_price': limit_price,
            'stop_price': stop_price,
            'is_from_optimizer': is_from_optimizer
        },
        'platform': platform,
        'client_identifier': client_identifier
    }
    if override_warnings:
        data['override_warnings'] = override_warnings
    elif override_closed:
        data['override_warnings'] = ['market_closed']
    else:
        data['override_warnings'] = []
    if input_type == 'dollars':
        data['order']['cash_amount'] = cash_amount
    response = client.make_request(endpoint=endpoint, method='POST', json=data)
