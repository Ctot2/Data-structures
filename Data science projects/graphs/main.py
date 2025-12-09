from graph import *
star_systems = ['Aldebaran', 'Alderamin', 'Algol', 'Alioth', 'Aljanah', 'Alkaid', 'Alnair', 'Alnasl', 'Alpha Centauri', 'Altair', 'Ankaa', 'Antares', 'Arcturus', 'Ascella', 'Castor', 'Cor Caroli', 'Deneb', 'Denebola', 'Diphda', 'Fomalhaut', 'Hamal', 'Larawag', 'Markab', 'Menkalinan', 'Menkent', 'Merak', 'Muphrid', 'Musica', 'Nihal', 'Peacock', 'Phecda', 'Pollux', 'Procyon', 'Ran', 'Rasalhague', 'Regulus', 'Sabik', 'Sheratan', 'Sirius', 'Sol', 'Tarazed', 'Tau Ceti', 'Tiaki', 'Vega', 'Zaurak', 'Zosma']
hyperlanes = [['Aldebaran', 'Menkalinan'], ['Aldebaran', 'Pollux'], ['Alderamin', 'Cor Caroli'], ['Alderamin', 'Markab'], ['Alderamin', 'Vega'], ['Algol', 'Menkalinan'], ['Algol', 'Merak'], ['Algol', 'Phecda'], ['Alioth', 'Cor Caroli'], ['Aljanah', 'Markab'], ['Aljanah', 'Tarazed'], ['Alkaid', 'Markab'], ['Alkaid', 'Musica'], ['Alpha Centauri', 'Sol'], ['Alnair', 'Alpha Centauri'], ['Alnair', 'Ankaa'], ['Alnair', 'Muphrid'], ['Alnair', 'Tiaki'], ['Alnasl', 'Sabik'], ['Alnasl', 'Ascella'], ['Altair', 'Arcturus'], ['Altair', 'Fomalhaut'], ['Altair', 'Vega'], ['Ankaa', 'Denebola'], ['Ankaa', 'Sirius'], ['Antares', 'Ascella'], ['Antares', 'Larawag'], ['Arcturus', 'Muphrid'], ['Arcturus', 'Rasalhague'], ['Castor', 'Pollux'], ['Castor', 'Zaurak'], ['Deneb', 'Tarazed'], ['Denebola', 'Zosma'], ['Diphda', 'Fomalhaut'], ['Diphda', 'Hamal'], ['Diphda', 'Tau Ceti'], ['Fomalhaut', 'Sol'], ['Hamal', 'Phecda'], ['Larawag', 'Menkent'], ['Larawag', 'Peacock'], ['Menkent', 'Tiaki'], ['Nihal', 'Regulus'], ["Pollux", "Procyon"], ['Procyon', 'Ran'], ['Ran', 'Sirius'], ['Ran', 'Sol'], ['Ran', 'Tau Ceti'], ['Regulus', 'Zaurak'], ['Regulus', 'Zosma'], ['Sheratan', 'Tau Ceti']]
galaxy = Graph()
for i in star_systems:
    galaxy.add_node(Node(i))

for i in hyperlanes:
    n1 = galaxy.find_node(i[0])
    n2 = galaxy.find_node(i[1])
    galaxy.add_edge(n1, n2)

print(galaxy)

galaxy.shortest_path('Sol', 'Sheratan')