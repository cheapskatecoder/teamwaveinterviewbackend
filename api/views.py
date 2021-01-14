from datetime import datetime
import json
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from stackapi import StackAPI

from api.models import Query
from api.serializers import QueryModelSerializer



class QueryModelViewSet(ModelViewSet):
    serializer_class = QueryModelSerializer
    queryset = Query.objects.all()
    permission_classes = [IsAuthenticated, ]


class QueryAPIView(APIView):
    serializer_class = QueryModelSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        site = StackAPI('stackoverflow')
        query_parameters = ['fromdate', 'todate', 'min', 'sort', 'tag', 'page', 'page-size', 'order', 'max']
        query_string = f''

        for key, value in request.data.items():
            if key == 'page-size' and request.data.get('sort') == 'votes' and value and value != "None":
                # set page_size to passed value
                print('passing')
                site.page_size = value
                pass
            elif key == 'page' and request.data.get('votes') and value  and value != "None":
                # set max_pages to passed value
                print('p2')
                site.max_pages = value
                pass
            elif key == 'max' or key == 'min' and value and value != "None":
                if request.data.get('sort') == 'hot' \
                    or request.data.get('sort') == 'week' or request.data.get('sort') == 'month':
                        print('min max')
                        query_string += f'{key}="{value}", '
                elif request.data.get('sort') == 'activity' or request.data.get('sort') == 'creation':
                    query_string += f'{key}={value}, '
            elif key == 'order' or key == 'sort' or key == 'tag' and value and value != "None":
                if key == 'page-size':
                    pass
                else:
                    query_string += f'{key}="{value}", '
            elif key in query_parameters and value and value != "None":
                if key == 'page-size':
                    pass
                else:
                    query_string += f'{key}={value}, '

        if query_string.endswith(', '):
            query_string = query_string[0:-2]


        print(f"site.fetch('questions', {query_string})")
        questions = eval(f"site.fetch('questions', {query_string})")
        existing_query = Query.objects.filter(query=query_string)
        print(existing_query)

        if existing_query.exists():
            print("cached")
            serialized_data = self.serializer_class(existing_query, many=True)
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        else:
            query = Query.objects.create(query=query_string, results=questions, user=request.user)
            serialized_data = self.serializer_class(query)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)

