const apiUrl = 'http://ec2-44-211-255-243.compute-1.amazonaws.com:8080/api/livros';  // Atualize para a URL do seu backend na AWS

document.addEventListener('DOMContentLoaded', listarLivros);

async function listarLivros() {
    try {
        const response = await fetch(apiUrl);
        
        if (!response.ok) {
            throw new Error('Erro ao listar livros: ' + response.statusText);
        }
        
        const data = await response.json();
        const tbody = document.querySelector('#livrosTable tbody');
        tbody.innerHTML = '';

        data.forEach(livro => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${livro.id}</td>
                <td>${livro.nome}</td>
                <td>${livro.autor}</td>
                <td>${livro.ano}</td>
                <td>${livro.exemplares}</td>
                <td><img src="${livro.fotoCapa}" alt="Capa do Livro" width="50"></td>
                <td>
                    <button onclick="editarLivro(${livro.id})">Editar</button>
                    <button onclick="deletarLivro(${livro.id})">Deletar</button>
                </td>
            `;
            tbody.appendChild(tr);
        });
    } catch (error) {
        console.error('Erro ao listar livros:', error);
    }
}

async function salvarLivro() {
    const id = document.getElementById('livroId').value;
    const nome = document.getElementById('nome').value;
    const autor = document.getElementById('autor').value;
    const ano = parseInt(document.getElementById('ano').value);
    const exemplares = parseInt(document.getElementById('exemplares').value);
    const fotoCapa = document.getElementById('fotoCapa').value;

    const livro = { nome, autor, ano, exemplares, fotoCapa };

    try {
        let response;
        if (id) {
            // Atualizar
            response = await fetch(`${apiUrl}/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(livro)
            });
        } else {
            // Criar
            response = await fetch(apiUrl, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(livro)
            });
        }

        if (!response.ok) {
            throw new Error('Erro ao salvar livro: ' + response.statusText);
        }

        limparForm();
        listarLivros();
    } catch (error) {
        console.error('Erro ao salvar livro:', error);
    }
}

async function editarLivro(id) {
    try {
        const response = await fetch(`${apiUrl}/${id}`);

        if (!response.ok) {
            throw new Error('Erro ao editar livro: ' + response.statusText);
        }

        const livro = await response.json();
        document.getElementById('livroId').value = livro.id;
        document.getElementById('nome').value = livro.nome;
        document.getElementById('autor').value = livro.autor;
        document.getElementById('ano').value = livro.ano;
        document.getElementById('exemplares').value = livro.exemplares;
        document.getElementById('fotoCapa').value = livro.fotoCapa;
    } catch (error) {
        console.error('Erro ao editar livro:', error);
    }
}

async function deletarLivro(id) {
    if (confirm('Tem certeza que deseja deletar este livro?')) {
        try {
            const response = await fetch(`${apiUrl}/${id}`, { method: 'DELETE' });

            if (!response.ok) {
                throw new Error('Erro ao deletar livro: ' + response.statusText);
            }

            listarLivros();
        } catch (error) {
            console.error('Erro ao deletar livro:', error);
        }
    }
}

function limparForm() {
    document.getElementById('livroId').value = '';
    document.getElementById('livroForm').reset();
}
