from flask import Flask, request, jsonify
from models import Tarefa

app = Flask(__name__)

# Lista de tarefas para exemplificar (geralmente seria um banco de dados)
tarefas = []

# Rota para editar uma tarefa
@app.route('/tarefa/<int:id>', methods=['PUT'])
def editar_tarefa(id):
    # Encontra a tarefa pela ID
    tarefa = next((t for t in tarefas if t.id == id), None)
    
    if tarefa is None:
        return jsonify({'erro': 'Tarefa não encontrada'}), 404

    # Obtendo os dados para edição do corpo da requisição
    dados = request.get_json()
    
    # Atualizando os atributos da tarefa
    tarefa.editar(
        nome=dados.get('nome'),
        descricao=dados.get('descricao'),
        data_inicio=dados.get('data_inicio'),
        data_fim=dados.get('data_fim')
    )
    
    return jsonify({
        'id': tarefa.id,
        'nome': tarefa.nome,
        'descricao': tarefa.descricao,
        'data_inicio': tarefa.data_inicio,
        'data_fim': tarefa.data_fim
    }), 200

# Iniciando o servidor
if __name__ == '__main__':
    app.run(debug=True)

