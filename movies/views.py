
from django.shortcuts import render
from rest_framework.decorators import api_view
from pymongo import MongoClient
from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime,timedelta
# Create your views here.

client=MongoClient()
db= client['moviestest']

@api_view(['GET'])
def get_frist(request):
    collection=db['movies']
    data=[]
    cursor=collection.aggregate([{"$group":{"_id":"director","count":{"$sum":1}}}])
    data=list(cursor)
    return JsonResponse(data,safe=False)

@api_view(['GET'])
def get_mostpopular (request):
    collection = db['movies']
    cursor =collection.find().sort({"$99popularity":1}).limit(-1)
    data = []
    for doc in cursor:
        doc.pop("_id")
        data.append(doc)
    return JsonResponse(data,safe=False)
 
@api_view(['GET'])
def get_max_wat(request):
    collection = db['movies']
    cursor=collection.aggregate([{"$group":{"_id":"$director","count":{"$max":"$name"}}}])
    data = []
    for doc in cursor:
        doc.pop("_id")
        data.append(doc)
    return JsonResponse(data,safe=False)


@api_view(['GET'])
def get_leastwatch(request):
    collection = db['movies']
    cursor=collection.aggregate([{"$group":{"_id":"name","minScore":{"$min":"$imdb_score"}}}])
    data = []
    for doc in cursor:
        doc.pop("_id")
        data.append(doc)
    return JsonResponse(data,safe=False)





#post fav movie
@api_view(['POST'])
def post_fav(request):
    print(request.data)
    collection = db['movies']
    data=[]

    cursor = collection.insert({"99popularity":request.data["99popularity"],
                                "director":request.data["director"],
                                "genre":request.data["genre"],
                                "imdb_score":request.data["imdb_score"],
                                "name":request.data["name"]})
    return JsonResponse({'data':'ok'},safe=False)    





#Director with maximum number of movies 

#What is the most popular genere watched by audiance

#List out top ten movies according to imdb score.

#Find Least watched movie by its imdb score.

#Who is the best director in the top hundred movies

#Add your favouite movie details in database using POST method.

db.test.find({"number": {"$gt": 1}}).sort([("number", 1), ("date", -1)])