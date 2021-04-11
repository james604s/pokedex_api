from django.db import models

# Create your models here.
class PokeInfo(models.Model):
    """blank=有無空白, null=是否為空值"""
    poke_number = models.CharField(max_length=10, blank=True, null=False, unique=True)
    poke_name = models.CharField(max_length=30, blank=True, null=False)

    def __str__(self):
        return f"<number: {self.poke_number}>"

    # class Meta:
    #     # managed = True
    #     db_table = 'poke_info'

class PokeType(models.Model):
    poke_original = models.ForeignKey(PokeInfo, on_delete=models.CASCADE, related_name='types')
    poke_type = models.CharField(max_length=10, blank=True, null=False)
    
    # class Meta:
    #     # managed = True
    #     db_table = 'poke_type'

class PokeEvo(models.Model):
    poke_original = models.ForeignKey(PokeInfo, on_delete=models.CASCADE, related_name='evos')
    poke_evo = models.CharField(max_length=10, blank=True, null=True)

    # class Meta:
    #     # managed = True
    #     db_table = 'poke_evo'

