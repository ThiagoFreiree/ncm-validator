📦 NCM Validator

Validador de códigos NCM (Nomenclatura Comum do Mercosul) desenvolvido em Python.

O projeto permite:

✅ Validar códigos NCM

📊 Exibir resumo de válidos e inválidos

📝 Gerar log estruturado da execução

📁 Exportar resultados para CSV

🚀 Pronto para versionamento com Git

📌 O que é NCM?

NCM (Nomenclatura Comum do Mercosul) é um código de 8 dígitos utilizado para classificar mercadorias no Brasil e demais países do Mercosul.

Este projeto valida se o NCM:

Possui exatamente 8 dígitos

Contém apenas números

Não está vazio ou nulo

🧠 Regras de Validação
Condição	Resultado
8 dígitos numéricos	OK
Menos ou mais de 8 dígitos	NCM INVÁLIDO
Contém letras	NCM INVÁLIDO
None ou vazio	SEM NCM
🗂 Estrutura do Projeto
RPA_PYTHON/
│
├── main.py
├── validator.py
├── exporter.py
├── logger_config.py
├── requirements.txt
├── resultado_ncm.csv
├── ncm.log
└── .gitignore

⚙️ Instalação
1️⃣ Criar ambiente virtual
python -m venv .venv


Ativar:

Windows:

.venv\Scripts\activate


Linux/macOS:

source .venv/bin/activate

2️⃣ Instalar dependências
pip install -r requirements.txt

▶️ Como Executar
python main.py

📤 Saídas Geradas

Após execução:

📝 Log

Arquivo:

ncm.log


Contém:

Início da execução

Status de cada NCM

Resumo final

📊 CSV Exportado

Arquivo:

resultado_ncm.csv


Formato:

NCM	Status
12345678	OK
1234	NCM INVÁLIDO
None	SEM NCM
📈 Resumo de Execução

Ao final da execução o sistema mostra:

Total analisados: X
Válidos: Y
Inválidos: Z

🛠 Tecnologias Utilizadas

Python 3.14+

logging

colorlog

csv

Git

🔒 .gitignore recomendado
.venv/
__pycache__/
*.pyc
ncm.log
resultado_ncm.csv

🚀 Próximas Evoluções

Possíveis melhorias:

Integração com banco de dados

Leitura de NCM via arquivo CSV externo

Interface CLI com argumentos

Integração com API fiscal

Pipeline automatizado

👨‍💻 Autor

Thiago Freire Barbosa
