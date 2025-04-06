# importação das bibliotecas usadas
from PIL import Image         #manipulacao das imagens
import pytesseract             # ocr
from pdf2image import convert_from_path    #convercao de pdf em imagem
from spellchecker import SpellChecker      #correcao automatica

imagem = Image.open("exemplo_ocr.jpg") # abre uma imgaem
texto = pytesseract.image_to_string(imagem, lang='por')   # extrai o texto da imagem
spell = SpellChecker(language="pt")    # define o idioma usado pelo corretor
palavras = texto.split()
correcao = [spell.correction(p) if spell.correction(p) else p for p in palavras]
# aplica a correcao em todas as palavras e mantem a original caso nao tenha necessidade de alteracao
texto_corrigido = " ".join(correcao)
print("Texto corrigido:", texto_corrigido)  # exibe o texto
print(texto)

# Converter PDF para imagem
imagens = convert_from_path('Mussum Ipsum.pdf')
# salva cada pagina como uma imagem
for i, img in enumerate(imagens):
    img.save(f'pagina_{i}.jpg', 'JPEG')   # define o nome que sera salvo
    print(f'Página {i} salva como imagem.')

# página0
imagem0 = Image.open("pagina_0.jpg")
texto0 = pytesseract.image_to_string(imagem0, lang='por')
print(texto0)
spell = SpellChecker(language="pt")
palavras0 = texto0.split()
correcao0 = [spell.correction(p) if spell.correction(p) else p for p in palavras0]
texto_corrigido0 = " ".join(correcao0)
with open("Pagina_0.txt", "w", encoding="utf-8") as f:
    f.write(texto_corrigido0)
print("Texto corrigido:", texto_corrigido0)

# página 1
imagem1 = Image.open("pagina_1.jpg")
texto1 = pytesseract.image_to_string(imagem1, lang='por')
print(texto1)
spell = SpellChecker(language="pt")
palavras1 = texto1.split()
correcao1 = [spell.correction(p) if spell.correction(p) else p for p in palavras1]
texto_corrigido1 = " ".join(correcao1)
with open("Pagina_1.txt", "w", encoding="utf-8") as f:
    f.write(texto_corrigido1)
print("Texto corrigido:", texto_corrigido1)

imagem2 = Image.open("pagina_2.jpg")
texto2 = pytesseract.image_to_string(imagem2, lang='por')
print(texto2)
spell = SpellChecker(language="pt")
palavras2 = texto2.split()
correcao2 = [spell.correction(p) if spell.correction(p) else p for p in palavras2]
texto_corrigido2 = " ".join(correcao2)
with open("Pagina_2.txt", "w", encoding="utf-8") as f:
    f.write(texto_corrigido2)
print("Texto corrigido:", texto_corrigido2)

imagem3 = Image.open("pagina_3.jpg")
texto3 = pytesseract.image_to_string(imagem3, lang='por')
print(texto3)
spell = SpellChecker(language="pt")
palavras3 = texto3.split()
correcao3 = [spell.correction(p) if spell.correction(p) else p for p in palavras3]
texto_corrigido3 = " ".join(correcao3)
with open("Pagina_3.txt", "w", encoding="utf-8") as f:
    f.write(texto_corrigido3)
print("Texto corrigido:", texto_corrigido3)