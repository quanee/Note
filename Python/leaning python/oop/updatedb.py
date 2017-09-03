import shelve


db = shelve.open('persondb')

for key in sorted(db):