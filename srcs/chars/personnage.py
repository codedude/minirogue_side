#!/usr/bin/env/ python3.4
#-*- coding: utf-8 -*-
#
#Launch the app

try:
	import sys
	# from gui import *
	# from chars import *

except ImportError as e:
	print("Failed to load modules : {0}".format(e))
	sys.exit(2)



class Personnage:

	def __init__(self, nom, classe):

		#attributs
		self.nom = nom
		self.classe = classe
		self.caracteristique = Caract(classe)
		self.inventaire = Inventaire()
		self.x = 0
		self.y = 0
		self.gold = 0
		self.xp = 0


	def attaquer(self, ennemi):
		ennemi.estBlesse(self.caracteristique.AP)
		return self.nom + "attaque"+ennemi.nom

	def estBlesse(self, dommages):
		if (self.caracteristique.armure < dommages):
			self.caracteristique.hp = self.caracteristique.hp - dommages + self.caracteristique.armure
			return self.nom+"a perdu " + str(dommages - self.caracteristique.armure) + " HP"
		return self.nom+"n'est pas blesse. Il est totalememt protege par son armure."

	def guerir(self, hp):
		self.caracteristique.hp += hp
		return self.nom+" a recupere"+str(hp)+" HP"

	def getGold(self, montant):
		self.gold += montant
		return self.nom+" a gagne"+str(montant)+" pieces d'or"

	def depense(self, montant):
		self.gold -= montant
		return self.nom+" a depense"+str(montant)+" pieces d'or"

	def utiliser(self, objet):
		self.caracteristique.hp += objet['hp']
		self.caracteristique.AP += objet['AP']
		self.caracteristique.agilite += objet['agilite']
		self.caracteristique.armure += objet['armure']
		texte = self.nom + "gagne "
		if (objet['hp'] != 0):
			texte += str(objet['hp']) + 'HP; '
		if (objet['AP'] != 0):
			texte += str(objet['AP']) + 'AP; '
		if (objet['armure'] != 0):
			texte += str(objet['armure']) + "d'armure; "
		if (objet['agilite'] != 0):
			texte += str(objet['agilite']) + "d'agilite"
		return texte

	def prendre(self, objet):
		self.inventaire.ajouter(objet)
		return self.utiliser(objet)

	# def fuite(self, ennemi):
	# 	if(self.caracteristique.agilite > ennemi.caracteristique.agilite):
	# 		return True

	# def deplacement(self):

class Caract:

	def __init__(self, classe):
			self.hp = classe['hp']
			self.AP = classe['AP']
			self.agilite = classe['agilite']
			self.armure = classe['armure']


class Inventaire:

	def __init__(self):
		self.objets = []

	def ajouter(self, objet):
		self.objets.append(objet)
		return "Vous avez pris" + objet['nom']

	# def jeter(self, ind_objet):
	# 	objets.pop(ind_objet)
	# 	return "Vous jetez" +objet.nom




#Definition des differents peronnages

#Attibuts du guerrier
guerrier = {}
guerrier['classe'] = 'guerrier'
guerrier['hp'] = 15
guerrier['AP'] = 4
guerrier['agilite'] = 2
guerrier['armure'] = 7

#Attributs des monstres
monstre_base = {}
monstre_base['classe'] = 'Lapin tueur'
monstre_base['hp'] = 3
monstre_base['AP'] = 2
monstre_base['agilite'] = 0
monstre_base['armure'] = 2

monstre2= {}
monstre2['classe'] = 'Chevalier noir'
monstre2['hp'] = 5
monstre2['AP'] = 1
monstre2['agilite'] = 0
monstre2['armure'] = 1

#Definition des differents objets
chaussure = {}
chaussure['nom'] = 'Chaussure de celerite'
chaussure['equipe'] = False
chaussure['usage unique'] = False
chaussure['poids'] = 2
chaussure['AP'] = 0
chaussure['agilite'] = 3
chaussure['armure'] =  0

epee = {}
epee['nom'] = 'Excalibur'
epee['usage unique'] = False
epee['equipe'] = False
epee['poids'] = 3
epee['AP'] = 3
epee['agilite'] = 0
epee['armure'] =  2 

bouclier = {}
bouclier['nom'] = 'Bouclier'
bouclier['usage unique'] = False
bouclier['equipe'] = False
bouclier['poids'] = 2
bouclier['AP'] = 0
bouclier['agilite'] = 0
bouclier['armure'] =  2 

potion = {}
potion['nom'] = "Potion de vie"
potion['usage unique'] = True
potion['poids'] = 1
potion['AP'] = 0
potion['agilite'] = 0
potion['armure'] =  0
potion['hp'] = 4


if __name__ == '__main__':
	perso = Personnage('moi', guerrier)
	monstre = Personnage('lui', monstre_base)
	print(perso.caracteristique.hp)
	print(monstre.caracteristique.hp)
	perso.attaquer(monstre)
	print(perso.caracteristique.hp)
	print(monstre.caracteristique.hp)
	monstre.prendre(potion)
	print(perso.caracteristique.hp)
	print(monstre.caracteristique.hp)

	sys.exit()



#Le royaume est en peril. La princess s'est fait capturee par le comte Dracula et seul vous, preux chevalier, pouvez l'aider. Lancez vous
#a l'attaque de son antre afin de sauver la princesse avant que son heure ne vienne. Mefiez-vous, ce sera un dangereux periple!
