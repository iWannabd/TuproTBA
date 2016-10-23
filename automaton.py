fa = {
	"A":
  {
    "a": "F",
    " ": "A",
    "n": "C",
    "q": "B",
    "p": "B",
    "s": "B",
    "r": "B",
    "t": "Q",
    "x": "K",
    "o": "I",
    "i": "N",
    "(": "U",
    ")": "V"
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
    "o": "D"
  },
    "D":
  {
    "t": "E"
  },
    "E":
  {
    " ": "A"
  },
    "F":
  {
    "n": "G"
  },
    "G":
  {
    "d": "H"
  },
    "H":
  {
    " ": "A"
  },
    "I":
  {
    "r": "J"
  },
    "J":
  {
    " ": "A"
  },
    "K":
  {
    "o": "L",
  },
    "L":
  {
    "r": "M"
  },
    "M":
  {
    " ": "A"
  },
    "N":
  {
    "f": "O"
  },
    "O":
  {
    " ": "A",
    "f": "P"
  },
    "P":
  {
    " ": "A"
  },
    "Q":
  {
    "h": "R"
  },
    "R":
  {
    "e": "S"
  },
    "S":
  {
    "n": "T"
  },
  "T":
  {
    " ":"A"
  },
  	"U":
  	{
  	   " ":"A"
  	},
  	"V":
  	{
  	   " ":"A"
  	}

}
#daftar final state
finalstate = {
	'B''E''H''J''M''P''T''U''V''O'
}

#berisi daftar dtate token beserta nomornya
tokens = {
	'B':1,
	'E':2,
	'H':3,
	'J':4,
	'M':5,
	'P':6,
	'T':7,
	'U':8,
	'V':9,
	'O':10
}

def bacakan(transisi,init,finals,string):
        #fungsi ini mengouputkan nomor token berdasarkan string yang dibaca
	tok = [] # daftar token yang dibaca
	state = init #init diisi dengan state awal
	for x in string:
                try:
                        state = transisi[state][x] #state diganti dengan next state, berulang sepanjang string
                except KeyError:
                    print "simbol ",x," tidak valid"
                    break
                if state in tokens:
                    tok.append(tokens[state]) #menambahkan nomor token yang terbaca
	print tok
        print string
#setiap token harus dipisahkan dengan spasi
var = "if ( ) or not p q r s not xor if then"
bacakan(fa,'A',finalstate,var)
