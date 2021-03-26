import logging
import azure.functions as func
import pymongo

from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            url = ""
            client = pymongo.MongoClient(url)
            database = client['notes_db']
            collection = database['notes']       

            result = collection.find({})
            result = dumps(result)            

            return func.HttpResponse(result,mimetype="application/json",charset="utf-8", status_code=200)

        except:
            return func.HttpResponse("Bad request", status_code=400)

    else:
        try:
            url = ""
            client = pymongo.MongoClient(url)
            database = client['notes_db']
            collection = database['notes']       

            result = collection.find_one({'title': name})
            result = dumps(result)
            print(result)

            return func.HttpResponse(result,mimetype="application/json",charset="utf-8", status_code=200)

        except:
            return func.HttpResponse("Bad request", status_code=400)