from django.test import TestCase
from api.models import *
# Create your tests here.


class PokemonModelTest(TestCase):
    def setUp(self):
        poke_info = PokeInfo.objects.create(
                            poke_number="001",
                            poke_name = "Bulbasaur"
                            )
        poke_info.types.create(poke_type="Grass")
        poke_info.types.create(poke_type="Poison")

        poke_info = PokeInfo.objects.create(
                            poke_number="002",
                            poke_name = "Ivysaur"
                            )
        poke_info.types.create(poke_type="Grass")
        poke_info.types.create(poke_type="Poison")

        poke_info = PokeInfo.objects.create(
                            poke_number="003",
                            poke_name = "Venusaur"
                            )
        poke_info.types.create(poke_type="Grass")
        poke_info.types.create(poke_type="Poison")

        poke_evo = PokeInfo.objects.get(poke_number="001")
        poke_evo.evos.create(poke_evo="002")
        poke_evo.evos.create(poke_evo="003")

        poke_evo = PokeInfo.objects.get(poke_number="002")
        poke_evo.evos.create(poke_evo="003")
    
    def test_pokemon_data(self):
        data = PokeInfo.objects.all()
        self.assertTrue(len(data))