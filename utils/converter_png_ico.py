from PIL import Image

# Abra a imagem que você deseja converter
img = Image.open("WhatsApp Image 2026-03-31 at 11.15.08 AM.jpeg")  # Altere para o caminho da sua imagem

#  Salve a imagem no formato ICO
img.save("favicon.ico", format="ICO", sizes=[(96, 96)])  # Define o tamanho do ícone (32x32 no exemplo)
