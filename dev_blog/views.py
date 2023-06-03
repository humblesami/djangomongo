import os

from pymongo import MongoClient
from django.http import HttpResponse


def mongo_operations(request):
    
    my_client = MongoClient()
    # First define the database name
    dbname = my_client['sample_medicines']
    collection_name = dbname["medicinedetails"]
    
    # let's create two documents
    medicine_1 = {
        "medicine_id": "RR000123456",
        "common_name": "Paracetamol",
        "scientific_name": "",
        "available": "Y",
        "category": "fever"
    }
    medicine_2 = {
        "medicine_id": "RR000342522",
        "common_name": "Metformin",
        "scientific_name": "",
        "available": "Y",
        "category": "type 2 diabetes"
    }
    # Insert the documents
    collection_name.insert_many([medicine_1, medicine_2])
    # Check the count
    count = collection_name.count()
    print(count)
    
    # Read the documents
    med_details = collection_name.find({})
    # Print on the terminal
    for r in med_details:
        print(r["common_name"])
    # Update one document
    data_to_update = {'medicine_id': 'RR000123456'}, {'$set': {'common_name': 'Paracetamol 500'}}
    update_data = collection_name.update_one(data_to_update)
    
    # Delete one document
    delete_data = collection_name.delete_one({'medicine_id': 'RR000123456'})
    med_details = collection_name.find({})
    # Print on the terminal
    for r in med_details:
        print(r["common_name"])
    return HttpResponse('done')
