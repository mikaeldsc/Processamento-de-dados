# Processamento de Dados - Salários de Cientistas de Dados

## 📊 Projeto
Análise e processamento de dados sobre salários de cientistas de dados usando dataset do Kaggle.

## 📁 Estrutura do Projeto
```
Processamento-de-dados/
├── data/                      # Dados
│   ├── raw/                   # Dados brutos do Kaggle
│   └── processed/             # Dados processados
├── notebooks/                 # Jupyter notebooks
│   └── eda.ipynb             # Análise Exploratória
├── scripts/                   # Scripts Python
│   ├── download_dataset.py   # Download do Kaggle
│   ├── process_data.py       # Processamento dos dados
│   └── analysis.py           # Análises
├── requirements.txt           # Dependências Python
└── README.md                 # Este arquivo
```

## 🎯 Dataset
**Data Science Job Salaries (2020-2025)**
- Fonte: [Kaggle](https://www.kaggle.com/datasets/saurabhbadole/latest-data-science-job-salaries-2024)
- Arquivo: `DataScience_salaries_2025.csv`
- Colunas principais:
  - `work_year`: Ano do registro
  - `experience_level`: Nível de experiência (EN, MI, SE, EX)
  - `employment_type`: Tipo de emprego (FT, PT, CT, FR)
  - `job_title`: Título do cargo
  - `salary`: Salário em moeda local
  - `salary_usd`: Salário em USD
  - `employee_residence`: País do funcionário
  - `remote_ratio`: Percentual de trabalho remoto
  - `company_location`: Localização da empresa
  - `company_size`: Tamanho da empresa (S, M, L)

## ⚙️ Configuração

### 1. Clonar o repositório
```bash
git clone https://github.com/mikaeldsc/Processamento-de-dados.git
cd Processamento-de-dados
```

### 2. Criar ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar credenciais do Kaggle
```bash
# Baixar arquivo de credenciais em: https://www.kaggle.com/settings/account
# Salvar em ~/.kaggle/kaggle.json (Linux/Mac) ou %USERPROFILE%\.kaggle\kaggle.json (Windows)
```

### 5. Executar download do dataset
```bash
python scripts/download_dataset.py
```

## 🔍 Análises Disponíveis

- **Exploratória (EDA):** Distribuição de salários, tendências por ano, experiência, país
- **Processamento:** Limpeza, transformação e preparação dos dados
- **Visualizações:** Gráficos de salários por nível de experiência, país, tipo de trabalho

## 📚 Executar

```bash
# Processar dados
python scripts/process_data.py

# Análises
python scripts/analysis.py

# Jupyter notebook
jupyter notebook notebooks/eda.ipynb
```

## 👨‍💻 Autor
Mikael DSC

## 📄 Licença
MIT
