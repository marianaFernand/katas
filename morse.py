
morse = {
    'A':'·—', 
    'B':'—···', 
    'C': '—·—·', 
    'D': '—··', 
    'E': '·', 
    'F': '··—·',  
    'G': '——·',
    'H': '····', 
    'I': '··',
    'J': '·———',
    'K': '—·—',
    'L': '·—··',
    'M': '——',
    'N': '—·',
    'Ñ': '——·——', 
    'O': '———',
    'P': '·——·',
    'Q': '——·—',
    'R': '·—·', 
    'S': '···',
    'T': '—',
    'U': '··—',
    'V': '···—',
    'W': '·——',
    'X': '—··—',
    'Y': '—·——', 
    'Z': '——··',
    '0': '—————',
    '1': '·————',
    '2': '··———',
    '3': '···——',
    '4': '····—',
    '5': '·····',
    '6': '—····',
    '7': '——···', 
    '8':'———··',
    '9': '————·',
    '.': '·—·—·—',
    ',': '—·—·——',
    '?': '··——··',
    '"': '·—··—·',
    '!': '——··——'}



def toMorse(texto):
    texto = texto.upper()  #para las mayusculas
    resultado = ""
    for letra in texto:
        if letra in morse:
            resultado+= morse [letra]
            resultado+=" "
        else:
            resultado += " "
    return resultado

def toPlain(codigo):
    codigo = codigo.split(" ")
    reversoAR =reverso()
    resultado= ""
   
    for simbolo in codigo:
        if simbolo in reversoAR:
            resultado+= reversoAR[simbolo]
            resultado+=""
        else:
            resultado+=" "
    return resultado

def reverso ():
    texto = {}
    for key in morse: 
        valor = morse[key]
        texto[valor] = key
    return texto

