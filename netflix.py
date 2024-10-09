# ------ Opdracht 1 ------ #

##### Opdracht 1.1 Installeren externe modules
# Bekijk het bestand 'requirements.txt'. Hierin staat welke externe modules van PyPi zijn gebruikt.
# Installeer de modules

#### Opdracht 1.2 Installeren meegeleverde modules
# Installeer en importeer de meegeleverde module 'dbc.py'

# import ....

#### Opdracht 1.3 CSV bestanden
# De variabele env['path'] verwijst naar de plek waar de csv-bestanden staan.
# Zorg ervoor dat de applicatie jouw csv-bestanden kan vinden!

env = {
    "tables" : ['buildings', 'persons','scans'], # tabellen in de database
    # pad naar de csv-bestanden eindigt met een '/'
    "path" : "" 
}

#Initialiseren (hier hoef je niks aan te doen)
question = ""
query = ""
keuze = 0

#### Opdracht 1.4 Studentgegevens
# Vul jouw gegevens in:

s = {
    "Naam": "",
    "Studentnummer": "",
    "Groep": ""
}


# ----- Opdracht 2 ------ #

#### Opdracht 2.1 Datum
# Geef hier de code om de huidige datum en tijd op het scherm af te drukken
# voorbeeld: "Datum: 12-12-2022 12:12:12"



#### Opdracht 2.2 Databaseconnectie
# Vul de gegevens in voor de database op jouw systeem

con = dbc.conn(
    host='',
    user='',
    password='',
    port=0,
    database=''
)

### Opdracht 2.3 Maak het keuzescherm zoals hieronder beschreven:
# Gebruik de list questions om een genummerd overzicht weer te geven van de vragen in de lijst

questions = [
    "Tabellen leegmaken en nieuwe gegevens inlezen",
    "Medewerkers in dienst bij SuperDuper",
    "Medewerkers aantal per functie",
    "Aantal professoren of ingenieurs",
    "Aantal medewerkers dat is ingechecked per gebouw over de gehele periode",
    "Aantal medewerkers dat is ingechecked bij een gebouw op een bepaalde datum van afgelopen maand",
    "Overzicht van medewerkers die zijn vergeten uit te checken bij een bepaald gebouw op een bepaalde datum van afgelopen maand",
    "Overzicht van alle medewerkers en het aantal uur dat ze op een bepaalde dag hebben gewerkt.",
    "Medewerker van de maand! (De medewerker die het meeste uren heeft gemaakt van iedereen over de gehele periode)"
]


# Opdracht 2.4 Maak de code om de keuze van de gebruiker in een variabele op te slaan
# Zorg ervoor dat de keuze als een integer wordt opgeslagen
# Uncomment de variabele 'keuze' en vul de code aan

# keuze ...

# ------ Opdracht 3 ------ #

# De gebruiker kiest voor nummer 1.
# De database wordt leeggemaakt en nieuwe gegevens worden geïmporteerd vanuit de csv-bestanden
# Deze code niet aanpassen!
if keuze == 1:
    # Met keuze 1 worden de tabellen in de database leeggemaakt
    # De csv-files worden ingelezen de gegevens worden in de tabellen gezet.
    # Student-file wordt aangemaakt/leegggemaakt
    dbc.clear_database(con, env["tables"], s)
    dbc.setup_database(con, env)

#### Opdracht 3.1
# geef een overzicht van alle tabellen in de database
    query = ''


#### Opdracht 3.2
# Medewerkers in dienst bij SuperDuper
if keuze == 2:
    query= ''

#### Opdracht 3.3
# Medewerkers aantal per functie
if keuze == 3:
    query= ''

#### Opdracht 3.4
# Aantal professoren of ingenieurs
if keuze == 4:
    query= ''

#### Opdracht 3.5
# Aantal medewerkers dat is ingechecked per gebouw over de gehele periode
if keuze == 5:
    query= ''

#### Opdracht 3.6
# Aantal medewerkers dat is ingechecked bij een gebouw op een bepaalde datum
if keuze == 6:
    # datum = ...
    query= ''

#### Opdracht 3.7
# Overzicht van medewerkers die zijn vergeten uit te checken bij een bepaald gebouw op een bepaalde datum
if keuze == 7:
    # datum = ...
    # gebouw = ...
    query= ''

#### Opdracht 3.8
# Overzicht van alle medewerkers en het aantal uur dat ze op een bepaalde dag hebben gewerkt.
if keuze == 8:
    # datum = ...
    query= ''

#### Opdracht 3.9
# Medewerker van de maand! (De medewerker die het meeste uren heeft gemaakt van iedereen over de gehele periode
if keuze == 9:
    query = "drop view if exists v2"
    dbc.select_query(con, query, s)
    query = "create view v2 as \
    select p.id, p.firstname, p.lastname, scandate, max(scantime) as starttime, min(scantime) as endtime, time_to_sec(timediff(max(scantime), min(scantime))) as total \
    from persons p join scans s on p.id = s.person_id group by p.id, s.scandate;"
    dbc.select_query(con, query, s)
    query = "select id, firstname, lastname, TIME_FORMAT(sec_to_time(sum(total)),'%H') as aantal_uur_gewerkt from v2 group by id order by sum(total) desc limit 0,10"

# Query wordt uitgevoerd en output wordt op scherm getoond 
# Deze code hier laten staan!
output = dbc.select_query(con, query, s)
dbc.outputToScreen(output, s)

# Output wordt in file opgeslagen
# Deze code hier laten staan!
dbc.outputToFile(question, query, s, output)
con.close()


