#001
p001 = PokeInfo.objects.create(
    poke_number = "001", poke_name = "Bulbasaur"
)
p001.types.create(
    poke_type = 'Grass'
)

p001.types.create(
    poke_type = 'Poison'
)

PokeInfo.objects.get(id=1)
PokeInfo.objects.get(id=1).types.create(
    poke_type = 'Grass'
)
PokeInfo.objects.get(id=1).types.create(
    poke_type = 'Poison'
)

p001 = PokeInfo.objects.create(
    poke_number = "001", poke_name = "Bulbasaur"
)

PokeInfo.objects.get(id=1).evos.create(
    poke_evo = "003"
)

#002
PokeInfo.objects.create(
    poke_number = "002", poke_name = "Ivysaur"
)

PokeInfo.objects.get(id=3).types.create(
    poke_type = 'Poison'
)

PokeInfo.objects.get(id=3).types.create(
    poke_type = 'Grass'
)

PokeInfo.objects.get(id=3).evos.create(
    poke_evo = "003"
)
#003
PokeInfo.objects.create(
    poke_number = "003", poke_name = "Venusaur"
)

PokeInfo.objects.get(id=4).types.create(
    poke_type = 'Poison'
)

PokeInfo.objects.get(id=4).types.create(
    poke_type = 'Grass'
)

#004
PokeInfo.objects.create(
    poke_number = "004", poke_name = "Charmander"
)

PokeInfo.objects.get(id=5).types.create(
    poke_type = 'Fire'
)

#
PokeType.objects.filter(poke_type="Fire", poke_number_id=4).delete()



PokeInfo.objects.get(id=1).types.all().values("poke_type")

PokeInfo.objects.filter(id=1)

name = PokeInfo.objects.get(poke_number="001").poke_name
name = PokeInfo.objects.get(poke_number="001").objects.all()
types = PokeInfo.objects.get(poke_number="001").types.all().values("poke_type")
evolutions = list(PokeInfo.objects.get(poke_number="001").evos.all().values("poke_evo"))
PokeInfo.objects.get(poke_number="001").poke_name

list(PokeInfo.objects.filter(poke_number="005").values("poke_name"))[0]['poke_name']
PokeInfo.objects.filter(poke_number="005").values("poke_name")


test = PokeInfo.objects.select_related().all()

for c in test:
    print(c.poke_number)


a = PokeEvo.objects.select_related().filter(pk=1)

PokeEvo.objects.all()

PokeInfo.objects.select_related()

test = PokeEvo.objects.all().first()
test.poke_original.poke_name

test2 = PokeInfo.objects.first()
test2.pokeevo_set.all()

a = PokeInfo.objects.filter(poke_number="008").exists()

PokeInfo.objects.get(poke_number="001")

##select_related
a = PokeType.objects.select_related('poke_original')

PokeInfo.objects.select_related('poke_original')