from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import *
from package import requetesql


class Plante:
    """création structure pour bdd de plantes"""

    def __init__(self):
        self.nom = ""
        self.type = ""
        self.hauteur = 0
        self.envergure = 0
        self.typesol = ""
        self.arrosage = ""
        self.associations = ""
        self.temperaturegermination = 0
        self.exposition = ""
        self.datedesemis = ""
        self.datedeplantation = ""
        self.duree = ""


    "création méthode d'ajout d'un nom de plante"


Planteajoutee = Plante()
tamponplantes = []


class Fenetreajoutplante(QWidget):
    def __init__(self):
        super().__init__()
        layoutPrincipal = QHBoxLayout(self)
        layoutGauche = QGridLayout(self)
        layoutDroit = QVBoxLayout(self)
        layoutDroitHaut = QGridLayout(self)
        layoutDroitBas = QVBoxLayout(self)
        layoutPrincipal.addLayout(layoutGauche)
        layoutPrincipal.addLayout(layoutDroit)
        layoutDroit.addLayout(layoutDroitHaut)
        layoutDroit.addLayout(layoutDroitBas)

        self.setWindowTitle("fenêtre d'ajout de plante")
        self.LBLnom = QLabel("Quel est le nom de la plante? ")
        self.LEnom = QLineEdit()
        self.LBLtype = QLabel("Quel type de plante est-ce?")
        self.LEtype = QLineEdit()
        self.LBLht = QLabel("Quelle est la hauteur de la plante? ")
        self.LEht = QLineEdit()
        self.LBLenvergure = QLabel("Quelle est son envergure? ")
        self.LEenvg = QLineEdit()
        self.LBLexpo = QLabel("A quelle exposition peut on la planter (ombre, mi-ombre, etc): ")
        self.LEexpo = QLineEdit()
        self.LBLdatesemis = QLabel("Quand peut-on débuter les semis: ")
        self.LEdatesemis = QLineEdit()
        self.LBLdateplantation = QLabel("Quand peut on les mettre en pleine terre: ")
        self.LEdateplantation = QLineEdit()
        self.LBLduree = QLabel("combien de temps occupe-t-il l'espace octroyer dans le jardin? ")
        self.LEduree = QLineEdit()
        self.LBLarrosage = QLabel("Quel est son besoin en eau? ")
        self.LEarrosage = QLineEdit()
        self.LBLsol = QLabel("Quelle doit être la richesse du sol? ")
        self.LEsol = QLineEdit()
        self.LBLassoc = QLabel("Avec quelles autres plantes peut-on l'associer? ")
        self.LEassoc = QLineEdit()
        self.LBLtempgerm = QLabel("Quelle est la température de germination? ")
        self.LEtempgerm = QLineEdit()

        # ajout widget layout gauche
        layoutGauche.addWidget(self.LBLnom, 0, 0)
        layoutGauche.addWidget(self.LEnom, 0, 1)
        layoutGauche.addWidget(self.LBLht, 1, 0)
        layoutGauche.addWidget(self.LEht, 1, 1)
        layoutGauche.addWidget(self.LBLenvergure, 2, 0)
        layoutGauche.addWidget(self.LEenvg, 2, 1)
        layoutGauche.addWidget(self.LBLexpo, 3, 0)
        layoutGauche.addWidget(self.LEexpo, 3, 1)
        layoutGauche.addWidget(self.LBLdatesemis, 4, 0)
        layoutGauche.addWidget(self.LEdatesemis, 4, 1)
        layoutGauche.addWidget(self.LBLdateplantation, 5, 0)
        layoutGauche.addWidget(self.LEdateplantation, 5, 1)
        layoutGauche.addWidget(self.LBLduree, 6, 0)
        layoutGauche.addWidget(self.LEduree, 6, 1)
        layoutGauche.addWidget(self.LBLarrosage, 7, 0)
        layoutGauche.addWidget(self.LEarrosage, 7, 1)
        layoutGauche.addWidget(self.LBLsol, 8, 0)
        layoutGauche.addWidget(self.LEsol, 8, 1)
        layoutGauche.addWidget(self.LBLassoc, 9, 0)
        layoutGauche.addWidget(self.LEassoc, 9, 1)
        layoutGauche.addWidget(self.LBLtempgerm, 10, 0)
        layoutGauche.addWidget(self.LEtempgerm, 10, 1)
        layoutGauche.addWidget(self.LBLtype, 11, 0)
        layoutGauche.addWidget(self.LEtype, 11, 1)

        # bouton de commande layout droit
        btnSauvegarde = QPushButton("Sauvegarde", self)
        btnRecherche = QPushButton("Rechercher", self)
        btnAjouter = QPushButton("Ajouter", self)
        btnSupprimer = QPushButton("Supprimer", self)
        btnQuitter = QPushButton("Quitter", self)
        btnQuitter.clicked.connect(self.quitterajoutplante)
        btnSauvegarde.clicked.connect(self.sauvegardeplantes)
        btnRecherche.clicked.connect(self.rechercherplante)
        btnAjouter.clicked.connect(self.ajouterplante)
        btnSupprimer.clicked.connect(self.supprimerplante)

        # ajout boutons au layout droit
        layoutDroitBas.addWidget(btnAjouter)
        layoutDroitBas.addWidget(btnRecherche)
        layoutDroitBas.addWidget(btnSauvegarde)
        layoutDroitBas.addWidget(btnSupprimer)
        layoutDroitBas.addWidget(btnQuitter)
        layoutDroitBas.setAlignment(Qt.AlignLeft)
        layoutDroitBas.setAlignment(Qt.AlignBottom)
        self.setLayout(layoutPrincipal)
        self.resize(800, 600)

    def quitterajoutplante(self):
        self.close()

    def sauvegardeplantes(self, repertoire):
        pass

    def rechercherplante(self):
        pass

    def ajouterplante(self):
        # ajouter la plante au tampon avant la sauvegarde dans la BDD
        Planteajoutee.nom = self.LEnom.text()
        Planteajoutee.hauteur = self.LEht.text()
        Planteajoutee.envergure = self.LEenvg.text()
        Planteajoutee.exposition = self.LEexpo.text()
        Planteajoutee.datedesemis = self.LEdatesemis.text()
        Planteajoutee.datedeplantation = self.LEdateplantation.text()
        Planteajoutee.duree = self.LEduree.text()
        Planteajoutee.arrosage = self.LEarrosage.text()
        Planteajoutee.typesol = self.LEsol.text()
        Planteajoutee.associations = self.LEassoc.text()
        Planteajoutee.temperaturegermination = self.LEtempgerm.text()
        Planteajoutee.type = self.LEtype.text()
        tamponplantes.append((Planteajoutee.nom, Planteajoutee.hauteur, Planteajoutee.envergure, Planteajoutee.exposition, Planteajoutee.datedesemis, Planteajoutee.datedeplantation, Planteajoutee.duree, Planteajoutee.arrosage, Planteajoutee.typesol, Planteajoutee.associations, Planteajoutee.temperaturegermination, Planteajoutee.type))
        requetesql.maj_bdd(tamponplantes)
        tamponplantes.clear()

    def supprimerplante(self):
        pass
    def parcourirlabasededonnee(self):
        connection = sqlite3.connect("plantes.db")
        cursor = connection.cursor()
        sqlstr = 'SELECT * FROM plantes'
        plantedelabdd = cursor.execute(sqlstr)
        donnees = plantedelabdd.fetchall()
        for plante in donnees:
            print(plante)

        #en cours de création