from django.shortcuts import render, get_object_or_404,redirect
from .models import Banner, Activity, Realisation, About, Member,Commune, Departement, Zone, Secteur, Comite
from .forms import MemberRegistrationForm, ContactForm,MemberContributionForm,MemberRegistrationForm,DelegueRegistrationForm
from django.views import View
from django.contrib import messages
from django.http import JsonResponse



def home(request):
    bans = Banner.objects.all()
    acts = Activity.objects.all().order_by('-id')[:6]
    reals = Realisation.objects.all()

    context= {
        'bans':bans,
        'acts':acts,
        'reals':reals,
       

    }
    return render(request, 'app/index.html', context)

def about(request):
    about = About.objects.all().order_by('-id')[:1]
    context = {
        'about':about
    }

    return render(request, 'app/about.html', context)

class MemberRegistrationView(View):
    template_name = 'app/member.html'
    def get_context_data(self, **kwargs):
        context = {}
        context['communes'] = Commune.objects.all()
        context['departements'] = Departement.objects.all()
        context['zones'] = Zone.objects.all()
        context['secteurs'] = Secteur.objects.all()
        context['comites'] = Comite.objects.all()
        return context
    
    @staticmethod
    def get_departements(request):
        commune_id = request.GET.get('commune_id')
        departements = Departement.objects.filter(commune_id=commune_id)
        data = {'departements': list(departements.values('id', 'nom_dept'))}
        return JsonResponse(data)

    def get(self, request):
        form = MemberRegistrationForm()
        return render(request, self.template_name, self.get_context_data())

    def post(self, request):
        form = MemberRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Félicitations, vous êtes inscrit comme nouveau membre de l'UJ-RHDP ")
        else:
            messages.warning(request, "Les données entrées sont invalides")
        
        return render(request, self.template_name, self.get_context_data())

def all(request):
    Activites = Activity.objects.all()

    context = {
        'activites':Activites
    }

    return render(request, 'app/all_activity.html', context)


def detail(request, pk):
    activite = get_object_or_404(Activity, pk=pk)
    context = {
        'activite': activite
    }
    return render(request, 'app/detail_activity.html', context)

class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'app/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Merci pour votre message, nous prenons note du message.")
        else:
            messages.warning(request, "Veuillez remplir tous les champs.")

        return render(request, 'app/contact.html', {'form': form})


def add_contribution(request):
    if request.method == 'POST':
        form = MemberContributionForm(request.POST)
        if form.is_valid():
            nom_membre = form.cleaned_data['nom_membre']
            mail = form.cleaned_data['mail']
            sujet = form.cleaned_data['sujet']
            text = form.cleaned_data['text']
    else:
        form = MemberContributionForm()
    
    return render(request, 'app/contribution.html', {'form': form})


def load_departements(request):
    commune_id = request.GET.get('commune_id') 
    departements = Departement.objects.filter(com_id=commune_id).values('id', 'nom_dept')
    return JsonResponse(list(departements), safe=False)

def load_zones(request):
    departement_id = request.GET.get(' departement_id')
    zones = Zone.objects.filter(departement_id=departement_id).values('id', 'nom_zone')
    return JsonResponse(list(zones), safe=False)

def load_secteurs(request):
    zone_id = request.GET.get('zone_id')
    secteurs = Secteur.objects.filter(zone_id=zone_id).values('id', 'nom_secteur')
    return JsonResponse(list(secteurs), safe=False) 
def load_comites(request):
    secteur_id = request.GET.get('secteur_id')
    comites = Comite.objects.filter(secteur_id=secteur_id).values('id', 'nom_comite') 
    return JsonResponse(list(comites), safe=False)

class DelegueRegistrationView(View):
    def get(self, request):
        form=DelegueRegistrationForm()
        return render(request, 'app/delegue-registration.html', locals())

    def post(self, request):
        form = DelegueRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User register succesfull" )
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'app/delegue-registration.html', locals())




def logout_view(request):
    logout(request)
    return redirect("login")

def profile(request):
    user=request.user
