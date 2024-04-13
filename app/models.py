from django.db import models
from django.contrib.auth.models import User

class Banner(models.Model):
    ban_image = models.ImageField(upload_to="images")
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Activity(models.Model):
    title = models.CharField(max_length=255)
    lieu = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="images")


    def __str__(self):
        return self.title

class Realisation(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title

class About(models.Model):
    titre1 = models.CharField(max_length=255)
    desc1 = models.TextField()
    titre2 = models.CharField(max_length=255)
    desc2 = models.TextField()
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.titre1

class Commune(models.Model):
    nom_com = models.CharField(max_length=255)

    def __str__(self):
        return self.nom_com

class Departement(models.Model):
    nom_dept =models.CharField(max_length=255)
    com = models.ForeignKey(Commune, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_dept

class Zone(models.Model):
    nom_zone = models.CharField(max_length=255)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_zone

class Secteur(models.Model):
    nom_secteur = models.CharField(max_length=255)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_secteur

class Comite(models.Model):
    nom_comite = models.CharField(max_length=255)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_comite

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom_membre = models.CharField(max_length=255)
    prenom_membre = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    mail = models.EmailField()
    num_cni = models.CharField(max_length=150, unique=True)
    num_cei = models.CharField(max_length=150, unique=True)
    lieu_de_vote = models.CharField(max_length=255)
    contact = models.IntegerField(default=0, unique=True)
    profession = models.CharField(max_length=255)
    post_parti = models.CharField(max_length=255)
    image=models.ImageField(upload_to="images")
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE)
    comite = models.OneToOneField(Comite, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_membre

    def clean(self):
        super().clean()
        if self.post_parti not in ['delegue_zone', 'delegue_departemental']:
            raise ValidationError("Le poste spécifié n'est pas autorisé pour cet utilisateur.")

        max_members = 25
        if Member.objects.filter(comite=self.comite).count() >= max_members:
            raise ValidationError("Le comité a atteint le nombre maximum de membres (25).")

class Contribution(models.Model):
    sujet = models.CharField(max_length=150)
    text = models.TextField()
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    

class Contact(models.Model):
    name = models.CharField(max_length=255)
    mail = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.name


class Pv(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)

    def __str__(self):
        return self.titre