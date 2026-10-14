Gmail Cleaner
Python · Gmail API · OAuth 2.0

🇧🇷 Sobre o projeto
Aplicação em Python para automatizar o gerenciamento de e-mails utilizando a Gmail API e autenticação OAuth 2.0. O projeto utiliza processamento em lotes e paginação para lidar com mensagens, buscando reduzir tarefas repetitivas com foco em segurança e eficiência.

🇺🇸 About the project
Python application for automating email management using the Gmail API and OAuth 2.0 authentication. The project uses batch processing and pagination to handle messages, reducing repetitive tasks while focusing on security and efficiency.

## Features

- Gmail API integration using OAuth 2.0
- Python automation executed through the Linux terminal
- Command-line execution in Kali Linux
- Batch deletion of email messages using the Gmail API
- Email filtering through Gmail search queries
- Progress reporting during execution
- OAuth token storage and credential refresh

## Technologies

- Python 3
- Kali Linux
- Linux command-line interface (CLI)
- Gmail API
- OAuth 2.0
- Google Cloud Platform
- REST API
- JSON

## Prerequisites

- Kali Linux or another compatible Linux distribution
- Python 3
- pip
- A Google account
- A Google Cloud project with the Gmail API enabled

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/john-root-opsec/gmail-cleaner.git
cd gmail-cleaner
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

## Google Cloud Setup

1. Create a project in the [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the Gmail API.
3. Configure the OAuth consent screen and add your Google account as a test user if required.
4. Create OAuth client credentials for a desktop application.
5. Download the credentials JSON file and save it as `credentials.json` in the project directory.

**Security:** Never upload `credentials.json` or `token.json` to GitHub.

## Usage

### 1. Open the project in the terminal

Navigate to the project directory:

```bash
cd gmail-cleaner
```

### 2. Activate the virtual environment

```bash
source venv/bin/activate
```

### 3. Run the Python script

```bash
python3 cleaner.py
```

On the first run, the script opens a local authorization flow through your browser so you can authorize Gmail access using OAuth 2.0.

After authorization, the script stores the access token locally in `token.json` and starts processing messages matching the configured Gmail search query.

The terminal displays progress and the number of messages deleted.

### Important Warning

This script uses the Gmail API's `batchDelete` method, which permanently deletes messages without asking for confirmation. Test with a suitable account before running it on important mailboxes.

## Project Status

Personal Python automation project developed and executed in a Kali Linux terminal. It demonstrates Gmail API integration, OAuth 2.0 authentication, Python scripting, virtual environment management, and automated email processing.
