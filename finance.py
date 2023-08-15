import requests
from randommer import Randommer

class Finance(Randommer):
    def get_crypto_address_types(self, api_key: str) -> list:
        '''get available crypto types

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
        response=requests.get(f'{url}Finance/CryptoAddress/Types',headers=headers)
        if response.status_code == 200:
            data = response.json()
        else:
            data = {"error": "Bad request."}
        
        return data
        
    def get_crypto_address(self, crypto_type: str, api_key: str) -> dict:
        '''get available crypto address

        Args:
            crypto_type (str): crypto type
            api_key (str): api key

        Returns:
            dict: crypto address
        '''
        headers={ 
            "X-Api-key": api_key
        }
        cryptoType={
            'cryptoType' : crypto_type
        }
        url=self.get_url()
        response=requests.get(f'{url}Finance/CryptoAddress',headers=headers , params=cryptoType)
        if response.status_code == 200:
            data = response.json()
        else:
            data = {"error": "Bad request."}
        
        return data

    def get_countries(self, api_key: str) -> list:
        '''get available countries

        Args:
            api_key (str): api key

        Returns:
            list: crypto address
        '''
        headers={ "X-Api-key":api_key }
        url=self.get_url()
        response=requests.get(f'{url}Finance/Countries',headers=headers)
        if response.status_code == 200:
            data = response.json()
        else:
            data = {"error": "Bad request."}
        
        return data

    def get_iban_by_country_code(self, country_code: str, api_key: str) -> dict:
        '''get available countries

        Args:
            country_code (str): country code
            api_key (str): api key

        Returns:
            dict: idan data
        '''
        headers={ "X-Api-key":api_key }
        countrycode={'countrycode': country_code }
        url=self.get_url()
        response=requests.get(f'{url}Finance/Iban/{country_code}',headers=headers,params=countrycode)
        if response.status_code == 200:
            data = response.json()
        else:
            data = {"error": "Bad request."}
        
        return data
        

ans=Finance()
key = "2d794c6f46094ceb96bd719c1c26c984"
print(ans.get_crypto_address_types(key))
print(ans.get_crypto_address('Dash', key))
print(ans.get_countries(key))
print(ans.get_iban_by_country_code('AL', key))