import requests
from randommer import Randommer


class Phone(Randommer):
    def generate(self, api_key: str, CountryCode: str, Quantity: int) -> list:
        '''get bulk telephone numbers for a country
        Args:
            api_key (str): api key
            CountryCode (str): CountryCode ex: 'uz'
            Quantity (str): Quantity
        Returns:
            list: list of phone numbers
        '''
        headers={ 'X-Api-Key': api_key}
        params={ 'CountryCode':CountryCode, 
                'Quantity':Quantity
            }
        r=requests.get(f'{self.get_url()}Phone/Generate',headers=headers,params=params)
        return r.json()

    
    def get_IMEI(self, api_key: str, Quantity: int) -> list:
        '''get bulk imei
        Args:
            api_key (str): api key
            Quantity (str): Quantity
        Returns:
            list: list of phone numbers
        '''
        headers={'X-Api-Key': api_key}
        params={'Quantity':Quantity}
        r=requests.get(f'{self.get_url()}Phone/IMEI',headers=headers,params=params)
        return r.json()
    
    def is_valid(self, api_key: str, telephone: str, CountryCode: str) -> bool:
        '''get bulk imei
        Args:
            api_key (str): api key
            telephone (str): phone number
            CountryCode (str): CountryCode ex: 'uz'
        Returns:
            bool: is valid
        '''
        headers={'X-Api-Key': api_key}
        params={'telephone':telephone,'CountryCode':CountryCode}
        r=requests.get(f'{self.get_url()}Phone/Validate',headers=headers,params=params)
        return r.json()

    
    def get_countries(self, api_key: str) -> list:
        '''get countries
        Args:
            api_key (str): api key
        Returns:
            list: lsit of countries
        '''
        headers={'X-Api-Key': api_key}
        r=requests.get(f'{self.get_url()}Phone/Countries',headers=headers)
        return r.json()        

ans=Phone()
key = "940a688e878544858234dee258149563"
print(ans.generate(key,'AS','5'))
print(ans.get_IMEI(key ,5))
print(ans.is_valid(key,'+1 684-770-8875','AS'))
print(ans.get_countries(key))