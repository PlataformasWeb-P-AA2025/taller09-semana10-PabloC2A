from django.db import models

class EquipoFutbol(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)
    username_twitter = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Equipo de Fútbol"
        verbose_name_plural = "Equipos de Fútbol"


class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion_campo = models.CharField(max_length=2, choices=[('PT', 'Portero'), ('DF', 'Defensa'), ('MC', 'Mediocampista'), ('DL', 'Delantero')])
    numero_camiseta = models.PositiveIntegerField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    equipo = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.numero_camiseta})"

    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"


class Campeonato(models.Model):
    nombre_campeonato = models.CharField(max_length=100)
    auspiciante = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_campeonato

    class Meta:
        verbose_name = "Campeonato"
        verbose_name_plural = "Campeonatos"


class CampeonatoEquipos(models.Model):
    año = models.PositiveIntegerField()
    equipo = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('año', 'equipo', 'campeonato')
        verbose_name = "Campeonato Equipos"
        verbose_name_plural = "Campeonato Equipos"

    def __str__(self):
        return f"{self.campeonato} - {self.equipo} ({self.año})"
