from django.shortcuts import render

# Snake Data
snakes = [
    {
        'name': 'Black Mamba',
        'domain': 'Eukaryota',
        'kingdom': 'Animalia',
        'Phylum': 'Chordata',
        'Class': 'Reptilia',
        'Order': 'Squamata',
        'Suborder':	'Serpentes',
        'family': 'Elapidae',
        'Genus': 'Dendroaspis',
        'Species': 'D. polylepis',
        'venom level': 'Highly Venomous',
        'native to': 'sub-Saharan Africa',
        'natural habitat': 'savannah, woodland'
    },

    {
        'name': 'Inland Taipan',
        'domain': 'Eukaryota',
        'kingdom': 'Animalia',
        'Phylum': 'Chordata',
        'Class': 'Reptilia',
        'Order': 'Squamata',
        'Suborder':	'Serpentes',
        'family': 'Elapidae',
        'Genus': 'Oxyuranus',
        'Species': 'O. microlepidotus',
        'venom level': 'Most Venomous Snake in the World',
        'native to': 'Goyder Lagoon in north-east South Australia',
        'natural habitat': 'The black soil plains in the semiarid regions where the Queensland and South Australia borders converge'
    },

    {
        'name': 'Echis (common names: saw-scaled vipers, carpet vipers)',
        'domain': 'Eukaryota',
        'kingdom': 'Animalia',
        'Phylum': 'Chordata',
        'Class': 'Reptilia',
        'Order': 'Squamata',
        'Suborder':	'Serpentes',
        'family': 'Viperidae',
        'subfamily': 'Viperinae',
        'venom level': 'Highly Venomous',
        'native to': 'Pakistan, India (in rocky regions of Maharashtra, Rajasthan, Uttar Pradesh, and Punjab) and Sri Lanka, parts of the Middle East, and Africa north of the equator.',
        'natural habitat': 'sand, rock, soft soil and in scrublands. It is often found hiding under loose rocks'
    }
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def snakes_index(request):
    return render(request, 'sankes/index.html', {
        'snakes': snakes
    })