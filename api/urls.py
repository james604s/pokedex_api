from django.urls import path
from api.views import (
                        PokemonBasicCRUDView, 
                        PokemonFilterTypeView,
                        PokemonEvosView
                        )

urlpatterns = [
    path('pokemon/', PokemonBasicCRUDView.as_view()),
    path('pokemon/<str:poke_number>/', PokemonBasicCRUDView.as_view()),
    path('pokemon/<str:poke_number>/evos/', PokemonEvosView.as_view()),
    path('pokemon/<str:poke_number>/evos/<str:poke_evo_number/', PokemonEvosView.as_view()),
    path('types/<str:poke_type>/', PokemonFilterTypeView.as_view()),
    # path('pokemon/types/<str:type>/', PokemonBasicCRUDView.as_view()),
    # path('update_pokemon/<str:poke_number>', UpdatePokemonView.as_view()),

]
