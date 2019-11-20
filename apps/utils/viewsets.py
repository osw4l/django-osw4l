from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from apps.utils.shortcuts import get_object_or_none
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from collections import OrderedDict
from rest_framework import filters


class CustomPagination(PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('current_page', self.page.number),
            ('pages', self.page.paginator.num_pages),
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))

