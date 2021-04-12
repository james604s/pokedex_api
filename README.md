# pokedex_api
 
# Envs
    pip install -r requirements.txt
    _________________________________
    django==3.1.3
    django-debug-toolbar==3.2
    djangorestframework==3.12.4
    mysqlclient==2.0.3
    numpy==1.20.2
    pandas==1.2.3

# API
### Retrieve a Pokemon by identifier
ex: 127.0.0.1:8000  <br />

GET /api/pokemon/{poke_number}/ <br />
Get a pokemon by its number.  <br />

### Create a Pokemon
POST /api/pokemon/ <br />
Create a new pokemon.  <br />

