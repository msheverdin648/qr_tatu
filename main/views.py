from django.shortcuts import render
from django.views import View


class IndexView(View):

    def get(self, request):
        context = {}
        return render(request, 'main/index.html', context)