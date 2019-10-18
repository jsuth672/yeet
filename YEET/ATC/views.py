from django.shortcuts import render, redirect
from .models import Airport, Airline, Runway, Plane, Gate


def airport_index(request):
    return render(request, 'airport/index.html')


def airport_create(request):
    pass


def airport_update(request, airport_id):
    pass


def airport_delete(request, airport_id):
    pass


def airline_index(request):
    pass


def airline_create(request):
    pass


def airline_update(request, airline_id):
    pass


def airline_delete(request, airline_id):
    pass


def runway_index(request):
    pass


def runway_create(request):
    pass


def runway_update(request, runway_id):
    pass


def runway_delete(request, runway_id):
    pass




def gate_index(request):
    pass


def gate_create(request):
    pass


def gate_update(request, gate_id):
    pass


def gate_delete(request, gate_id):
    pass


def plane_index(request):
    pass


def plane_create(request):
    pass


def plane_update(request, plane_id):
    pass


def plane_delete(request, plane_id):
    pass

