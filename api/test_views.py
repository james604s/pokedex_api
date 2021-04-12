from django.test import TestCase, Client
from api.models import *

client = Client()

class APIClientTest(TestCase):
    client = Client()
    poke_info_form = {
        "number": "001", 
        "name": "Bulbasaur", 
        "types": [
            "Grass",
            "Poison" ],
        "evolutions": [ 
            {
                "number": "002", 
                "name": "Ivysaur", 
                "types": [
                "Grass", 
                "Poison"
                ]
            },
            {
                "number": "003", 
                "name": "Venusaur", 
                "types": [
                "Grass", 
                "Poison"
                ]
            }
        ]
    }

    def test_pokemon_basic_retrieve_api(self):
        url = "/api/pokemon/001/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


