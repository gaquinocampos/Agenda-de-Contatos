import json
import os
import time

arquivo_agenda = "contatos.json"

def exibir_menu():
    print("\n" + "="*30)
    print("       AGENDA DE CONTATOS      ")
    print("="*30)
    print("1. Adicionar Contato (Create)")
    print("2. Listar Contatos (Read)")
    print("3. Buscar Contato (Read)")
    print("4. Atualizar Contato (Update)")
    print("5. Excluir Contato (Delete)")
    print("6. Criar Backup (Salvar)")
    print("Extra. Abrir Backup (Carregar)")
    print("7. Sair")
    print("="*30)

def adicionar_contato(contatos):
    print("\n--- Adicionar Novo Contato ---")
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()
    
    if not nome:
        print("Erro: O nome do contato não pode estar vazio!")
        return
    
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    contatos.append(contato)
    print(f"Sucesso! Contato '{nome}' foi adicionado.")

def listar_contatos(contatos):
    print("\n--- Lista de Contatos ---")
    if not contatos:
        print("Nenhum contato cadastrado na agenda.")
        return
    
    for i, contato in enumerate(contatos, 1):
        print(f"[{i}] Nome: {contato['nome']} | Telefone: {contato['telefone']} | E-mail: {contato['email']}")

def buscar_contato(contatos):
    print("\n--- Buscar Contato ---")
    if not contatos:
        print("A agenda está vazia.")
        return
        
    termo = input("Digite o nome (ou parte dele) para buscar: ").lower().strip()
    encontrados = [c for c in contatos if termo in c['nome'].lower()]
    
    if not encontrados:
        print("Nenhum contato encontrado com esse nome.")
        return
    
    print(f"\nForam encontrados {len(encontrados)} contato(s):")
    for contato in encontrados:
        print(f"- Nome: {contato['nome']} | Telefone: {contato['telefone']} | E-mail: {contato['email']}")

def atualizar_contato(contatos):
    print("\n--- Atualizar Contato ---")
    listar_contatos(contatos)
    if not contatos:
        return
    
    try:
        indice = int(input("\nDigite o número do contato que deseja atualizar: ")) - 1
        
        if 0 <= indice < len(contatos):
            contato_atual = contatos[indice]
            print(f"Editando contato: {contato_atual['nome']}")
            print("Dica: Pressione Enter sem digitar nada caso não queira alterar o campo.")
            
            novo_nome = input(f"Novo nome [{contato_atual['nome']}]: ").strip()
            novo_tel = input(f"Novo telefone [{contato_atual['telefone']}]: ").strip()
            novo_email = input(f"Novo e-mail [{contato_atual['email']}]: ").strip()
            
            if novo_nome:
                contato_atual['nome'] = novo_nome
            if novo_tel:
                contato_atual['telefone'] = novo_tel
            if novo_email:
                contato_atual['email'] = novo_email
                
            print("Contato atualizado com sucesso!")
        else:
            print("Número de contato inválido.")
    except ValueError:
        print("Por favor, digite apenas números válidos.")

def deletar_contato(contatos):
    print("\n--- Excluir Contato ---")
    listar_contatos(contatos)
    if not contatos:
        return
    
    try:
        indice = int(input("\nDigite o número do contato que deseja excluir: ")) - 1
        
        if 0 <= indice < len(contatos):
            removido = contatos.pop(indice)
            print(f"Contato '{removido['nome']}' excluído com sucesso!")
        else:
            print("Número de contato inválido.")
    except ValueError:
        print("Por favor, digite apenas números válidos.")

def verificar_backup():
    if os.path.exists(arquivo_agenda):
        tamanho = os.path.getsize(arquivo_agenda)
        timestamp_modificacao = os.path.getmtime(arquivo_agenda)
        hora_formatada = time.strftime('%d/%m/%Y às %H:%M:%S', time.localtime(timestamp_modificacao))
        
        print(f"\n[Status] O arquivo de backup '{arquivo_agenda}' existe!")
        print(f"-> Último salvamento: {hora_formatada}")
        print(f"-> Tamanho do arquivo: {tamanho} bytes")
    else:
        print(f"\n[Status] O arquivo '{arquivo_agenda}' ainda não foi criado.")

def criar_backup(contatos):
    with open(arquivo_agenda, 'w', encoding='utf-8') as f:
        json.dump(contatos, f, indent=4, ensure_ascii=False)
    print("Backup criado e contatos salvos com sucesso!")
    verificar_backup()

def carregar_backup():
    try:
        with open(arquivo_agenda, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            print("Backup carregado com sucesso!")
            return dados
    except FileNotFoundError:
        print("Ainda não existe nenhum arquivo de backup.")
        return []

def main():
    contatos = []
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == '1':
            adicionar_contato(contatos)
        elif opcao == '2':
            listar_contatos(contatos)
        elif opcao == '3':
            buscar_contato(contatos)
        elif opcao == '4':
            atualizar_contato(contatos)
        elif opcao == '5':
            deletar_contato(contatos)
        elif opcao == '6':
            criar_backup(contatos)
        elif opcao.lower() == 'extra':
            contatos = carregar_backup()
        elif opcao == '7':
            print("\nEncerrando a agenda. Até logo!")
            break
        else:
            print("\nOpção inválida! Por favor, escolha uma opção válida do menu.")

if __name__ == "__main__":
    main()