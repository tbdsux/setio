import requests

import pymongo
import os

client = pymongo.MongoClient(os.getenv("MONGO_DB"))

base_url = "https://gagger.herokuapp.com"

class Meme:
    @staticmethod
    def Get(fb_id):
        db = client["SetioMemes"]
        collection = db[fb_id]

        meme = Meme.memer()

        if collection.count_documents({"fb_id": fb_id, "meme": meme}) == 0:
            collection.insert_one({"fb_id": fb_id, "meme": meme})
            return meme
        else:
            return Meme.Get(fb_id) # recursion
    
    @staticmethod
    def memer():
        resp = requests.get(base_url).json()

        return resp['meme']