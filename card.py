import requests
from randommer import Randommer


class Card(Randommer):
    def get_card(self, api_key: str, type=None) -> dict:
        '''get card from randommer
        
        Args:
            api_key (str): api key
            type (str): card type

        Returns:
            dict: card data
        '''
        endpoint = '/api/Card/'
        url = self.get_url() + endpoint

        payload = {
            "type": type
        }
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url=url, params=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
        else:
            data = {"error": "Bad request."}
        
        return data

    def get_card_types(self, api_key: str) -> list:
        '''get cars types from randommer

        Args:
            api_key (str): api key
            
        Returns:
            list: list of types
        '''
        endpoint = '/api/Card/Types/'
        url = self.get_url() + endpoint

        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            data = response.json()
        else:
            data = {"error": "Bad request."}
        
        return data
    


card = Card()
print(card.get_card_types(api_key="2d794c6f46094ceb96bd719c1c26c984"))
card = Card()
print(card.get_card(api_key="2d794c6f46094ceb96bd719c1c26c984"))