from django.contrib import admin

from .models import Banner, Activity, Realisation, About, Commune, Departement, Zone, Secteur, Comite, Member,Contact,Contribution

@admin.register(Banner)

class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'ban_image','title']

@admin.register(Activity)

class ActivityModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'lieu',  'date', 'description', 'image']

@admin.register(Realisation)

class RealisationModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','date','image']

@admin.register(About)

class AboutModelAdmin(admin.ModelAdmin):
    list_display= ['id', 'titre1', 'desc1', 'titre2', 'desc2', 'image']

@admin.register(Commune)
class CommuneModelAdmin(admin.ModelAdmin):
    list_display= ['id', 'nom_com']

@admin.register(Departement)
class DepartementModelAdmin(admin.ModelAdmin):
    list_display=['id', 'nom_dept', 'com']

@admin.register(Zone)
class ZoneModelAdmin(admin.ModelAdmin):
    list_display=['id', 'nom_zone', 'commune', 'departement']

@admin.register(Secteur)
class SecteurModelAdmin(admin.ModelAdmin):
    list_display=['id', 'nom_secteur', 'commune', 'departement', 'zone']

@admin.register(Comite)

class ComiteModelAdmin(admin.ModelAdmin):
    list_display=['id', 'nom_comite', 'commune', 'departement', 'zone', 'secteur']

@admin.register(Member)

class MemberModelAdmin(admin.ModelAdmin):
    list_display=['id','nom_membre', 'prenom_membre', 'date_of_birth', 'num_cni', 'num_cei', 'lieu_de_vote', 'profession', 'post_parti', 'commune', 'departement', 'zone', 'secteur', 'comite', 'image']

@admin.register(Contact)

class ContactModelAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'mail', 'text']

@admin.register(Contribution)
class ContributionModelAdmin(admin.ModelAdmin):
    list_display=['nom_membre', 'mail', 'member']

    def nom_membre(self, obj):
        return obj.member.nom_membre

    def mail(self, obj):
        return obj.member.mail
