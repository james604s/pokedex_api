from api.extractors import pokemon_info
from api.models import *

class PokemonService:
    def get_pokemon_data(self, poke_number):
        result_json = pokemon_info.get_pokemon_by_identifier(poke_number)
        evolutions_info = pokemon_info.get_pokemon_evolutions_info(poke_number)
        if result_json:
            result_json.update({"evolutions":evolutions_info})
            return result_json
        return {"message": f"This pokemon number:{poke_number} does not exist."}

    def create_pokemon_data(self, poke_number, poke_name, poke_types):
        if PokeInfo.objects.filter(poke_number=poke_number).exists():
            return {"message": f"This pokemon number:{poke_number} already exist."}
        create_info = PokeInfo.objects.create(poke_number = poke_number, poke_name = poke_name)
        poke_types_list = poke_types.split(",")
        for item in poke_types_list:
            create_info.types.create(poke_type=item)
        result_json = {
                "number": poke_number,
                "name": poke_name,
                "types": poke_types_list
            }
        return result_json

    def update_pokemon_data(self, poke_number, poke_name, poke_types):
        """
        需求
        1. 若無此Pokemon是否需要新增？
        2. 是否需要取出進化的資料？
        3. 若有此Pokemon更新資料是否需要與舊資料傳送比對？
        """
        result_json = pokemon_info.get_pokemon_by_identifier(poke_number)
        if result_json:
            if poke_name:
                #update name
                result_json['name'] = poke_name
                PokeInfo.objects.filter(poke_number=poke_number).update(poke_name=poke_name)
                #update types
                poke_types_list = poke_types.split(",")
                result_json['types'] = poke_types_list
                poke_info = PokeInfo.objects.get(poke_number=poke_number)
                poke_type_id_list = poke_info.types.values("id")
                poke_type_id_list = [item['id'] for item in poke_type_id_list]
                for poke_type_id in poke_type_id_list:
                    PokeType.objects.filter(id=poke_type_id).delete()
                for poke_type in poke_types_list:
                    poke_info.types.create(poke_type=poke_type)
                return result_json
        return {"message": f"This pokemon number:{poke_number} does not exist."}

    def delete_pokemon_data(self, poke_number):
        """
        Note that a deleted Pokemon should not be evolution of other Pokemon.
        """
        if PokeInfo.objects.filter(poke_number=poke_number).exists():
            if PokeEvo.objects.filter(poke_number=poke_number).exists():
                return {"message": f"This pokemon number:{poke_number} is other pokemon's evolution, can not delete."}
            poke_info = PokeInfo.objects.get(poke_number=poke_number)
            PokeType.objects.filter(poke_original_id=poke_info.id).delete()
            poke_info.delete()
            return {"message": f"This pokemon number:{poke_number} is delete."}
        return {"message": f"This pokemon number:{poke_number} does not exist."}

pokemon_service = PokemonService()

class PokemonFilterService:
    def get_pokemon_data_by_type(self):
        return

class PokemonEvosService:
    def create_evos_pokemon_data(self):
        return

    def delete_evos_pokemon_data(self):
        return