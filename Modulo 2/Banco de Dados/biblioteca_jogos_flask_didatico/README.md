# Biblioteca de Jogos - Flask + SQLite

Projeto simples para demonstrar persistência de dados usando:

- Python
- Flask
- SQLite
- SQL puro
- HTML/Jinja

## Instalação

```bash
pip install flask
```

## Executar

```bash
python app.py
```

Depois abra:

http://127.0.0.1:5000

O arquivo `jogos.db` será criado automaticamente na primeira execução.

## O que observar em aula

1. O navegador envia os dados do formulário.
2. Flask recebe os valores com `request.form`.
3. Python abre uma conexão com SQLite.
4. `INSERT`, `SELECT`, `UPDATE` e `DELETE` manipulam o banco.
5. `commit()` torna as alterações persistentes.
6. Mesmo fechando e reabrindo o programa, os dados continuam em `jogos.db`.

## Campo de imagem

Para manter o exemplo simples, a imagem é armazenada como URL (`TEXT`) no banco.
Assim os alunos veem que o banco guarda apenas o endereço da imagem, e não a imagem em si.
