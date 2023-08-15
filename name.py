import requests
from randommer import Randommer
randomer=Randommer()

class Name(Randommer):
    def __init__(self,api_key) -> None:
        self.api_key=api_key

    def get_name(self, nameType: str, quantity: int) -> list:
        '''get name

        Args:
            api_key (str): api key
            nameType (str): nameType
            quantity (str): number of names

        Returns:
            list: list of names
        '''
        base_url=randomer.base_url      
        url=base_url+"Name"
        heardes={
            "X-Api-Key":self.api_key
        }
        payload={
            "nameType":nameType,
            "quantity":quantity
        }
        r=requests.get(url,params=payload, headers=heardes)
        return r.json()
    
    def get_name_suggestions(self, startingWords: str) -> list:
        '''get name suggestions

        Args:
            api_key (str): api key
            startingWords (str): startingWords

        Returns:
            list: list of name suggestions
        '''
        base_url=randomer.base_url      
        url=base_url+"Name/Suggestions"
        heardes={
            "X-Api-Key":self.api_key
        }
        payload={
            "startingWords":startingWords
        }
        r=requests.get(url,params=payload, headers=heardes)
        return r.json()
    
    def get_name_cultures(self) -> list:
        '''get available cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of names
        '''
        base_url=randomer.base_url      
        url=base_url+"Name/Cultures"
        heardes={
            "X-Api-Key":self.api_key
        }
        r=requests.get(url, headers=heardes)
        return r.json()
key="2d794c6f46094ceb96bd719c1c26c984"
name=Name(key)
print(name.get_name_cultures())