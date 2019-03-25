import csv
from academy.models import Invite
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Loading CSV")
        csv_path = "./VoterList0319.csv"
        csv_file = open(csv_path, 'rt')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            obj = Invite.objects.create(
                voterid=row['VoterID'],
                county=row['County'],
                firstname=row['First Name'],
                middlename=row['Middle Name'],
                lastname=row['Last Name'],
                suffix=row['Suffix'],
                birthdate=row['Birth Date'],
                regdate=row['Registration Date'],
                address1=row['Address 1'],
                address2=row['Address 2'],
                city=row['City'],
                state=row['State'],
                zip=row['Zip'],
                phone=row['Phone'],
                party=row['Party'],
                condistrict=row['Congressional District'],
                senatedistrict=row['Senate District'],
                assemblydistrict=row['Assembly District'],
                edudistrict=row['Education District'],
                regentdistrict=row['Regent District'],
                regprecinct=row['Registered Precinct'],
                countystatus=row['County Status'],
                countyvoterid=row['County Voter ID'],
                idrequired=row['ID Required']
            )
            print(obj)
