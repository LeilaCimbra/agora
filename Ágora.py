import re

usuarios = [
    {
        'id': 'admin', 'senha': '1234', 'nome': 'Administrador',
        'email': 'admin', 'telefone': '00000000000',
        'cpf': '00000000000', 'endereco': 'Biblioteca Ágora', 'tipo': 'admin'
    },
    {
        'id': '123456', 'senha': '123456', 'nome': 'Fulano',
        'email': 'fulano@gmail.com', 'telefone': '12123412345',
        'cpf': '12345678901', 'endereco': 'Casa do Fulano', 'tipo': 'comum'
    }
]
livros = [
    {'titulo': 'O Senhor dos Anéis', 'autor': 'J.J.R.Tolkien', 'isbn': '1234567890', 'tema': 'Fantasia', 'emprestado': False},
    {'titulo': 'Romeu e Julieta', 'autor': 'William Shakespeare', 'isbn': '9876543210', 'tema': 'Romance', 'emprestado': False},
    {'titulo': 'Guerra dos Tronos', 'autor': 'George R.R. Martin', 'isbn': '123456789', 'tema': 'Fantasia', 'emprestado': False},
    {'titulo': 'Memórias Póstumas de Brás Cubas', 'autor': 'Machado de Assis', 'isbn': '987654321', 'tema': 'Satira', 'emprestado': False},
    {'titulo': 'Cinquenta tons de cinza', 'autor': 'E.L. James', 'isbn': '12345', 'tema': 'Romance', 'emprestado': False}
]
emprestimos = []
solicitacoes = []
tempo_atual = 0

tentativas_senha = {}

def validar_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validar_id(id):
    return any(i['id'] == id for i in usuarios)

def cpf_existente(cpf):
    return any(u['cpf'] == cpf for u in usuarios)

def validar_telefone(telefone):
    return telefone.isdigit() and len(telefone) == 11

def validar_senha(senha):
    return len(senha) >= 6

def campos_obrigatorios_preenchidos(dados):
    return all(dados.values())

def menu_livros():
    global livros
    while True:
        print("\nGerenciamento de Livros")
        print("1 - Cadastrar um Livro") 
        print("2 - Remover um Livro")
        print("0 - Voltar")
        op = input("Opção: ")

        if op == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            tema = input("Tema: ")
            if not (titulo and autor and isbn and tema):
                print("Erro: Todos os campos são obrigatórios.")
                continue
            existente = next((l for l in livros if l['isbn'] == isbn), None)
            if existente:
                print("Livro já existe. Atualizando cadastro.")
                existente['titulo'] = titulo
                existente['autor'] = autor
                existente['tema'] = tema
            else:
                livros.append({'titulo': titulo, 'autor': autor, 'isbn': isbn, 'tema': tema, 'emprestado': False})
                print("Livro cadastrado com sucesso.")
        elif op == '2':
            isbn = input("ISBN do livro a excluir: ")
            livro = next((l for l in livros if l['isbn'] == isbn), None)
            if not livro:
                print("Livro não encontrado.")
                continue
            if livro['emprestado']:
                print("Não é possível excluir: livro está emprestado.")
                continue
            livros.remove(livro)
            print("Livro excluído.")
        elif op == '0':
            break

def cadastrar_usuario():
    while True:
        print("\nCadastro de Usuário")
        print("\n1 - Cadastrar Administrador")
        print("2 - Cadastrar Usuário Comum")
        print("3 - Editar Usuário")
        print("4 - Excluir Usuário")
        print("0 - Voltar")

        op = input("\nEscolha uma opção: ")
        
        if op == '1':
            if not usuario_logado or usuario_logado['tipo'] != 'admin':
                print("Erro: Apenas administradores podem cadastrar novos administradores.")
                continue
            nome = input("Nome: ").strip()
            id = input("ID: ").strip()
            email = input("Email: ").strip()
            telefone = input("Telefone: ").strip()
            cpf = input("CPF: ").strip()
            endereco = input("Endereço: ").strip()
            senha = input("Senha (mínimo 6 caracteres): ").strip()

            if not (validar_email(email)):
                print("Erro: Email inválido.")
                continue

            if (validar_id(id)):
                print("Erro: ID inválido.")
                continue

            if not (validar_telefone(telefone)):
                print("Erro: Telefone inválido.")
                continue

            if not (validar_senha(senha)):
                print("Erro: Senha inválida.")
                continue

            if cpf_existente(cpf):
                print("Erro: CPF já cadastrado.")
                continue

            dados = {
                'id': id,
                'nome': nome,
                'email': email,
                'telefone': telefone,
                'cpf': cpf,
                'endereco': endereco,
                'senha': senha,
                'tipo': 'admin'
            }

            if not campos_obrigatorios_preenchidos(dados):
                print("Erro: Todos os campos devem ser preenchidos.")
                continue

            usuarios.append(dados)
            print("Administrador cadastrado com sucesso!")

        elif op == '2':
            if not usuario_logado or usuario_logado['tipo'] != 'admin':
                print("Erro: Apenas administradores podem cadastrar usuários.")
                continue
            nome = input("Nome: ").strip()
            id = input("ID: ").strip()
            email = input("Email: ").strip()
            telefone = input("Telefone: ").strip()
            cpf = input("CPF: ").strip()
            endereco = input("Endereço: ").strip()
            senha = input("Senha (mínimo 6 caracteres): ").strip()

            if not (validar_email(email)):
                print("Erro: Email inválido.")
                continue

            if (validar_id(id)):
                print("Erro: ID inválido.")
                continue

            if not (validar_telefone(telefone)):
                print("Erro: Telefone inválido.")
                continue

            if not (validar_senha(senha)):
                print("Erro: Senha inválida.")
                continue

            if cpf_existente(cpf):
                print("Erro: CPF já cadastrado.")
                continue

            dados = {
                'id': id,
                'nome': nome,
                'email': email,
                'telefone': telefone,
                'cpf': cpf,
                'endereco': endereco,
                'senha': senha,
                'tipo': 'comum'
            }

            if not campos_obrigatorios_preenchidos(dados):
                print("Erro: Todos os campos devem ser preenchidos.")
                continue

            usuarios.append(dados)
            print("Usuário cadastrado com sucesso!")
        
        elif op == '3':
            if not usuario_logado or usuario_logado['tipo'] != 'admin':
                print("Erro: Apenas administradores podem editar usuários.")
                continue
            cpf = input("Digite o CPF do usuário a ser editado: ")
            usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
            if not usuario:
                print("Usuário não encontrado.")
                continue

            editar_usuario(usuario)

        elif op == '4':
            if not usuario_logado or usuario_logado['tipo'] != 'admin':
                print("Erro: Apenas administradores podem excluir usuários.")
                continue
            cpf = input("Digite o CPF do usuário a ser excluído: ")
            usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
            if not usuario:
                print("Usuário não encontrado.")
                continue

            excluir_usuario(usuario_logado)

        elif op == '0':
            break
        
def excluir_usuario(usuario_logado):
    if usuario_logado['tipo'] != 'admin':
        print("Apenas administradores podem excluir usuários.")
        return

    cpf = input("Digite o CPF do usuário a ser excluído: ")
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)

    if not usuario:
        print("Usuário não encontrado.")
        return

    if usuario['id'] == usuario_logado['id']:
        print("Não é permitido excluir a si mesmo. Ação inválida.")
        return

    senha = input("Confirme sua senha: ")
    if senha != usuario_logado['senha']:
        print("Senha incorreta.")
        return

    usuarios.remove(usuario)
    print("Usuário excluído com sucesso.")

def buscar_livros():
    print("\nBuscar Livros")
    print("Filtros disponíveis: título, autor, ISBN")
    titulo = input("Título (opcional): ").lower()
    autor = input("Autor (opcional): ").lower()
    isbn = input("ISBN (opcional): ")
    tema = input("Tema (opcional): ")

    resultados = []
    for livro in livros:
        if (not titulo or titulo in livro['titulo'].lower()) and \
           (not autor or autor in livro['autor'].lower()) and \
           (not isbn or isbn == livro['isbn']) and \
           (not tema or tema in livro['tema'].lower()):
            resultados.append(livro)

    if not resultados:
        print("Nenhum livro encontrado. Tente novamente.")
    else:
        for l in resultados:
            status = 'Emprestado' if l['emprestado'] else 'Disponível'
            print(f"{l['titulo']} - {l['autor']} (ISBN: {l['isbn']}, Tema: {l['tema']}) - {status}")

def registrar_emprestimo():
    global emprestimos, tempo_atual
    print("\nRegistrar Empréstimo")
    cpf = input("CPF do usuário: ")
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if not usuario:
        print("Usuário não encontrado.")
        return
    isbn = input("ISBN do livro: ")
    livro = next((l for l in livros if l['isbn'] == isbn), None)
    if not livro:
        print("Livro não encontrado.")
        return
    if livro['emprestado']:
        print("Livro já emprestado.")
        return
    emprestimos_usuario = [e for e in emprestimos if e['cpf'] == cpf and not e['devolvido']]
    multa = sum(max(0, tempo_atual - (e['data'] + 14)) for e in emprestimos_usuario)
    if multa > 10:
        print("Empréstimo não permitido. Verifique suas pendências na aba 'Minha conta'.")
        return
    livro['emprestado'] = True
    emprestimos.append({'cpf': cpf, 'isbn': isbn, 'data': tempo_atual, 'devolvido': False})
    print("Empréstimo registrado com sucesso.")

def registrar_devolucao():
    global emprestimos
    print("\nDevolução de Livro")
    isbn = input("ISBN do livro: ")
    emprestimo = next((e for e in emprestimos if e['isbn'] == isbn and not e['devolvido']), None)
    if not emprestimo:
        print("Empréstimo não encontrado ou livro já devolvido.")
        return
    livro = next((l for l in livros if l['isbn'] == isbn), None)
    emprestimo['devolvido'] = True
    livro['emprestado'] = False
    atraso = max(0, tempo_atual - (emprestimo['data'] + 14))
    if atraso > 0:
        print(f"Livro devolvido com {atraso} dias de atraso. Pendência registrada.")
    else:
        print("Livro devolvido com sucesso. Sem pendências.")

def relatorios():
    print("\nRelatórios:")
    print("1 - Livros Emprestados")
    print("2 - Livros Devolvidos")
    print("3 - Livros em Atraso")
    op = input("Escolha: ")
    for e in emprestimos:
        livro = next((l for l in livros if l['isbn'] == e['isbn']), None)
        if not livro:
            continue
        status = "Em atraso" if not e['devolvido'] and tempo_atual > e['data'] + 14 else "No prazo"
        if op == '1' and not e['devolvido']:
            print(f"{livro['titulo']} (ISBN {livro['isbn']}) - {status}")
        elif op == '2' and e['devolvido']:
            print(f"{livro['titulo']} (ISBN {livro['isbn']}) - Devolvido")
        elif op == '3' and not e['devolvido'] and tempo_atual > e['data'] + 14:
            atraso = tempo_atual - (e['data'] + 14)
            print(f"{livro['titulo']} - {atraso} dias em atraso")

def avancar_dias():
    global tempo_atual
    dias = int(input("Quantos dias deseja avançar? "))
    tempo_atual += dias
    print(f"Tempo avançado para o dia {tempo_atual}.")

def editar_usuario(usuario):
    print("\nEditar Perfil")
    usuario['nome'] = input(f"Nome ({usuario['nome']}): ") or usuario['nome']
    usuario['telefone'] = input(f"Telefone ({usuario['telefone']}): ") or usuario['telefone']
    usuario['endereco'] = input(f"Endereço ({usuario['endereco']}): ") or usuario['endereco']
    nova_senha = input("Nova senha (deixe em branco para manter): ")
    if nova_senha:
        if validar_senha(nova_senha):
            usuario['senha'] = nova_senha
        else:
            print("Senha inválida. Mínimo de 6 caracteres.")
    print("Perfil atualizado com sucesso.")

def consultar_usuarios():
    print('\nLista de Usuários')
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    
    for u in usuarios:
        print(f"Nome: {u['nome']} | CPF: {u['cpf']} | Tipo: {u['tipo']} | ID: {u['id']}")

def login():
    usuario_id = input("\nUsuário (e-mail): ")
    senha = input("Senha: ")

    usuario = next((u for u in usuarios if u['email'] == usuario_id), None)
    if not usuario:
        print("Usuário não encontrado.")
        return None

    tentativas = tentativas_senha.get(usuario_id, 0)
    if tentativas >= 3:
        print("Conta bloqueada. Requer recuperação.")
        return None

    if senha == usuario['senha']:
        tentativas_senha[usuario_id] = 0
        print(f"\nBem-vindo, {usuario['nome']}!")
        return usuario
    else:
        tentativas_senha[usuario_id] = tentativas + 1
        print("Senha incorreta.")
        return None

def menu_principal(usuario_logado):
    while True:
        print("\nMenu Principal")
       
        if usuario_logado['tipo'] == 'admin':
            print("\n1 - Consultar Livro")
            print("2 - Empréstimo") 
            print("3 - Gerenciamento de Livros")
            print("4 - Cadastrar Usuário")
            print("5 - Devolução")
            print("6 - Consultar Usuário")
            print("7 - Relatórios")
            print("8 - Avançar Dias")
            print("9 - Ver Solicitações") 
            print("0 - Sair")
        else:
            print("\n1 - Buscar Livros")
            print("2 - Meus Livros")
            print("3 - Solicitar Livro")
            print("4 - Excluir Solicitação")
            print("5 - Editar Perfil")
            print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if usuario_logado['tipo'] == 'admin':
            if opcao == "1":
                buscar_livros()
            elif opcao == "2":
                registrar_emprestimo()
            elif opcao == "3":
                menu_livros()
            elif opcao == "4":
                cadastrar_usuario()
            elif opcao == "5":
                registrar_devolucao()
            elif opcao == "6" and usuario_logado['tipo'] == 'admin':
                consultar_usuarios()
            elif opcao == "7":
                relatorios() 
            elif opcao == "8":
                avancar_dias()
            elif opcao == "9":
                ver_solicitacoes()
            elif opcao == "0":
                break
        else:
            if opcao == "1":
                buscar_livros()
            elif opcao == "2":
                meus_livros(usuario_logado)
            elif opcao == "3":
                solicitar_livro(usuario_logado)
            elif opcao == "4":
                excluir_solicitacao(usuario_logado)
            elif opcao == "5":
                editar_usuario(usuario_logado)
            elif opcao == "0":
                break

def meus_livros(usuario):
    print("\nMeus Livros:")
    for emp in emprestimos:
        if emp['cpf'] == usuario['cpf'] and not emp['devolvido']:
            livro = next((l for l in livros if l['isbn'] == emp['isbn']), None)
            if livro:
                atraso = tempo_atual - (emp['data'] + 14)
                status = "Em dia" if atraso <= 0 else f"Atrasado ({atraso} dias)"
                print(f"{livro['titulo']} - {status}")

def solicitar_livro(usuario):
    cpf = usuario['cpf']
    pendencias = any(
        not e['devolvido'] and tempo_atual > e['data'] + 14
        for e in emprestimos if e['cpf'] == cpf
    )
    if pendencias:
        print("Você possui pendências e não pode solicitar novos livros.")
        return

    isbn = input("Digite o ISBN do livro a solicitar: ")
    livro = next((l for l in livros if l['isbn'] == isbn), None)
    if not livro:
        print("Livro não encontrado.")
        return
    if livro['emprestado']:
        print("Livro indisponível.")
        return

    livro['emprestado'] = True
    solicitacoes.append({
        'usuario': usuario['nome'],
        'cpf': cpf,
        'isbn': isbn,
        'data': tempo_atual,
        'prevista_entrega': tempo_atual + 14
    })
    emprestimos.append({
        'cpf': cpf,
        'isbn': isbn,
        'data': tempo_atual,
        'devolvido': False
    })
    print("Solicitação registrada com sucesso.")

def excluir_solicitacao(usuario):
    cpf = usuario['cpf']
    solicit = next((s for s in solicitacoes if s['cpf'] == cpf), None)
    if not solicit:
        print("Nenhuma solicitação encontrada.")
        return
    solicitacoes.remove(solicit)
    livro = next((l for l in livros if l['isbn'] == solicit['isbn']), None)
    if livro:
        livro['emprestado'] = False
    emprestimo = next((e for e in emprestimos if e['cpf'] == cpf and e['isbn'] == solicit['isbn'] and not e['devolvido']), None)
    if emprestimo:
        emprestimos.remove(emprestimo)
    print("Solicitação excluída com sucesso.")

def ver_solicitacoes():
    print("\nSolicitações de Empréstimo:")
    if not solicitacoes:
        print("Nenhuma solicitação no momento.")
        return
    for s in solicitacoes:
        livro = next((l for l in livros if l['isbn'] == s['isbn']), None)
        status = "Indisponível" if livro and livro['emprestado'] else "Disponível"
        print(f"{s['usuario']} solicitou o livro ISBN {s['isbn']} - Status: {status}")

while True:
    usuario_logado = None
    while not usuario_logado:
        print("\nSistema de Biblioteca Ágora")
        print("1 - Login")
        print("0 - Sair")
        escolha = input("Escolha: ")
        if escolha == "1":
            usuario_logado = login()
        elif escolha == "0":
            print("Saindo do sistema.")
            exit()
        else:
            print("Opção inválida.")

    menu_principal(usuario_logado)
