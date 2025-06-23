
✅ Como rodar o projeto:

1. Instale as dependências:
   pip install -r requirements.txt

2. Execute o servidor:
   python app.py

3. Acesse via navegador ou requisições HTTP:
   http://127.0.0.1:5000/api_il   → Para POST de e-mail e senha
   http://127.0.0.1:5000/api_tao  → Para POST de dados de cartão


✅ Para gerar um EXE:

1. Instale o PyInstaller:
   pip install pyinstaller

2. Gere o EXE:
   pyinstaller --onefile --add-data "dados;dados" app.py

O executável estará na pasta /dist

Quando rodar o EXE, o servidor ficará acessível localmente em:
http://127.0.0.1:5000

Os dados serão salvos na pasta 'dados'.
