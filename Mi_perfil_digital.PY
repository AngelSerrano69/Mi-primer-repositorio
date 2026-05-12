#uso de los tipos de datos en python
# 1. Datos basicos (str, int, bool, float)

nombre = "Angel de Jesús Serrano Lopez"
edad = 14
estatura = 1.72
es_estudiante = True

# 2. Redes_Sociales = (tuple)

Redes_sociales = ("serr.151", "angl.192")

# 3. Playlist de cantantes favoritos = (list en un dict)

Playlist = [{"titulo": "Man in the mirror", "artista": "Michael Jackson", "duracion": "5:18"},
{"titulo": "Human nature", "artista": "Michael Jackson", "duracion": "4:07"},
{"titulo": "I want you back", "artista": "The Jackson 5", "duracion": "2:56"}]

print("presentacion personal")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿estoy activo en el colegio?", es_estudiante)
print("Mis redes sociales son:", Redes_sociales)
print("Mi playlist favorita:") 
print(f"{cancion["titulo"]} - {cancion["artista"]})({cancion["duracion"]})min")
print ("----------------------------------")
