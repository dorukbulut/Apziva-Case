import email
from http.client import HTTPResponse
from re import search
from telnetlib import STATUS
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Individual
from json import loads
import requests
import aiohttp
import asyncio

TOKEN = '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'
headers = {'Authorization': 'token ' + TOKEN}

# Async api calls in order to get faster results
async def main(user_data):
    index = 1
    async with aiohttp.ClientSession() as session : 
        tasks = []
        
        for user in user_data["items"] :
            task = asyncio.ensure_future(get_user_data(session, user, index))
            tasks.append(task)
            index += 1

        users = await asyncio.gather(*tasks)

        return users

async def get_user_data(session, user, index):
    async with session.get(user["url"],headers=headers) as response:

        profile_data = await response.json()

        async with session.get(user["repos_url"], headers=headers) as response2:
            repos_data = await response2.json()

            new_user = {
                "id" : index,
                "name" : profile_data['name'],
                'email' : profile_data['email'],
                'location' : profile_data['location'],
                'bio' : profile_data['bio'],
                'github' : user['html_url'],
                'languages' : list(set([repos['language'] for repos in repos_data]))
            }

             


            return new_user



# Create your views here.

def index(req): 
    return render(req, "index.html")



@csrf_exempt
def save_to_db(req):
    person = loads(req.body)
    new_person = Individual(name=person["user_name"], 
                            email=person["user_email"],
                            location = person["user_location"],
                            bio = person["user_bio"],
                            job_title = person["job_title"],
                            skills = person["user_skills"], 
                            github_url = person["user_github"]
    )

    new_person.save()
    return JsonResponse({"status" : 200})

    
@csrf_exempt
def results(req):
    search_text  = req.POST.get('search')
    response = requests.get('https://api.github.com/search/users',params={'q': search_text}, headers=headers)
    user_data = response.json()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    users = asyncio.run(main(user_data))
    return render(req, "results.html", {"search": search_text, "users": users})
    
