from endpoints import Endpoints


class Account:
    def __init__(self, client):
        self.client = client

    def transaction_history(self):
        """
        Returns the transaction history of the current user
        :return: list of dictionaries containing each transaction: amount (float), timestamp, and type (str)
        for bank transfers, there is also a 'status' key with known values of: 'pending'
        type has known values of: 'Promotional Reward', 'Deposit'
        """
        endpoint = Endpoints.transaction_history
        response = self.client.make_request(endpoint=endpoint)
        return response.json()

    def withdrawal_availability(self):
        """
        Returns the availability of funds for withdrawal based on each deposit / bonus
        :return: dictionary containing funds_available (float) and withdrawal_availability (list of dictionaries containing each deposit: amount (float), available_on (YYYY-MM-DD), and reason (str))
        """
        endpoint = Endpoints.withdrawal_info
        response = self.client.make_request(endpoint=endpoint)
        return response.json()

    def funds_available_for_withdrawal(self):
        """
        Returns the total amount of funds currently available for withdrawal
        :return: float
        """
        withdrawal_info = self.withdrawal_availability()
        return withdrawal_info['funds_available']

    def funds_availability(self):
        """
        Returns the availability of funds for withdrawal based on each deposit / bonus
        :return: list of dictionaries containing each deposit: amount (float), available_on (YYYY-MM-DD), and reason (str)
        """
        withdrawal_info = self.withdrawal_availability()
        funds = withdrawal_info['withdrawal_availability']
        return funds
