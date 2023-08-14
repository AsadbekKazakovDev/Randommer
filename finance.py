import requests
from randommer import Randommer
randoner=Randommer()
class Finance(Randommer):
    def __init__(self,api_key):
        self.api_key=api_key
    def get_crypto_address_types(self) -> list:
        '''get available crypto types

        Args:
            api_key (str): api key

        Returns:
            list: list of types
        '''
        base_url='https://randommer.io'
        url=base_url+"/Finance/CryptoAddress/Types"
        heardes={
            "X-Api-Key":self.api_key
        }
        response=requests.get(url,headers=heardes)

        if response.status_code==200:
            data = response.json()
        else:
            data = {"error":"bad response"}
        return data

    def get_crypto_address(self, crypto_type: str,) -> dict:
        '''get available crypto address

        Args:
            crypto_type (str): crypto type
            api_key (str): api key

        Returns:
            dict: crypto address
        '''
        base_url='https://randommer.io'
        url=base_url+"/Finance/CryptoAddress"
        heardes={
            "X-Api-Key":self.api_key
        }
        payload={
            "cryptoType":crypto_type
        }
        response=requests.get(url,params=payload, headers=heardes)
        if response.status_code==200:
            data = response.json()
        else:
            data = {"error":"bad response"}
        return data


    def get_countries(self,) -> list:
        '''get available countries

        Args:
            api_key (str): api key

        Returns:
            list: crypto address
        '''
        base_url='https://randommer.io'
        url=base_url+"/Finance/Countries"
        heardes={
            "X-Api-Key":self.api_key
        }
        response=requests.get(url,headers=heardes)
        if response.status_code==200:
            data = response.json()
        else:
            data = {"error":"bad response"}
        return data

    def get_iban_by_country_code(self, country_code: str) -> dict:
        '''get available countries

        Args:
            country_code (str): country code
            api_key (str): api key

        Returns:
            dict: idan data
        '''
        base_url='https://randommer.io'
        url=base_url+f"/Finance/Iban/{country_code}"
        heardes={
            "X-Api-Key":self.api_key
        }
        payload={
            "countryCode ":country_code
        }

        response=requests.get(url,params=payload,headers=heardes)
        if response.status_code==200:
            data = response.json()
        else:
            data = {"error":"bad response"}
        return data
key="2d794c6f46094ceb96bd719c1c26c984"
finace=Finance(key)
print(finace.get_iban_by_country_code("SA"))