from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import globalConfig



# Create your views here.
def startPage(request):
    return HttpResponse("Hello, world. You're at the home index.")

def index(request):
    configTable = globalConfig.objects.all()
    if configTable:
        config = configTable[0]
    else:
        config=[]
    #all_product_list = Product.objects.all()
    template = loader.get_template('home/index.html')
    context = {
        #'all_product_list': all_product_list,
        'config': config,
    }
    return HttpResponse(template.render(context, request))


def contact(request):
    configTable = globalConfig.objects.all()
    if configTable:
        config = configTable[0]
    else:
        config=[]
    #all_product_list = Product.objects.all()
    template = loader.get_template('home/pages/contact-us.html')
    context = {
        #'all_product_list': all_product_list,
        'config': config,
    }
    return HttpResponse(template.render(context, request))


def about(request):
    configTable = globalConfig.objects.all()
    if configTable:
        config = configTable[0]
    else:
        config=[]
    template = loader.get_template('home/pages/about-us.html')
    context = {
        'config': config,
    }
    return HttpResponse(template.render(context, request))


def author(request):
    configTable = globalConfig.objects.all()
    if configTable:
        config = configTable[0]
    else:
        config=[]
    template = loader.get_template('home/pages/author.html')
    context = {
        'config': config,
    }
    return HttpResponse(template.render(context, request))


def faq(request):
    configTable = globalConfig.objects.all()
    if configTable:
        config = configTable[0]
    else:
        config=[]
    template = loader.get_template('home/pages/faq.html')
    context = {
        'config': config,
    }
    return HttpResponse(template.render(context, request))

def pricing(request):
    configTable = globalConfig.objects.all()
    if configTable:
        config = configTable[0]
    else:
        config=[]
    template = loader.get_template('home/pages/pricing.html')
    context = {
        'config': config,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    configTable = globalConfig.objects.all()
    if configTable:
        config = configTable[0]
    else:
        config=[]
    template = loader.get_template('home/pages/login.html')
    context = {
        'config': config,
    }
    return HttpResponse(template.render(context, request))

