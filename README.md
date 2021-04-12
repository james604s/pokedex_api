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
  <br />
ex: 127.0.0.1:8000  <br />


# API  <br />
## Retrieve a Pokemon by identifier  <br />

GET /api/pokemon/{poke_number}/ <br />
Get a pokemon by its number.  <br />

## Create a Pokemon  <br />
POST /api/pokemon/ <br />
desc: Create a new pokemon.  <br />

#### Request  <br />
QUERY PARAMETERS  <br />

#### poke_number  <br />
type: string  <br />
desc: pokemon's number.  <br />

#### poke_name  <br />
type: string  <br />
desc: pokemon's name.  <br />

#### poke_types  <br />
type: string  <br />
desc: pokemon's types.  <br />
notice: If this pokemon have muti-type, please use comma(,) and can't use space.  <br />
example: Grass,Poison  <br />


## Update a Pokemon by identifier  <br />
PUT /api/pokemon/{poke_number}/ <br />
desc: Update a pokemon.  <br />

#### Request  <br />
QUERY PARAMETERS  <br />

#### poke_name  <br />
type: string  <br />
desc: pokemon's name.  <br />

#### poke_types  <br />
type: string  <br />
desc: pokemon's name.  <br />
notice: If this pokemon have muti-type, please use comma(,) and can't use space.  <br />
example: Grass,Poison  <br />

## Delete a Pokemon by identifier  <br />
DELETE /api/pokemon/{poke_number}/ <br />
desc: DELETE a pokemon.  <br />
notice: that a deleted Pokemon should not be evolution of other Pokemon.  <br />

## Retrieve Pokemons filter by types  <br />
DELETE /api/types/{poke_type}  <br />
desc: Get pokemons by type pokemon.  <br />

## Add evolutions of Pokemon  <br />
CREATE /api/pokemon/{poke_number}/evos/  <br />
desc: CREATE pokemon's evolutions related data, pokemon need already exist.  <br />

#### Request  <br />
QUERY PARAMETERS  <br />

#### poke_evo_number  <br />
type: string  <br />
desc: pokemon's evolutions' pokemon's number.  <br />

## Delete evolutions of Pokemon
DELETE /api/pokemon/{poke_number}/evos/{poke_evo_number}/  <br />
desc: DELETE pokemon's evolutions data.

