from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.services import (
                            pokemon_service,
                            pokemon_filter_service,
                            pokemon_evos_service
                        )

from utils.response import ErrorResponse

import traceback

"""
1.Retrieve a Pokemon by identifier
2.Create a Pokemon
3.Update a Pokemon by identifier
4.Delete a Pokemon by identifier. Note that a deleted Pokemon should not be evolution of other Pokemon.
5.Retrieve Pokemons filter by types
6.Add / Delete evolutions of Pokemon
"""
class PokemonBasicCRUDView(APIView):
    def get(self, request, poke_number):
        try:
            # poke_number = request.query_params.get("poke_number")
            result_json = pokemon_service.get_pokemon_data(poke_number)
            return Response(result_json)
        except Exception as e:
            return ErrorResponse(traceback.format_exc())

    def post(self, request):
        try:
            poke_number = request.data.get("poke_number")
            poke_name = request.data.get("poke_name")
            poke_types = request.data.get("poke_types")
            result_json = pokemon_service.create_pokemon_data(poke_number, poke_name, poke_types)
            return Response(result_json)
        except Exception as e:
            return ErrorResponse(traceback.format_exc())

    def put(self, request, poke_number):
        try:
            poke_name = request.data.get("poke_name")
            poke_types = request.data.get("poke_types")
            result_json = pokemon_service.update_pokemon_data(poke_number, poke_name, poke_types)
            return Response(result_json)
        except Exception as e:
            return ErrorResponse(traceback.format_exc())

    def delete(self, request, poke_number):
        try:
            result_json = pokemon_service.delete_pokemon_data(poke_number)
            return Response(result_json)
        except Exception as e:
            return ErrorResponse(traceback.format_exc())

class PokemonFilterTypeView(APIView):
    def get(self, request, poke_type):
        try:
            result_json = pokemon_filter_service.get_pokemon_data_by_type(poke_type)
            return Response(result_json)
        except Exception as e:
            return ErrorResponse(traceback.format_exc())

class PokemonEvosView(APIView):
    def post(self, request, poke_number):
        try:
            poke_evo_number= request.data.get("poke_evo_number")
            result_json = pokemon_evos_service.create_evos_pokemon_data(poke_number, poke_evo_number)
            return Response(result_json)
        except Exception as e:
            return ErrorResponse(traceback.format_exc())

    def delete(self, request, poke_number, poke_evo_number):
        try:
            result_json = pokemon_evos_service.delete_evos_pokemon_data(poke_number, poke_evo_number)
            return Response(result_json)
        except Exception as e:
            return ErrorResponse(traceback.format_exc())
        
# class CreatePokemonView(APIView):
#     def post(self, request):
#         try:
#             poke_number = request.data.get("poke_number")
#             poke_name = request.data.get("poke_name")
#             poke_types = request.data.get("poke_types")
#             result_json = create_pokemon_service.create_pokemon_data(poke_number, poke_name, poke_types)
#             return Response(result_json)
#         except Exception as e:
#             return ErrorResponse(traceback.format_exc())

# class UpdatePokemonView(APIView):
#     def put(self, request, poke_number):
#         try:
#             poke_name = request.data.get("poke_name")
#             poke_types = request.data.get("poke_types")
#             result_json = update_pokemon_service.update_pokemon_data(poke_number, poke_name, poke_types)
#             return Response(result_json)
#         except Exception as e:
#             return ErrorResponse(traceback.format_exc())
