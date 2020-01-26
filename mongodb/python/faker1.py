#Write fake data into MongoDB
import pymongo
from faker import Faker
import random

client = pymongo.MongoClient("mongodb://mongo:27017/")

db = client["faker1"]

faker1 = db["faker1"]

print(client.database_names())

fake = Faker()			
db.faker1.insert_many([{
		 'i': i
		,'first_name':fake.first_name()
		,'last_name':fake.last_name()
		,'job':fake.job()
		,'company':fake.company()
		,'date_of_birth':fake.date(pattern="%Y-%m-%d", end_datetime=None)
		,'city':fake.city()
		,'country':fake.country()
		,'phone_number':fake.phone_number()
		,'iban':fake.iban()
		,'account_balance':random.randrange(0,1000000000)
		} for i in range(1000)]).inserted_ids

print(db.faker1.count_documents({}))


