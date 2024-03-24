from django.shortcuts import render

def about(request):
    return render(request, 'pages/about.html')

def shipping_policy(request):
    return render(request, 'pages/shipping_policy.html')

def faq(request):
    return render(request, 'pages/faq.html')