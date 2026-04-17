# imagem oficial do Python
FROM python:3.13-slim

# diretório de trabalho dentro do container
WORKDIR /app

# copia os arquivos do projeto para dentro do container
COPY . .

# executar a aplicação
CMD ["python", "calculadora.py"]
