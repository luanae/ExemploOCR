## Extração de texto via OCR com correção ortográfica

A atividade teve como objetivo extrair texto de arquivo PDF utilizando OCR, ele converte o PDF em imagem para possibilitar o uso do OCR, extrai o texto usando tesseract e aplica correção ortográfica, além de armazenar o conteúdo em arquivos txt.

## Pré-requisitos:
- Python 3.3+.
- Tesseract OCR.
- Poppler.
- Pip

## Bibliotecas utilizadas:

- Pillow: Manipulação das imagens.
- Pytesseract: Extração dos textos de imagem (OCR).
- Pdf2image: Conversão de PDF para imagem JPG.
- Pyspellchecker: Correção ortogréfica.

## Instalação das dependências:
No terminal, crie um ambiente virtual e instale os pacotes:
- Ambiente virtual: _Python -m venv venv_
- Bibliotecas: _pip install pillow pytesseract pdf2image pyspellchecker_

## Instalação do Tesseract 
- Instalação do tesseract através do link: https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe
- Após isso, adicione a paste ao PATH nas váriaveis de ambiente.

## Instalação e utilização da biblioteca Pdf2image
Foi necessario a utilização do poppler que é um conjunto de ferramentas usado internamente pela biblioteca pd2image para converter páginas de PDF em imagem.

- Para baixar no windows: https://github.com/oschwartz10612/poppler-windows/releases/
- Extraia o arquivo .zip
- Adicione o caminho da pasta bin ao PATH em variáveis do sistema
- Após fazer isso, reinicie seu terminal para que a nova variável seja reconhecida.

## Funcionamento do código:
O script converte o PDF em imagens, aplica OCR com tesseract, corrige a ortografia do texto extraído e salva em arquivos .txt.
  
