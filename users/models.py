from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from localflavor.br.models import BRCPFField, BRPostalCodeField


class User(AbstractUser):
    phone_number = models.CharField(
        verbose_name="Telefone",
        max_length=250,
        default="",
        blank=True,
        null=True,
    )
    cpf = BRCPFField(
        verbose_name="CPF",
        max_length=11,
        default="",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "user"
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self) -> str:
        return f'{self.id} - {self.username}'

    def get_absolute_url(self):
        return reverse("user:user_detail", kwargs={"pk": self.pk})


class Address(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="address_user",
        blank=True,
        null=True,
    )
    street = models.CharField(
        verbose_name="Rua",
        max_length=225,
    )
    number = models.CharField(
        verbose_name="Número",
        max_length=10,
    )
    complement = models.CharField(
        verbose_name="Complemento",
        max_length=70,
        blank=True,
        null=True,
    )
    district = models.CharField(
        verbose_name="Bairro",
        max_length=70,
    )
    postal_code = BRPostalCodeField(
        verbose_name="CEP",
    )

    class Meta:
        db_table = "address"
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    def __str__(self) -> str:
        return f'{self.id} - {self.street}'

    def get_absolute_url(self):
        return reverse("user:address_detail", kwargs={"pk": self.pk})
