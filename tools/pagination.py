from rest_framework.pagination import PageNumberPagination


class BZPagination(PageNumberPagination):
    """
    Enable pagination.
    """
    page_size_query_param = "page_size"
    max_page_size = 1024
