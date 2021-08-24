"""
    Google Firebase
    Cloud Firestore -> NoSQL Document DataBase
    https://firebase.google.com/products/firestore
"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


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
        cred = credentials.Certificate("service-account-key.json")
        # Create Connection to Firebase Backend
        firebase_admin.initialize_app(cred)
        print("Firebase Initialized")

        # get the reference of Firestore DB
        self.db = firestore.client()

    def insert_document(self, document):
        # add creates the document id automatically
        # self.db.collection('students-py').add(document)

        # set creates the document with the document id of your choice
        # set will be used to also update the document -> re-write the data
        self.db.collection('students-py').document(str(document['roll'])).set(document)
        print("Document Saved :)")

    def fetch_documents(self):
        documents = self.db.collection('students-py').get()
        for document in documents:
            # print(document) # Object of Type DocumentSnapshot
            print(document.id)
            print(document.to_dict())

    def fetch_single_document(self):
        document = self.db.collection('students-py').document('3').get()
        print(document, type(document))
        print("Document ID:", document.id)
        print("Document Dictionary:", document.to_dict())
        print("Document Vars:", vars(document))


    def delete_document(self):
        self.db.collection('students-py').document('3').delete()
        print("Document Deleted")


def main():
    my_db = DB()
    """
    student = Student(input_flag=True)
    document = vars(student)
    document['subjects'] = [
        {"physics": 0},
        {"chemistry": 0},
        {"maths": 0},
    ]
    print("DATA TO SAVE:", document)
    """

    # my_db.insert_document(document)
    # my_db.fetch_documents()
    # my_db.fetch_single_document()
    my_db.delete_document()

if __name__ == '__main__':
    main()
