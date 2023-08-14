import requests
from randommer import Randommer
randomer=Randommer()


class Misc(Randommer):
    def __init__(self,api_key)  :
        self.api_key=api_key
    def get_cultures(self) -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of cultures
        '''
        base_url='https://randommer.io'
        url=base_url+"/Misc/Cultures/"
        heardes={
            "X-Api-Key":self.api_key
        }
        response=requests.get(url,headers=heardes)
        if response.status_code==200:
            data = response.json()
        else:
            data = {"error":"bad response"}
        return data
    
    def get_random_address(self,number: int, culture='en') -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key
            number (str): number
            culture (str): culture

        Returns:
            list: random address
        '''
        base_url='https://randommer.io'
        url=base_url+"/Misc/Random-Address"
        heardes={
            "X-Api-Key":self.api_key
        }
        payload={
            "number":number
        }
        response=requests.get(url,params=payload,headers=heardes)
        if response.status_code==200:
            data = response.json()
        else:
            data = {"error":"bad response"}
        return data
key="f1ab06cd2da14928a4f4299e85162d76"
misc=Misc(key)
print(misc.get_random_address(1))