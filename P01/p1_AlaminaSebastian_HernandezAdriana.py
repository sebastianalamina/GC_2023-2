# Genómica Computacional [2023-2] - Práctica 1
# 318685496 | Sebastián Alamina Ramírez
# 316161570 | Adriana Henández Gasca
import re

def cadena_complementaria(cadena, ADN):
	"""Devuelve la secuencia complementaria a la dada, con bases correspondientes al ADN (True) o al ARN (False)."""

	# Comprobaciones de tipado :P.
	assert type(cadena) == str
	assert type(ADN) == bool

	# Bases que se unen por puentes de hidrógeno.
	bases_complementarias = {
		"A":None, # La Adenina se une con Timina dentro del ADN, y con Uracilo dentro del ARN.
		"T":"A",
		"U":"A",
		"C":"G",
		"G":"C"
	}

	# Creamos la secuencia complementaria al ir leyendo y transformando la original.
	secuencia_complementaria = ""
	for base in cadena:

		# Analizamos cuál será la base que reemplazará a la leída actualmente.
		# Si se lee otra letra que no corresponda a una base correcta,
		# no transcribimos dicha letra.
		try:
			base_complementaria = bases_complementarias[base]
		except KeyError as e:
			base_complementaria = ""

		# Determinamos si dejar Timina o Uracilo, que depende
		# de si la cadena resultante será ADN o ARN.
		if base == "A":
			if ADN:
				base_complementaria = "T"
			else:
				base_complementaria = "U"

		# La "cadena/secuencia complementaria" de la secuencia S es la
		# cadena/secuencia con el "complemento" de cada base de S.
		secuencia_complementaria += base_complementaria

	# Regresamos la secuencia complementaria.
	return(secuencia_complementaria)

class Secuencia(object):
	"""Secuencia 'original', su complementaria, su ARNm, sus aminoácidos, etc."""

	def __init__(self, ADN, tres_prima_a_cinco_prima):
		"""
		Método instanciador/inicializador que almacena una cadena/secuencia de ADN,
		según vaya de 3' a 5' (True) o de 5' a 3' (False).
		También calcula y guarda otros valores relevantes.
		"""

		# Verificaciones de tipado :P.
		assert type(ADN) == str
		assert type(tres_prima_a_cinco_prima) == bool

		# Comprobaciones sobre los parámetros.
		if "U" in ADN:
			raise Exception("Una secuencia de ADN no debería contener Uracilo, comprueba la cadena proporcionada.")

		# Guardamos el ADN, y su cadena complementaria, según sea el caso.
		if tres_prima_a_cinco_prima:
			self.ADN_tres_a_cinco = ADN
			self.ADN_cinco_a_tres = cadena_complementaria(ADN, True)
		else:
			self.ADN_cinco_a_tres = ADN
			self.ADN_tres_a_cinco = cadena_complementaria(ADN, True)

		# Transcribimos el ADN en ARNm.
		self.ARNm_cinco_a_tres = cadena_complementaria(self.ADN_tres_a_cinco, False)

		# Traducimos el ARNm en aminoácidos.  
		self.traducir()

	def traducir(self):
		"""Calcula y guarda las cadenas de aminoácidos generables en el ARNm."""

		# Aminoácidos correspondientes a cada codón.
		codones_traducción = {
			# Alanina
			"GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
			# Cisteína
			"UGU":"C", "UGC":"C",
			# Ácido aspártico
			"GAU":"D", "GAC":"D",
			# Ácido glutámico
			"GAA":"E", "GAG":"E",
			# Fenilalanina
			"UUU":"F", "UUC":"F",
			# Glicina
			"GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",
			# Histidina
			"CAU":"H", "CAC":"H",
			# Isoleucina
			"AUA":"I", "AUU":"I", "AUC":"I",
			# Lisina
			"AAA":"K", "AAG":"K",
			# Leucina
			"UUA":"L", "UUG":"L", "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
			# Metionina
			"AUG":"M", 
			# Aspargina
			"AAU":"N", "AAC":"N",
			# Prolina
			"CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
			# Glutamina
			"CAA":"Q", "CAG":"Q",
			# Arginina
			"CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R",
			# Serina
			"UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S", "AGU":"S", "AGC":"S",
			# Treonina
			"ACU":"U", "ACC":"U", "ACA":"U", "ACG":"U",
			# Valina
			"GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
			# Triptofano
			"UGG":"W",
			# Tirosina
			"UAU":"Y", "UAC":"Y",
			# Stop
			"UAA":"_", "UAG":"_", "UGA":"_"
		}

		# Lista que contendrá las secuencias de aminoácidos del ARNm.
		self.secuencias_de_aminoácidos = []

		# Codones partícipes en un ORF.
		codón_inicio = r"AUG"
		codón_paro = r"(UAA|UAG|UGA)"
		codones = r"((?!"+codón_paro+")(.{3}))*" # Cero o más codones que no sean de paro.

		# Open Reading Frame.
		ORF = codón_inicio+codones+codón_paro

		# Buscamos los ORF, para realizar las traducciones.
		for m in re.finditer(ORF, self.ARNm_cinco_a_tres):

			# La secuencia de aminoácidos actual.
			secuencia_de_aminoácidos = ""

			# Generamos codones al ir leyendo a partir del codón de inicio y
			# guardamos en la secuencia de aminoácidos el aminoácido correspondiente.
			codón = ""
			for base in m.group(): # Sin argumentos, Match.group() devuelve el match completo.
				
				# Vamos generando y traduciendo codones con las bases leídas.
				codón += base
				if len(codón)%3 == 0:
					secuencia_de_aminoácidos += codones_traducción[codón]
					codón = ""

			# Reportamos la posición en la cual empieza el ORF.
			secuencia_de_aminoácidos += f" desde la posición {m.start()} del ARNm."

			# Guardamos la secuencia de aminoácidos actual.
			self.secuencias_de_aminoácidos.append(secuencia_de_aminoácidos)

	def __str__(self):
		"""Representación en String."""
		s = ""
		s += f"• ADN   3'-5': {self.ADN_tres_a_cinco}\n"
		s += f"• ADN   5'-3': {self.ADN_cinco_a_tres}\n"
		s += f"• ARNm  5'-3': {self.ARNm_cinco_a_tres}\n"
		if self.secuencias_de_aminoácidos == []:
			s += "• La secuencia no tiene secuencias de aminoácidos."
			return s
		s += f"• Aminoácidos:\n"
		for s_aá in self.secuencias_de_aminoácidos:
			s += f"\t• {s_aá}\n"
		return s[:-1]

if __name__ == '__main__':
	"""Método Main."""
	
	# Leemos del usuario el nombre del archivo a trabajar.
	# strip() elimina whitespaces al principio y al final de la cadena.
	print("Introduce el nombre del archivo a leer.")
	print("• Éste se debe encontrar relativo al directorio donde se encuentra este archivo .py.")
	print("• Por ejemplo, suponiendo que \"al lado\" de este archivo hay una carpeta llamada 'data' con archivos FASTA dentro, es válido introducir 'data/dnaE.txt' (sin comillas)...")
	filename = input().strip()

	# Abrimos el archivo (en modo Sólo Lectura) y extraemos la secuencia.
	ADN = None
	with open(filename, 'r') as reader:

		# Se espera que la primera línea sea un encabezado.
		header = reader.readline()

		# Error si la primera línea no es el encabezado.
		if header[0] != ">":
			raise Exception("Error con el formato del archivo FASTA; la primera línea del archivo ha de contener el encabezado.")

		# Se espera que la segunda línea sea la secuencia.
		ADN = reader.readline()

		# Error si la secuencia es vacía o, por alguna razón, se leyó un encabezado.
		if ADN == "" or ">" in ADN:
			raise Exception("Error al intentar leer la secuencia; asegúrate de que ésta se encuentre en la segunda línea del archivo.")

		# Le quitamos el salto de línea al final de la secuencia (si tiene).
		if ADN[-1] == "\n":
			ADN = ADN[:-1]

	# Imprimimos los datos relacionados con la secuencia proporcionada.
	if ADN != None:
		S = Secuencia(ADN, True)
		print(S)
