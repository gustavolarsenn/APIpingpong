API ping pong - Criado por Gustavo Larsen e Guilherme Henrick Bessa

Criada utilizando a linguagem Python, junto da biblioteca "Flask".

Foi criada duas rotas, com somente o método 'GET', sendo:

1.http://localhost:5000/

2.http://localhost:5000/pingpong

Para cada rota, foi criada uma função, que retornar uma string, sendo o response.

Para a primeira rota ('/'), foi criada a função "show()", que não recebe parâmetro algum, e somente retorna o texto "Ping ou pong?"

Para a segunda rota('/pingpong/(string)'), foi criada a função "convert(req)", que receberá uma string (not case-sensitive) como parâmetro, que deverá ser "ping" ou "pong"

Caso for "ping", retornará "pong"
Caso for "pong", retornará "pong"
Caso for algo diferente das citadas anteriormente, retornará "Nem ping nem pong!"

Caso seja acessado alguma rota diferente das citadas anteriormente, será retornado o HTTP error 404 "NOT FOUND"

Caso for utilizado algum outro método além do 'GET' nas rotas existente, será retornado o HTTP error 405 "METHOD NOT ALLOWED"