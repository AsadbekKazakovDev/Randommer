import requests
from randommer import Randommer


class SocialNumber(Randommer):
    def get_SocialNumber(self, api_key: str) -> str:
        '''get SocialNumber

        Args:
            api_key (str): api key

        Returns:
            str: number as str
        '''
        headers = {"X-Api-Key": api_key}
        r = requests.get(f'{self.get_url()}SocialNumber', headers=headers)
        return r.json()
soc = SocialNumber()
key = "940a688e878544858234dee258149563"
print(soc.get_SocialNumber(key))