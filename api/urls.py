from django.urls import path
from .views import PokemonCRUDView
# (
#                     RetrievePokemonView, 
#                     CreatePokemonView,
#                     UpdatePokemonView
#                     )


urlpatterns = [
    path('pokemon/', PokemonBasicCRUDView.as_view()),
    path('pokemon/<str:poke_number>/', PokemonBasicCRUDView.as_view()),
    # path('pokemon/types/<str:type>/', PokemonBasicCRUDView.as_view()),
    # path('update_pokemon/<str:poke_number>', UpdatePokemonView.as_view()),

]
