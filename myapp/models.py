from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, validators=[MinLengthValidator(limit_value=3, message="Le nom "
                                                                                                     "d'utilisateur "
                                                                                                     "doit comporter "
                                                                                                     "au moins 3 "
                                                                                                     "caractères.")])
    email = models.EmailField(validators=[EmailValidator(message="Veuillez saisir une adresse e-mail valide.")])
    first_name = models.CharField(max_length=50, validators=[MinLengthValidator(limit_value=2, message="Le prénom "
                                                                                                       "doit "
                                                                                                       "comporter au "
                                                                                                       "moins 2 "
                                                                                                       "caractères.")])
    last_name = models.CharField(max_length=50, validators=[MinLengthValidator(limit_value=2, message="Le nom de "
                                                                                                      "famille doit "
                                                                                                      "comporter au "
                                                                                                      "moins 2 "
                                                                                                      "caractères.")])


class Visit(models.Model):
    count = models.IntegerField(default=0)
