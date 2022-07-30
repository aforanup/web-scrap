from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000
    page_query_param = "page"

    def get_paginated_response(self, data, message="Successfully fetched"):
        next_page = None if not self.page.has_next() else self.page.next_page_number()
        previous_page = (
            None if not self.page.has_previous() else self.page.previous_page_number()
        )

        return Response(
            {
                "message": message,
                "next": next_page,
                "previous": previous_page,
                "count": self.page.paginator.count,
                "data": data,
            }
        )
