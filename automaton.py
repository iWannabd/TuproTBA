fa = {
	# berikut adalah data tabel FA yang dimuat dalam bentuk dictionary python
	"A":
  {
    "a": "I",
    " ": "A",
    "n": "E",
    "q": "B",
    "p": "B",
    "s": "B",
    "r": "B",
    "t": "W",
    "x": "P",
    "o": "L",
    "i": "T",
    "(": "N",
    ")": "O"
  },
    "B":
  {
    " ": "A",
    "q": "A",
    "p": "A",
    "s": "A",
    "r": "A"
  },
    "C":
  {
    " ": "C",
    "q": "C",
    "p": "C",
    "s": "C",
    "r": "C"
  },
    "E":
  {
    "o": "F"
  },
    "F":
  {
    " ": "A",
    "t": "G"
  },
    "G":
  {
    " ": "A"
  },
    "I":
  {
    "n": "J"
  },
    "J":
  {
    "d": "K"
  },
    "K":
  {
    " ": "A"
  },
    "L":
  {
    " ": "A",
    "r": "M"
  },
    "M":
  {
    " ": "A"
  },
    "P":
  {
    "o": "Q",
    "r": "R"
  },
    "Q":
  {
    "r": "R"
  },
    "R":
  {
    " ": "A"
  },
    "T":
  {
    "f": "U"
  },
    "U":
  {
    " ": "A",
    "f": "V"
  },
    "W":
  {
    "h": "X"
  },
    "X":
  {
    "e": "Y"
  },
    "Y":
  {
    "n": "Z"
  },
    "Z":
  {
    " ": "A"
  },
  	"V":
  	{
  		" ":"A"
  	},
  	"N":
  	{
  		" ":"A"
  	},
  	"O":
  	{
  		" ":"A"
  	}



}
#daftar final state
finalstate = {
	'B''G''K''M''R''U''Z''V''N''O'
}
#berisi daftar dtate token beserta nomornya
tokens = {
	'B':1,
	'G':2,
	'K':3,
	'M':4,
	'R':5,
	'U':6,
	'Z':7,
	'V':8,
	'N':9,
	'O':10
}

def bacakan(transisi,init,finals,string):
	#fungsi ini mengouputkan nomor token berdasarkan string yang dibaca
	tok = [] # daftar token yang dibaca
	state = init #init diisi dengan state awal
	for x in string:
		state = transisi[state][x] #state diganti dengan next state, berulang sepanjang string
		if state in tokens:
			tok.append(tokens[state]) #menambahkan nomor token yang terbaca
	print tok
#setiap token harus dipisahkan dengan spasi 
bacakan(fa,'A',finalstate,'if ( p or q ) and r xor s then p or q')