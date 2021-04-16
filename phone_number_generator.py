import csv
from random import randrange,randint

class phone_number_generator:
    def __init__(self):
        return None

    def generate_phone(self,country,phone_type):
        with(open("phone_format.csv") as csv_file):
            csv_reader = csv.DictReader(csv_file)
            phone_number = ''
            for row in csv_reader:
                if(row['Country'] == country and row['type']==phone_type):
                    phone_number = 'random_phone_number:'
                    for character in row['format']:
                        if(character != 'x'):
                            phone_number+=character
                        else:
                            phone_number+=str(randint(1,9))
            if(phone_number == ''):
                phone_number='error: Country not found or incorrect'
            return phone_number
    
    

