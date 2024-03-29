import sqlite3

#ordre des champs dans bdd à modifier!!!
"""champs à ajouter pour mise à jour bdd
Planteajoutee.nom
Planteajoutee.envergure
Planteajoutee.exposition
Planteajoutee.datedesemis
Planteajoutee.datedeplantation
Planteajoutee.duree
Planteajoutee.arrosage
Planteajoutee.typesol
Planteajoutee.associations
Planteajoutee.temperaturegermination
Planteajoutee.type))"""
def creationBDD():
    # connexion à la base de données
    connection = sqlite3.connect("plantes.db")
    c = connection.cursor()
    c.execute('''
              CREATE TABLE IF NOT EXISTS plantes
              ([nom] TEXT,
                [taille] INTEGER,
                [envergure] INTEGER,
                [exposition] TEXT,
                [datesemis] TEXT,
                [dateplantation] TEXT,
                [duree] INTEGER,
                [arrosage] TEXT,
                [sol] TEXT,
                [association] TEXT,
                [tempgermination] INTEGER,
                [type] TEXT
                )
              ''')
    connection.commit()
    connection.close()
