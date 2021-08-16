"""
    Multi Threading :)
"""

import requests
import json
import threading


class Printer(threading.Thread):

    def __init__(self, document_name=None, num_of_copies=1):
        super().__init__() # execute the constructor of Thread Class. Mandatory
        self.document_name = document_name
        self.num_of_copies = num_of_copies

    # def print_document(self, document_name=None, num_of_copies=1):
    def run(self):
        for i in range(1, self.num_of_copies+1):
            print("## Printing Document {} Copy#{}".format(self.document_name, i))


class FetchCovidCases(threading.Thread): # IS-A

    # def fetch_cases(self):
    def run(self):
        url = "https://api.covid19india.org/v4/min/timeseries.min.json"
        response = requests.get(url)
        print(response.text[:100])
        # covid_cases = json.loads(response.text)
        # print(covid_cases)
        # print(covid_cases[])


# Execution of our Code is SEQUENTIAL
def main():
    print("App Started")

    cases = FetchCovidCases()
    # cases.fetch_cases()
    cases.start()

    printer = Printer(document_name="LearningPython.pdf", num_of_copies=10)
    # printer.print_document(document_name="LearningPython.pdf", num_of_copies=10)
    printer.start()


    print("App Finished")


if __name__ == '__main__':
    main()