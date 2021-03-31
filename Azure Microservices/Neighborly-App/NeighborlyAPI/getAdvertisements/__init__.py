import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://myneighborly-db:qHasaaGDH02MojORbigmpEdrAMhIlSCa7fiMooVsm8KsHLjFR0o9QL1AqlS4GvSSkiVUubeWa2nJyCUW5wxUlQ==@myneighborly-db.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@myneighborly-db@"
        client = pymongo.MongoClient(url)
        database = client['myneighborly-db']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

