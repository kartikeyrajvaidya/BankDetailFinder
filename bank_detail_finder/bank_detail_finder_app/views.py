from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import (LoginRequiredMixin)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.decorators import api_view

import json
from .models import Banks, Branches
from .serializers import BanksSerializer, BranchesSerializer


class AppHome(LoginRequiredMixin,TemplateView):
    template_name = 'bank_detail_finder_app/bank_detail_finder_app_home.html'


class BranchView(APIView):

    def get(self, request, ifsc_code):

        """ GET - get details of a brank branch by IFSC code"""

        response_dict = {}

        branch = Branches.objects.filter(ifsc=ifsc_code).first()
        if branch is None:
            response_dict["message"] = "no branch with this ifsc code found"
            return Response(response_dict, status=HTTP_404_NOT_FOUND)

        branch_serialized = BranchesSerializer(branch).data
        return Response(branch_serialized)


class BranchListView(APIView):

    def get(self, request):

        """ GET - get all branches of a BANK in a CITY """

        response_dict = {}
        city = request.GET.get("city", None)
        bank_name = request.GET.get("bank_name", None)

        bank = Banks.objects.filter(name=bank_name.upper()).first()
        if bank is None:
            response_dict["message"] = "Bank with given bank_name does not exist"
            return Response(response_dict, status=HTTP_422_UNPROCESSABLE_ENTITY)

        branches = Branches.objects.filter(city=city.upper(), bank=bank)

        if len(branches) < 1:
            response_dict["message"] = "no branch of {} exists in {}".format(bank_name, city)
            return Response(response_dict, status=HTTP_404_NOT_FOUND)

        branches_serialized = BranchesSerializer(branches, many=True).data
        return Response(branches_serialized)



@api_view(["GET"])
def getbanks(request):
    banks = Banks.objects.filter(name__icontains=request.GET.get("term", ""))[:8]
    bank_name_list = []
    for bank in banks:
        bank_name_list.append(bank.name)

    return HttpResponse(json.dumps(bank_name_list))



@api_view(["GET"])
def getbranch(request):
    branches = Branches.objects.filter(city__icontains=request.GET.get("term", ""))[:1]
    branch_city_list = []
    for branch in branches:
        branch_city_list.append(branch.city)

    return HttpResponse(json.dumps(branch_city_list))
