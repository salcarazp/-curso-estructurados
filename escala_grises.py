from PIL import Image

# Ruta de la imagen original
ruta_imagen = "img/logo.png"  # Puedes poner aquí ruta absoluta o relativa

# Abrir imagen
imagen_original = Image.open(ruta_imagen)

# Convertir a escala de grises - "L" es el modo de Pillow para escala de grises
imagen_gris = imagen_original.convert("L")

# Mostrar la imagen en gris
imagen_gris.show()

# Guardar la imagen en gris
imagen_gris.save("img/logo_gris.png")

print("Conversión a escala de grises realizada con éxito.")
