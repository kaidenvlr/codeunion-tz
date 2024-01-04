"""Pagination file of parser application"""
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class Pagination(PageNumberPagination):
    """Pagination class"""
    page_size = 5
    page_size_query_param = "per_page"
    max_page_size = 10
    page_query_param = "page"

    def get_paginated_response(self, data):
        """Returning edited json response with paginating queryset"""
        page_count = self.page.paginator.count // self.page.paginator.per_page
        if self.page.paginator.count % self.page.paginator.per_page != 0:
            page_count += 1
        return Response({
            'next': bool(self.get_next_link()),
            'previous': bool(self.get_previous_link()),
            'count': self.page.paginator.count,
            'pageCount': page_count,
            'results': data
        })
