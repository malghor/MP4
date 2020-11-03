# coding: utf-8
"""Partie Base de Donnée"""
import sqlite3
conn=sqlite3.connect('BD_mp4')
cur=conn.cursor()
#datas=[
#      (1,'Stéphane','Plante',416636368,'StephanePlante@test.com','connaissance'),
#      (2,'Aubert','Begin',516636368,'AubertBegin@test.com','collegue'),
#      (3,'Agrican','Jodion',516676368,'AgricanJodion@test.us','ami'),
#      (4,'Frontino','Gabriaux',116636368,'FrontinoGabriaux@test.com','connaissance'),
#      (5,'Anastasie','Goguen',519636368,'AnastasieGoguen@test.com','famille'),
#      (6,'Michel','Theberge',515136368,'MichelTheberge@test.com','client'),
#      (7,'Danielle','Blondlot',517306368,'DanielleBlondlot@test.com','collegue'),
#      ]

#cur.execute("CREATE TABLE IF NOT EXISTS ANNUAIRE(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, NOM TEXT, PRENOM TXT, TELEPHONE INT, EMAIL TEXT,QUALITE TEXT)")
#cur.executemany("INSERT INTO ANNUAIRE(id,nom,prenom,telephone,email,qualite)VALUES(?,?,?,?,?,?)",datas)
#conn.commit()


a="""Dans la base de données annuaire
1)Ajouter à la BDD
2)Supprimer
3)Modifier
4)Rechercher
5)Quitter
6)Commandes Bonus
"""

b="""
1)Recherhe par nom
2)Recherhe par prénom
3)Recherhe par telephone
4)Annuler la recherche
"""
c="""
1)Renvoie tous les noms qui se finnissent par i
2)Compter le nombre de contacts dans le répertoire
3)Trier le répertoire par ordre alphabétique (selon les noms)
4)retourner au menu principale
"""


def ajouter():
    """
    Il ne faut pas que l'id choisie soit déjà  présente dans la base de donnée,
    car si l'id utilisée est déjà  présente, le contact ne sera pas ajouter à la base de donnée
    """
    nombre=int(input("Combien de contact(s)voulez vous ajouter : "))
    nvx_data=[]
    while nombre>0:
        id=int(input("id "))
        nom=str(input("nom "))
        prenom=str(input("prenom "))
        tel=int(input("telephone "))
        email=str(input("email "))
        qualite=str(input("qualite"))
        data=(id,nom,prenom,tel,email,qualite)
        nombre-=1
        nvx_data.append(data)
        cur.executemany("INSERT or IGNORE INTO ANNUAIRE(id,nom,prenom,telephone,email,qualite)VALUES(?,?,?,?,?,?)",nvx_data)
    conn.commit()

def menu():
    boucle=True
    while boucle:
        print(a)
        z=int(input("Choix de votre la commande : "))
        if z==5:
            return ("Programme terminer")
            boucle=False
        elif z==4:
            print(b)
            z=int(input("Choix de votre recherche : "))
            if z==4:
                print(a)
            elif z==1:
                search=str(input("Nom de la personne que vous recherchez : "))
                cur.execute("SELECT prenom,nom,telephone FROM annuaire WHERE nom=? ",(search,))
                conn.commit
                print(cur.fetchall())
            elif z==2:
                search=str(input("Prenom de la personne que vous recherchez : "))
                cur.execute("SELECT prenom,nom,telephone annuaire WHERE prenom=? ",(search,))
                conn.commit
                print(cur.fetchall())
            elif z==3:
                search=str(input("Numéros de la personne que vous recherchez : "))
                cur.execute("SELECT prenom,nom,telephone FROM annuaire WHERE telephone=? ",(search,))
                conn.commit
                print(cur.fetchall())

        elif z==3:
            recherche=str(input('Contact que vous voulez modifier : '))
            z=int(input("nouveau numéros de telephone : "))
            modif=(z,recherche)
            cur.execute("UPDATE annuaire SET telephone=? WHERE nom=?",modif)
            conn.commit()


        elif z==2:
            sql="DELETE FROM annuaire WHERE nom=?"
            suppr=input("Qui voulez vous supprimer de votre répertoire ? ")
            print(suppr,"a était supprimer de votre répertoire")
            cur.execute(sql,(suppr,))
            conn.commit()

        elif z==1:
            ajouter()

        elif z==6:
            print(c)
            z=int(input("Choix de la commande : "))
            if z==1:
                cur.execute("SELECT * FROM annuaire WHERE nom LIKE'%i'")
                conn.commit
                print(cur.fetchall())
            elif z==2:
                cur.execute("SELECT COUNT(id) FROM annuaire")
                conn.commit
                print(cur.fetchall())

            elif z==3:
                sql = "SELECT * FROM annuaire ORDER BY nom" #il suffit ici de changer "nom" par "id" ou par "prenom" etc pour changer le paramètre de tri
                cur.execute(sql)                            #Pour trier par ordre décroissant il suffit de rajouter DESC apres nom
                result = cur.fetchall()
                for x in result:
                    print(x)
            elif z==4 or z>4:
                print(a)
print(menu())
cur.close()
conn.close()



