# Algoritmo Genético 
#Se debe diseñar y codificar(lenguaje libre) 
# un algoritmo genético que a partir de una población inicial
#  y luego de un cierto número de iteraciones sea posible encontrar 
# una cadena de caracteres lo más cercana posible a la definida.

# POR : Juan Felipe Angel Gomez - Diego Alejandro Hernandez Villegas - Andrea Bedoya Berrio

import random

POBLACION = 100

GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
QRSTUVWXYZ '''

CADENA = "Andrea Bedoya Berrio"

class Poblacion_Individuo(object):

	def __init__(self, cromosomas):
		self.cromosomas = cromosomas
		self.fitness = self.cal_fitness()

	@classmethod
	def mutacion_genes(self):
		'''
		Crea la mutación aleatoria
		'''
		global GENES
		gene = random.choice(GENES)
		return gene

	@classmethod
	def create_gnome(self):
		'''
		Cadena de Genes
		'''
		global CADENA
		gnome_len = len(CADENA)
		return [self.mutacion_genes() for _ in range(gnome_len)]

	def mate(self, par2):
		'''
		Realiza el apareamiento para ir formando la nueva descendencia.
		'''
		
		child_cromosomas = []
		for gp1, gp2 in zip(self.cromosomas, par2.cromosomas):	
			prob = random.random()
			if prob < 0.45:
				child_cromosomas.append(gp1)
			elif prob < 0.90:
				child_cromosomas.append(gp2)
			else:
				child_cromosomas.append(self.mutacion_genes())
		return Poblacion_Individuo(child_cromosomas)

	def cal_fitness(self):
		global CADENA
		fitness = 0
		for gs, gt in zip(self.cromosomas, CADENA):
			if gs != gt: fitness+= 1
		return fitness

def main():
	global POBLACION

	iteracion = 1

	found = False
	population = []

	for _ in range(POBLACION):
				gnome = Poblacion_Individuo.create_gnome()
				population.append(Poblacion_Individuo(gnome))

	while not found:

		population = sorted(population, key = lambda x:x.fitness)
		if population[0].fitness <= 0:
			found = True
			break

		new_iteracion = []
		s = int((10*POBLACION)/100)
		new_iteracion.extend(population[:s])
		s = int((90*POBLACION)/100)

		for _ in range(s):
			parent1 = random.choice(population[:50])
			parent2 = random.choice(population[:50])
			child = parent1.mate(parent2)
			new_iteracion.append(child)

		population = new_iteracion

		print("Iteración: {}\tDescendencia: {}\tFitness: {}".\
			format(iteracion,
			"".join(population[0].cromosomas),
			population[0].fitness))

		iteracion += 1
	
	print("Iteración: {}\tDescendencia: {}\tFitness: {}".\
		format(iteracion,
		"".join(population[0].cromosomas),
		population[0].fitness))

if __name__ == '__main__':
	main()
