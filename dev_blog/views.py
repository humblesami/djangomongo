import os
import random

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
    # for r in med_details:
    #     print(r["common_name"])
    filter = {'medicine_id': 'RR000123456'}
    newvalues = {"$set": {'common_name': 'Paracetamol 500'}}
    collection_name.update_one(filter, newvalues)
    
    # Delete one document
    delete_data = collection_name.delete_one({'medicine_id': 'RR000123456'})
    med_details = collection_name.find({})
    
    # Print on the terminal
    # for r in med_details:
    #     print(r["common_name"])
    
    bulk_insert(dbname)
    return HttpResponse('done')


def bulk_insert(dbname):
    cnt = 1
    test_collection_data = []
    student_records = dbname["students"]
    max_records = 10000
    pending_count_to_reach_10k = max_records - student_records.count()
    print('Pending count', pending_count_to_reach_10k)
    while cnt <= pending_count_to_reach_10k:
        test_collection_data.append({"name": "student" + str(cnt), "age": random.randint(18, 40)})
        cnt += 1
    if len(test_collection_data):
        student_records.insert_many(test_collection_data)
    else:
        print('Can not insert 0 records, there exist already '+str(max_records) + ' records')
    print('Student count', student_records.count())