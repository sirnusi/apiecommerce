from rest_framework.pagination import PageNumberPagination

class ProductListPagination(PageNumberPagination):
    page_size = 2
    #last_page_strings = 'last'