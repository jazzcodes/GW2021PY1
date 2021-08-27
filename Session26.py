import pymongo
import ssl # if you get SSL Certificate Error

class Student:

    def __init__(self, input_flag=False, roll=0, name="NA", email="NA", age=0):
        if input_flag:
            self.roll = int(input("Enter Roll Number: "))
            self.name = input("Enter Your Name: ")
            self.email = input("Enter Your Email: ")
            self.age = int(input("Enter Age: "))
        else:
            self.roll = roll
            self.name = name
            self.email = email
            self.age = age

    def __str__(self):
        return "{roll}, {name}, {email}, {age}".format_map(vars(self))


class DB:

    def __init__(self):
        db_config = {
            "username": "atpl",
            "password": "atpl",
            "db_name": "gw2021py1"
        }
        db_uri = "mongodb+srv://{username}:{password}@cluster0.eh8zx.gcp.mongodb.net/{db_name}?retryWrites=true&w=majority".format_map(
            db_config)
        # client = pymongo.MongoClient(db_uri)
        client = pymongo.MongoClient(db_uri, ssl_cert_reqs=ssl.CERT_NONE) # if you get SSL Certificate Error
        print("DB Connection Created :)")

        # self.db = client.gw2021py1
        self.db = client['gw2021py1'] # get the reference of our database
        self.collections = self.db.list_collection_names()

    def insert(self, document):
        # Select the Collection in which you wish to work
        self.collection = self.db['students']
        self.collection.insert_one(document)
        print("Document Inserted")

    def insert_operation(self, collection, document):
        # Select the Collection in which you wish to work
        self.collection = self.db[collection]
        self.collection.insert_one(document)
        print("Document Inserted")

    def fetch_collections(self):
        print("Fetching Collections from DB")
        for collection in self.collections:
            print(collection)

    def fetch_documents_in_collection(self, collection_name):
        print("Fetching Documents from", collection_name)
        self.collection = self.db[collection_name]
        documents = self.collection.find()
        for document in documents:
            print(document)
            # print(type(document)) # DataType -> Dictionary
        return documents

    def fetch_documents_in_collection_with_condition(self, collection_name, roll_number):
        print("Fetching Documents from", collection_name)
        self.collection = self.db[collection_name]
        # query = {"roll": roll_number}
        query = {"roll": {"$gt": roll_number}}
        # documents = self.collection.find(query)
        documents = self.collection.find(query).sort('name', -1) #-> -1 is descending order | by default -> ascending order
        for document in documents:
            print(document)
            # print(type(document)) # DataType -> Dictionary

    def delete_document_from_collection(self, collection_name, roll_number):
        query = {"roll": roll_number}
        self.collection = self.db[collection_name]
        result = self.collection.delete_one(query)
        # self.collection.delete_many(query)
        if result.deleted_count > 0:
            print("Document Deleted: ", result.deleted_count)
        else:
            print("Document Could'nt be Found :(")

    def update_document_in_collection(self, collection_name, roll_number):

        document = {"name": "John Watson", "email": "john.watson@example.com", "age": 25}
        update_query = {"$set": document}
        query = {"roll": roll_number}

        self.collection = self.db[collection_name]
        self.collection.update_one(query, update_query)
        # self.collection.update_many()

        print("Record Updated")


def main():

    my_db = DB()
    # my_db.fetch_collections()
    # my_db.fetch_documents_in_collection('students')
    # my_db.fetch_documents_in_collection_with_condition(collection_name="students", roll_number=1)
    # my_db.delete_document_from_collection(collection_name="students", roll_number=1)

    my_db.update_document_in_collection(collection_name="students", roll_number=1)

if __name__ == '__main__':
    main()

# Assignment: Create a GUI for a Student Registration Form
# Insert the data into Mongo DB