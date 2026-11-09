import json
import os
import time

arq_ag = "contatos.json"

def ver_mn():
    print("\n" + "="*30)
    print("        AGENDA DE CONTATOS       ")
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

def cad_contat(cts):
    print("\n--- Adicionar Novo Contato ---")
    nom = input("Nome: ").strip()
    tel = input("Telefone: ").strip()
    eml = input("E-mail: ").strip()
    
    if not nom:
        print("Erro: O nome do contato não pode estar vazio!")
        return
    
    ctt = {
        "nome": nom,
        "telefone": tel,
        "email": eml
    }
    cts.append(ctt)
    print(f"Sucesso! Contato '{nom}' foi adicionado.")

def list_cont(cts):
    print("\n--- Lista de Contatos ---")
    if not cts:
        print("Nenhum contato cadastrado na agenda.")
        return
    
    for i, ctt in enumerate(cts, 1):
        print(f"[{i}] Nome: {ctt['nome']} | Telefone: {ctt['telefone']} | E-mail: {ctt['email']}")

def bsc_cont(cts):
    print("\n--- Buscar Contato ---")
    if not cts:
        print("A agenda está vazia.")
        return
        
    trm = input("Digite o nome (ou parte dele) para buscar: ").lower().strip()
    enc = [c for c in cts if trm in c['nome'].lower()]
    
    if not enc:
        print("Nenhum contato encontrado com esse nome.")
        return
    
    print(f"\nForam encontrados {len(enc)} contato(s):")
    for ctt in enc:
        print(f"- Nome: {ctt['nome']} | Telefone: {ctt['telefone']} | E-mail: {ctt['email']}")

def atu_cont(cts):
    print("\n--- Atualizar Contato ---")
    list_cont(cts)
    if not cts:
        return
    
    try:
        idx = int(input("\nDigite o número do contato que deseja atualizar: ")) - 1
        
        if 0 <= idx < len(cts):
            ctt_at = cts[idx]
            print(f"Editando contato: {ctt_at['nome']}")
            print("Dica: Pressione Enter sem digitar nada caso não queira alterar o campo.")
            
            nov_nom = input(f"Novo nome [{ctt_at['nome']}]: ").strip()
            nov_tel = input(f"Novo telefone [{ctt_at['telefone']}]: ").strip()
            nov_eml = input(f"Novo e-mail [{ctt_at['email']}]: ").strip()
            
            if nov_nom:
                ctt_at['nome'] = nov_nom
            if nov_tel:
                ctt_at['telefone'] = nov_tel
            if nov_eml:
                ctt_at['email'] = nov_eml
                
            print("Contato atualizado com sucesso!")
        else:
            print("Número de contato inválido.")
    except ValueError:
        print("Por favor, digite apenas números válidos.")

def exc_cont(cts):
    print("\n--- Excluir Contato ---")
    list_cont(cts)
    if not cts:
        return
    
    try:
        idx = int(input("\nDigite o número do contato que deseja excluir: ")) - 1
        
        if 0 <= idx < len(cts):
            rmv = cts.pop(idx)
            print(f"Contato '{rmv['nome']}' excluído com sucesso!")
        else:
            print("Número de contato inválido.")
    except ValueError:
        print("Por favor, digite apenas números válidos.")

def vrf_bkp():
    if os.path.exists(arq_ag):
        tam = os.path.getsize(arq_ag)
        ts_mod = os.path.getmtime(arq_ag)
        hr_fmt = time.strftime('%d/%m/%Y às %H:%M:%S', time.localtime(ts_mod))
        
        print(f"\n[Status] O arquivo de backup '{arq_ag}' existe!")
        print(f"-> Último salvamento: {hr_fmt}")
        print(f"-> Tamanho do arquivo: {tam} bytes")
    else:
        print(f"\n[Status] O arquivo '{arq_ag}' ainda não foi criado.")

def cri_bkp(cts):
    with open(arq_ag, 'w', encoding='utf-8') as f:
        json.dump(cts, f, indent=4, ensure_ascii=False)
    print("Backup criado e contatos salvos com sucesso!")
    vrf_bkp()

def car_bkp():
    try:
        with open(arq_ag, 'r', encoding='utf-8') as f:
            dds = json.load(f)
            print("Backup carregado com sucesso!")
            return dds
    except FileNotFoundError:
        print("Ainda não existe nenhum arquivo de backup.")
        return []

def main():
    cts = []
    while True:
        ver_mn()
        opc = input("\nEscolha uma opção: ").strip()
        
        if opc == '1':
            cad_contat(cts)
        elif opc == '2':
            list_cont(cts)
        elif opc == '3':
            bsc_cont(cts)
        elif opc == '4':
            atu_cont(cts)
        elif opc == '5':
            exc_cont(cts)
        elif opc == '6':
            cri_bkp(cts)
        elif opc.lower() == 'extra':
            cts = car_bkp()
        elif opc == '7':
            print("\nEncerrando a agenda. Até logo!")
            break
        else:
            print("\nOpção inválida! Por favor, escolha uma opção válida do menu.")

if __name__ == "__main__":
    main()
