# Snake Views
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Snake

# Snake Data
# snakes = [
#     {
#         'name': 'Black Mamba',
#         'domain': 'Eukaryota',
#         'kingdom': 'Animalia',
#         'Phylum': 'Chordata',
#         'Class': 'Reptilia',
#         'Order': 'Squamata',
#         'Suborder':	'Serpentes',
#         'family': 'Elapidae',
#         'Genus': 'Dendroaspis',
#         'Species': 'D. polylepis',
#         'diet': 'Monkeys',
#         'venom_level': 'Highly Venomous',
#         'native_to': 'sub-Saharan Africa',
#         'natural_habitat': 'savannah, woodland',
#     },

#     {
#         'name': 'Inland Taipan',
#         'domain': 'Eukaryota',
#         'kingdom': 'Animalia',
#         'Phylum': 'Chordata',
#         'Class': 'Reptilia',
#         'Order': 'Squamata',
#         'Suborder':	'Serpentes',
#         'family': 'Elapidae',
#         'Genus': 'Oxyuranus',
#         'Species': 'O. microlepidotus',
#         'diet': 'Sea Otters',
#         'venom_level': 'Most Venomous Snake in the World',
#         'native_to': 'Goyder Lagoon in north-east South Australia',
#         'natural_habitat': 'The black soil plains in the semiarid regions where the Queensland and South Australia borders converge',
#     },

#     {
#         'name': 'Echis (common names: saw-scaled vipers, carpet vipers)',
#         'domain': 'Eukaryota',
#         'kingdom': 'Animalia',
#         'Phylum': 'Chordata',
#         'Class': 'Reptilia',
#         'Order': 'Squamata',
#         'Suborder':	'Serpentes',
#         'family': 'Viperidae',
#         'subfamily': 'Viperinae',
#         'diet': 'Camel Spiders',
#         'venom_level': 'Highly Venomous',
#         'native_to': 'Pakistan, India (in rocky regions of Maharashtra, Rajasthan, Uttar Pradesh, and Punjab) and Sri Lanka, parts of the Middle East, and Africa north of the equator.',
#         'natural_habitat': 'sand, rock, soft soil and in scrublands. It is often found hiding under loose rocks',
#     }
# ]

# Create your views here.

# Home View
def home(request):
    return render(request, 'home.html')

# About View
def about(request):
    return render(request, 'about.html')

# Snake Index
def snakes_index(request):
    snakes = Snake.objects.all()
    return render(request, 'snakes/index.html', {
        'snakes': snakes
    })

# Sanke Detail
def snakes_detail(request, snake_id):
    snake = Snake.objects.get(id=snake_id)
    return render(request, 'snakes/details.html',{
        'snake': snake 
    })

# Snake Create
class SnakeCreate(CreateView):
    model = Snake
    fields = ['name', 'native_to', 'natural_habitat', 'diet', 'venom_level']