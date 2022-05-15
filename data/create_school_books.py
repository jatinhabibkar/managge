from random import randint
import json

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(randint(range_start, range_end))


students = [{
    "ID": 1,
    "first_name": "Andy",
    "last_name": "Fullegar",
    "email": "afullegar0@wsj.com",
    "gender": "F",
    "school": "Henry Gordon Academy",
    "book": "Sands of Iwo Jima"
  },
  {
    "ID": 2,
    "first_name": "Lucy",
    "last_name": "Olifard",
    "email": "lolifard1@macromedia.com",
    "gender": "N",
    "school": "Lake Melville School",
    "book": "Connections"
  },
  {
    "ID": 3,
    "first_name": "Brianne",
    "last_name": "Reaman",
    "email": "breaman2@clickbank.net",
    "gender": "N",
    "school": "Menihek High School",
    "book": ""
  },
  {
    "ID": 4,
    "first_name": "Lorrie",
    "last_name": "Fison",
    "email": "lfison3@nationalgeographic.com",
    "gender": "M",
    "school": "J.C. Erhardt Memorial School",
    "book": "She Cried No (Freshman Fall)"
  },
  {
    "ID": 5,
    "first_name": "Alyss",
    "last_name": "Harcombe",
    "email": "aharcombe4@toplist.cz",
    "gender": "F",
    "school": "Amos Comenius Memorial School",
    "book": "Big Nothing"
  },
  {
    "ID": 6,
    "first_name": "Cirillo",
    "last_name": "Ferby",
    "email": "cferby5@cbsnews.com",
    "gender": "N",
    "school": "Northern Lights Academy",
    "book": "Opera Jawa"
  },
  {
    "ID": 7,
    "first_name": "Sandor",
    "last_name": "Ferby",
    "email": "shylands6@rambler.ru",
    "gender": "M",
    "school": "Menihek High School",
    "book": "My Chauffeur"
  },
  {
    "ID": 8,
    "first_name": "Lev",
    "last_name": "Boyford",
    "email": "lboyford7@zdnet.com",
    "gender": "M",
    "school": "Lake Melville School",
    "book": ""
  },
  {
    "ID": 9,
    "first_name": "Gram",
    "last_name": "Mecchi",
    "email": "gmecchi8@mysql.com",
    "gender": "M",
    "school": "William Gillett Academy",
    "book": "Keane"
  },
  {
    "ID": 10,
    "first_name": "Glenine",
    "last_name": "Blakey",
    "email": "gblakey9@whitehouse.gov",
    "gender": "F",
    "school": "Queen of Peace Middle School",
    "book": "Connections"
  },
  {
    "ID": 11,
    "first_name": "Grady",
    "last_name": "Diggins",
    "email": "gdigginsa@youtu.be",
    "gender": "M",
    "school": "William Gillett Academy",
    "book": "Genghis Blues"
  },
  {
    "ID": 12,
    "first_name": "Edlin",
    "last_name": "Cotterel",
    "email": "ecotterelb@blinklist.com",
    "gender": "M",
    "school": "St. Peter's School",
    "book": ""
  },
  {
    "ID": 13,
    "first_name": "Abraham",
    "last_name": "Crothers",
    "email": "acrothersc@comsenz.com",
    "gender": "M",
    "school": "Menihek High School",
    "book": "She Cried No (Freshman Fall)"
  },
  {
    "ID": 14,
    "first_name": "Hedwig",
    "last_name": "Englefield",
    "email": "henglefieldd@mapquest.com",
    "gender": "F",
    "school": "Northern Lights Academy",
    "book": ""
  },
  {
    "ID": 15,
    "first_name": "Chrisse",
    "last_name": "Blackburne",
    "email": "cblackburnee@geocities.jp",
    "gender": "M",
    "school": "St. Peter's School",
    "book": "Sands of Iwo Jima"
  },
  {
    "ID": 16,
    "first_name": "Estelle",
    "last_name": "Tatteshall",
    "email": "etatteshallf@archive.org",
    "gender": "F",
    "school": "Menihek High School",
    "book": "Basic Instinct"
  },
  {
    "ID": 17,
    "first_name": "Robinet",
    "last_name": "Godbert",
    "email": "rgodbertg@geocities.com",
    "gender": "M",
    "school": "Henry Gordon Academy",
    "book": "Opera Jawa"
  },
  {
    "ID": 18,
    "first_name": "Hadrian",
    "last_name": "Dunaway",
    "email": "hdunawayh@cnbc.com",
    "gender": "M",
    "school": "Mud Lake School",
    "book": ""
  },
  {
    "ID": 19,
    "first_name": "Dominik",
    "last_name": "Barrick",
    "email": "dbarricki@amazon.com",
    "gender": "M",
    "school": "William Gillett Academy",
    "book": "Basic Instinct"
  },
  {
    "ID": 20,
    "first_name": "Caitlin",
    "last_name": "Whapham",
    "email": "cwhaphamj@cnn.com",
    "gender": "F",
    "school": "Queen of Peace Middle School",
    "book": ""
  },
  {
    "ID": 21,
    "first_name": "Theodore",
    "last_name": "Gentric",
    "email": "tgentrick@free.fr",
    "gender": "N",
    "school": "B.L. Morrison",
    "book": "Big Nothing"
  },
  {
    "ID": 22,
    "first_name": "Lurleen",
    "last_name": "Stickler",
    "email": "lsticklerl@whitehouse.gov",
    "gender": "F",
    "school": "Northern Lights Academy",
    "book": ""
  },
  {
    "ID": 23,
    "first_name": "Hasheem",
    "last_name": "Got",
    "email": "hgotm@cnn.com",
    "gender": "M",
    "school": "Amos Comenius Memorial School",
    "book": ""
  },
  {
    "ID": 24,
    "first_name": "Johnette",
    "last_name": "Shaudfurth",
    "email": "jshaudfurthn@yandex.ru",
    "gender": "F",
    "school": "William Gillett Academy",
    "book": "Billy Bathgate"
  },
  {
    "ID": 25,
    "first_name": "Angel",
    "last_name": "Souter",
    "email": "asoutero@europa.eu",
    "gender": "N",
    "school": "Menihek High School",
    "book": ""
  },
  {
    "ID": 26,
    "first_name": "Montgomery",
    "last_name": "Balm",
    "email": "mbalmp@ftc.gov",
    "gender": "N",
    "school": "Queen of Peace Middle School",
    "book": "Sands of Iwo Jima"
  },
  {
    "ID": 27,
    "first_name": "Frank",
    "last_name": "Tilney",
    "email": "ftilneyq@wix.com",
    "gender": "N",
    "school": "Northern Lights Academy",
    "book": ""
  },
  {
    "ID": 28,
    "first_name": "Ianthe",
    "last_name": "Merigeau",
    "email": "imerigeaur@eepurl.com",
    "gender": "F",
    "school": "St. Peter's School",
    "book": "My Chauffeur"
  },
  {
    "ID": 29,
    "first_name": "Monica",
    "last_name": "Pasquale",
    "email": "mpasquales@home.pl",
    "gender": "F",
    "school": "Jens Haven Memorial",
    "book": "Big Nothing"
  },
  {
    "ID": 30,
    "first_name": "Belicia",
    "last_name": "Cardillo",
    "email": "bcardillot@multiply.com",
    "gender": "F",
    "school": "",
    "book": ""
  },
  {
    "ID": 31,
    "first_name": "Basil",
    "last_name": "Yedy",
    "email": "byedyu@free.fr",
    "gender": "N",
    "school": "Henry Gordon Academy",
    "book": "My Chauffeur"
  },
  {
    "ID": 32,
    "first_name": "Milzie",
    "last_name": "Gyurkovics",
    "email": "mgyurkovicsv@gizmodo.com",
    "gender": "F",
    "school": "Henry Gordon Academy",
    "book": "Connections"
  },
  {
    "ID": 33,
    "first_name": "Tierney",
    "last_name": "Moulsdall",
    "email": "tmoulsdallw@stanford.edu",
    "gender": "F",
    "school": "St. Peter's School",
    "book": "Billy Bathgate"
  },
  {
    "ID": 34,
    "first_name": "Petey",
    "last_name": "Ovesen",
    "email": "povesenx@blogtalkradio.com",
    "gender": "N",
    "school": "Lake Melville School",
    "book": ""
  },
  {
    "ID": 35,
    "first_name": "Nola",
    "last_name": "Stappard",
    "email": "nstappardy@imageshack.us",
    "gender": "F",
    "school": "Queen of Peace Middle School",
    "book": "Basic Instinct"
  },
  {
    "ID": 36,
    "first_name": "Durant",
    "last_name": "Becken",
    "email": "dbeckenz@blinklist.com",
    "gender": "M",
    "school": "B.L. Morrison",
    "book": "She Cried No (Freshman Fall)"
  },
  {
    "ID": 37,
    "first_name": "Otis",
    "last_name": "Bediss",
    "email": "obediss10@google.com.au",
    "gender": "N",
    "school": "Mud Lake School",
    "book": ""
  },
  {
    "ID": 38,
    "first_name": "Diane-marie",
    "last_name": "Tommen",
    "email": "dtommen11@ask.com",
    "gender": "F",
    "school": "",
    "book": ""
  },
  {
    "ID": 39,
    "first_name": "Lotte",
    "last_name": "Clell",
    "email": "lclell12@rambler.ru",
    "gender": "N",
    "school": "Peacock Primary School",
    "book": "Billy Bathgate"
  },
  {
    "ID": 40,
    "first_name": "Sherwin",
    "last_name": "Pert",
    "email": "spert13@uiuc.edu",
    "gender": "M",
    "school": "",
    "book": "Opera Jawa"
  },
  {
    "ID": 41,
    "first_name": "Anallese",
    "last_name": "Thireau",
    "email": "athireau14@omniture.com",
    "gender": "F",
    "school": "Henry Gordon Academy",
    "book": ""
  },
  {
    "ID": 42,
    "first_name": "Chancey",
    "last_name": "Lehr",
    "email": "clehr15@prlog.org",
    "gender": "N",
    "school": "William Gillett Academy",
    "book": ""
  },
  {
    "ID": 43,
    "first_name": "Tristam",
    "last_name": "Oram",
    "email": "toram16@berkeley.edu",
    "gender": "M",
    "school": "St. Peter's School",
    "book": "Keane"
  },
  {
    "ID": 44,
    "first_name": "Niel",
    "last_name": "MacGaughey",
    "email": "nmacgaughey17@discuz.net",
    "gender": "M",
    "school": "",
    "book": "My Chauffeur"
  },
  {
    "ID": 45,
    "first_name": "Koo",
    "last_name": "Favela",
    "email": "kfavela18@com.com",
    "gender": "F",
    "school": "Lake Melville School",
    "book": ""
  },
  {
    "ID": 46,
    "first_name": "Roger",
    "last_name": "Sterre",
    "email": "rsterre19@github.com",
    "gender": "M",
    "school": "",
    "book": "Genghis Blues"
  },
  {
    "ID": 47,
    "first_name": "Dalston",
    "last_name": "Alway",
    "email": "dalway1a@creativecommons.org",
    "gender": "M",
    "school": "Henry Gordon Academy",
    "book": "Big Nothing"
  },
  {
    "ID": 48,
    "first_name": "Ryley",
    "last_name": "Gostridge",
    "email": "rgostridge1b@un.org",
    "gender": "M",
    "school": "",
    "book": "Basic Instinct"
  },
  {
    "ID": 49,
    "first_name": "Loralee",
    "last_name": "Panton",
    "email": "lpanton1c@wsj.com",
    "gender": "F",
    "school": "St. Peter's School",
    "book": ""
  },
  {
    "ID": 50,
    "first_name": "Lainey",
    "last_name": "Crossfield",
    "email": "lcrossfield1d@yolasite.com",
    "gender": "N",
    "school": "Henry Gordon Academy",
    "book": "Keane"
  }
]



schools = {"Amos Comenius Memorial School":0,
"B.L. Morrison":1,
"Henry Gordon Academy":2,
"J.C. Erhardt Memorial School":3,
"Jens Haven Memorial":4,
"Lake Melville School":5,
"Menihek High School":6,
"Mud Lake School":7,
"Northern Lights Academy":8,
"Peacock Primary School":9,
"Queen of Peace Middle School":10,
"St. Peter's School":11,
"William Gillett Academy":12}

books = {
    "Basic Instinct":0,
    "Big Nothing":1,
    "Billy Bathgate":2,
    "book":3,
    "Connections":4,
    "Genghis Blues":5,
    "Keane":6,
    "My Chauffeur":7,
    "Opera Jawa":8,
    "Sands of Iwo Jima":9,
    "She Cried No (Freshman Fall)":10
}


data = []
for (key,val) in books.items():
    data.append(
    {
        "model": "home.book",
        "pk": val,
        "fields": {
            "name": key,
            "is_active": "True"
        }
    })

for (key,val) in schools.items():
    data.append(
    {
        "model": "home.school",
        "pk": val,
        "fields": {
            "name": key,
            "phone_number": "+91"+random_with_N_digits(10),
            "is_active": "True"
        }
    })
for s in students:
    school=1
    book=1
    if(s["school"]!= ''):
        school = schools[s["school"]]
    if(s["book"]!= ''):
        book = books[s["book"]]
    
    data.append({
        "model": "home.student",
        "pk": s["ID"],
        "fields": {
            "first_name": s["first_name"],
            "last_name": s["last_name"],
            "email": s["email"],
            "gender": s["gender"],
            "school": school,
            "book": book,
            "pages_read_count": random_with_N_digits(randint(1,4))
        }
    })

with open('load.json', 'w') as fp:
    json.dump(data, fp)