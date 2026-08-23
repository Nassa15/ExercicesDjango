from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
        related_name='produits'
    )

    def __str__(self):
        return self.nom


class Commande(models.Model):
    produit = models.ForeignKey(
        Produit,
        on_delete=models.CASCADE,
        related_name='commandes'
    )
    quantite = models.PositiveIntegerField(default=1)
    date_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande #{self.id} - {self.produit.nom} x{self.quantite}"