import requests
import json
list = [
'Tabraiz Shamsi',
'Imran Tahir',
'Farhaan Behardien',
'JP Duminy',
'Dane Paterson',
'Andile Phehlukwayo',
'David Miller',
'Aaron Phangiso',
'AB de Villiers',
'Dwaine Pretorius',
'Beuran Hendricks',
'Mangaliso Mosehle',
'Quinton de Kock',
'Hashim Amla',
'Robbie Frylinck',
'Dean Elgar',
'Dale Steyn',
'Morne Morkel',
'Theunis de Bruyn',
'Kagiso Rabada',
'Faf du Plessis',
'Keshav Maharaj',
'Vernon Philander',
'Aiden Markram',
'Temba Bavuma',
'Chris Morris',
'Lungi Ngidi',
'Duanne Olivier',
'Khaya Zondo',
'Heinrich Klaasen',
'JJ Smuts',
'Christiaan Jonker',
'Reeza Hendricks',
'Junior Dala',
'Wiaan Mulder',
'Shaun von Berg',
'Gihahn Cloete',
'Rassie van der Dussen',
'Zubayr Hamza',
'Pieter Malan',
'Lutho Sipamla',
'Janneman Malan',
'Anrich Nortje',
'Sinethemba Qeshile',
'Bjorn Fortuin',
'George Linde',
'Dane Piedt',
'Senuran Muthusamy',
'Rudi Second',
'Keegan Petersen',
'Sisanda Magala',
'Kyle Verreynne',
'Pite van Biljon',
'Daryn Dupavillion',
'Glenton Stuurman',
'Migael Pretorius',
'Raynard van Tonder',
'Sarel Erwee',
'Ottniel Baartman',
'Marco Jansen',
'Nandre Burger',
'Okuhle Cele',
'Jacques Snyman',
'Ryan Rickelton',
'Lizaad Williams'
]

for i in list:
	print("\n")
	url = 'https://cricapi.com/api/playerFinder?apikey=C41BJ7yN9wQmL1uByfrhksidpJs1&name='+i
	response = requests.request("GET", url)
	print(response.text)






