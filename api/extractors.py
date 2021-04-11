from api.models import *

class PokeExtractors:
    def get_pokemon_by_identifier(self, poke_number):
        """"""
        # name = PokeInfo.objects.get(poke_number=poke_number).poke_name
        name = list(PokeInfo.objects.filter(poke_number=poke_number).values("poke_name"))
        if name:
            types = list(PokeInfo.objects.get(poke_number=poke_number).types.all().values("poke_type"))
            result_json = {
                "number": poke_number,
                "name": name[0]['poke_name'],
                "types": [item['poke_type'] for item in types]
            }
            return result_json
        return 

    def get_pokemon_evolutions_info(self, poke_number):
        poke_info_id = list(PokeInfo.objects.filter(poke_number=poke_number).values("id"))
        if poke_info_id:
            evolutions = list(PokeEvo.objects.filter(poke_original=poke_info_id[0]['id']).values("poke_evo"))
            if evolutions:
                evolutions_list = [item['poke_evo'] for item in evolutions]
                evolutions_info = [self.get_pokemon_by_identifier(item) for item in evolutions_list]
                return evolutions_info
        return []

pokemon_info = PokeExtractors()