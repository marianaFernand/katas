import morse

mensaje = input ("dime algo en morse: ")

telegrama = morse.toPlain(mensaje)
print (telegrama)