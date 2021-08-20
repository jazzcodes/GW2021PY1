"""
    MongoDB
    1. Create a Cluster (Free Tier)
    2. Network Settings -> We can connect from any IP Address or some selected range
                        -> 0.0.0.0/0
                        (Security > Network Access)
    3. In the cluster, we can browse collections
        And to create collections, now we need to create a database with collection name

    4. Create Documents in Collections

    MongoDB
        stores data as Collection of Documents
        consider collection as table
        and document as rows. but document is a dictionary here :)

    CRUD Operations with MongoDB
    We will Use pymongo library to perform DB operations
    pip install pymongo -> use -> pip install 'pymongo[srv]'
"""
# to explore python with mongo db in detail
# refer the documentation -> https://docs.mongodb.com/drivers/pymongo/


import pymongo
print(pymongo.__version__)

# For making Connection with MongoDB
# We need to have a username and password
# Create Your Username and Password in DataBase Access of MongoDB Console Page | Security > DataBase Access

db_config = {
    "username": "atpl",
    "password": "atpl",
    "db_name": "gw2021py1"
}
db_uri = "mongodb+srv://{username}:{password}@cluster0.eh8zx.gcp.mongodb.net/{db_name}?retryWrites=true&w=majority".format_map(db_config)
client = pymongo.MongoClient(db_uri)
db = client.test
print(db)
print(type(db))



