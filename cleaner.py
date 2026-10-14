import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Escopo com permissão total para mover para lixeira / deletar
SCOPES = ['https://mail.google.com/']

def autenticar():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def deletar_emails(query='label:INBOX'):
    creds = autenticar()
    service = build('gmail', 'v1', credentials=creds)

    print("Buscando e-mails...")
    total_deletados = 0

    while True:
        # Busca mensagens em lotes
        results = service.users().messages().list(userId='me', q=query, maxResults=500).execute()
        messages = results.get('messages', [])

        if not messages:
            print("Nenhum e-mail encontrado para o filtro especificado.")
            break

        print(f"Encontrados {len(messages)} e-mails no lote atual. Deletando...")

        # Deleta os e-mails encontrados em lote (batchDelete)
        message_ids = [msg['id'] for msg in messages]
        service.users().messages().batchDelete(
            userId='me',
            body={'ids': message_ids}
        ).execute()

        total_deletados += len(message_ids)
        print(f"Progresso: {total_deletados} e-mails excluídos.")

        # Se não houver próxima página, encerra
        if 'nextPageToken' not in results:
            break

    print(f"\nConcluído! Total de e-mails excluídos com sucesso: {total_deletados}")

if __name__ == '__main__':
    # Altere a query se quiser filtrar (ex: 'is:unread', 'category:promotions', 'older_than:30d')
    # Use 'in:anywhere' para buscar em todas as pastas
    deletar_emails(query='in:inbox')