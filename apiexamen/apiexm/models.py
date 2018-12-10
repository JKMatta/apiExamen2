from django.db import models


class Usuario( models.Model ):
    Username = models.CharField( max_length = 255 )
    PassUser = models.CharField( max_length = 255 )
    Nombre = models.CharField( max_length = 255 )
    Apellido = models.CharField( max_length = 255 )
    Email= models.CharField( max_length = 255 )