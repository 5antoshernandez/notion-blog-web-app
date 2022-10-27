from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from .forms import ContactForm

import requests

class home(View):
    template = 'home/home.html'
    success_url = reverse_lazy('success')

    def get(self, request):
        # get notion database objects

        #add your secret key after Bearer in authorization
        #replace url with your notion database url.
        url = 'https://api.notion.com/v1/databases/34539ca85b9d46a8984e4ef5bb65c0db/query'
        headers = {'content-type': 'application/json', 'Notion-Version' : '2021-08-16', 'Authorization' : 'Bearer '}
        blogs = requests.post(url, headers=headers).json()["results"]

        form = ContactForm()


        ctx = {
            'blogs' : blogs,
            'form' : form
        }

        return render(request, self.template, ctx)

    def post(self, request):
        form = ContactForm(request.POST)
        if not form.is_valid():
            #add your secret key after Bearer in authorization
            #replace url with your notion database url.
            url = 'https://api.notion.com/v1/databases/34539ca85b9d46a8984e4ef5bb65c0db/query'
            headers = {'content-type': 'application/json', 'Notion-Version' : '2021-08-16', 'Authorization' : 'Bearer '}
            blogs = requests.post(url, headers=headers).json()["results"]
            ctx = {
                'blogs' : blogs,
                'form' : form
            }
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

def success(request):
    return render(request, "home/success.html")

def blog(request, blog_id):
    # get notion blog
    page_url = f'https://api.notion.com/v1/pages/{blog_id}'
    page_headers = {'content-type': 'application/json', 'Notion-Version' : '2021-08-16', 'Authorization' : 'Bearer '}
    blog = requests.get(page_url, headers=page_headers).json()

    # get content associated with notion blog
    blocks_url = f'https://api.notion.com/v1/blocks/{blog_id}/children'
    blocks_headers = {'content-type': 'application/json', 'Notion-Version' : '2021-08-16', 'Authorization' : 'Bearer '}
    blocks = requests.get(blocks_url, headers=blocks_headers).json()
    ctx = {
        'blog' : blog,
        'blocks':blocks
    }

    return render(request, "home/blog_detail.html", ctx)