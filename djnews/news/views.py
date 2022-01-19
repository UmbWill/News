from django.shortcuts import render
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin,  RetrieveModelMixin, UpdateModelMixin
)
from django.http import JsonResponse
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from .models import News
from .serializer import NewsSerializer
from django.utils import timezone
from .forms import ApikeyForm
import requests
from django.shortcuts import redirect

# Create your views here.

class NewsViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin,UpdateModelMixin, ListModelMixin):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def list(self,request, *args, **kwargs):
        # base class
        request.session.setdefault('wrongkey','')
        request.session.setdefault('apikey','0')
        if request.session['apikey'] == '1':
            request.session['apikey'] = '0'
        else:
            request.session['wrongkey'] = ''    
        return render(request, 'news/base.html', {'records':self.queryset.count(), 'wrongkey':request.session['wrongkey']})

    @action(detail=False, methods=['post'])	
    def apikey(self,request, *args, **kwargs):
        n = 0       
        request.session['wrongkey'] = ''
        request.session['apikey'] = '1'
        if request.method == 'POST':
            r = requests.get('https://newsapi.org/v2/everything?q=tesla&from=2022-01-15&sortBy=publishedAt&apiKey='+request.data['apikey'])
            r.json()
            try:
                r.json()['articles']
            except Exception as e:
                print("no key!")
                request.session['wrongkey']='Enter a valid key.'
                return redirect('/news/')
            for  a in r.json()['articles']:
                print(a["title"])
                news = News()
                news.source_id = a["source"]["id"]
                news.source_name = a["source"]["name"]
                news.author=a["author"]
                news.title= a["title"]
                news.description= a["description"]
                news.url=a["url"]
                news.urlToImage= a["urlToImage"]
                news.publishedAt= a["publishedAt"]
                news.content = a["content"]
                news.save()

        return redirect('/news/')

    @action(detail=False, methods=['get'])	
    def news20(self,request, *args, **kwargs):
        # get last 20 news ordered by published date
        #last20 = self.queryset.order_by('-publishedAt')[:20]
        last20 = News.objects.filter(publishedAt__lte=timezone.now()).order_by('-publishedAt')[:20]
        return render(request, 'news/list_news.html', {'news20':last20})
        data = {'articles':[]}
        for a in last20:
            data2 ={
                "source" : {
                    "id":a.source_id,
                    "name":a.source_name
                },
                "author": a.author,
                "title": a.title,
                "description": a.description,
                "url": a.url,
                "urlToImage": a.urlToImage,
                "publishedAt": a.publishedAt,
                "content" : a.content,
            }
            data['articles'].append(data2)
        #return a json response
        return JsonResponse(data, content_type='application/json')

    @action(detail=False, methods=['get'])	
    def news100(self,request, *args, **kwargs):
        # get last 100 news ordered by published date
        #last100 = self.queryset.order_by('-publishedAt')[:100]
        last100 = News.objects.filter(publishedAt__lte=timezone.now()).order_by('-publishedAt')[:100]
        data = {'articles':[]}
        for a in last100:
            data2 ={
                "source" : {
                    "id":a.source_id,
                    "name":a.source_name
                },
                "author": a.author,
                "title": a.title,
                "description": a.description,
                "url": a.url,
                "urlToImage": a.urlToImage,
                "publishedAt": a.publishedAt,
                "content" : a.content,
            }
            data['articles'].append(data2)
        #return a json response
        return JsonResponse(data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @action(detail=False, methods=['get'])	
    def news(self, request, *args, **kwargs):
        #return JsonResponse(request.data, content_type='application/json')
        print(request)
        print(request.data)
        print(request.body)
        return self.list(request, *args, **kwargs)    