#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para baixar o dataset de salários de cientistas de dados do Kaggle.

Prerequisitos:
- Ter a biblioteca kaggle instalada: pip install kaggle
- Configurar credenciais do Kaggle (~/.kaggle/kaggle.json)
"""

import os
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset():
    """
    Baixa o dataset do Kaggle para a pasta data/raw/
    """
    # Criar diretório se não existir
    data_dir = Path('data/raw')
    data_dir.mkdir(parents=True, exist_ok=True)
    
    # Inicializar API do Kaggle
    api = KaggleApi()
    api.authenticate()
    
    print("📥 Iniciando download do dataset...")
    print("Dataset: Data Science Job Salaries (2020-2025)")
    
    # Dataset ID do Kaggle
    dataset_id = 'saurabhbadole/latest-data-science-job-salaries-2024'
    
    try:
        # Baixar o dataset
        api.dataset_download_files(
            dataset_id,
            path=str(data_dir),
            unzip=True
        )
        print(f"✅ Dataset baixado com sucesso em: {data_dir}")
        
        # Listar arquivos baixados
        files = list(data_dir.glob('*.csv'))
        print(f"\n📄 Arquivos encontrados:")
        for file in files:
            print(f"  - {file.name} ({file.stat().st_size / 1024:.2f} KB)")
            
    except Exception as e:
        print(f"❌ Erro ao baixar dataset: {e}")
        print("\n💡 Dica: Certifique-se de ter configurado as credenciais do Kaggle")
        print("   1. Acesse: https://www.kaggle.com/settings/account")
        print("   2. Clique em 'Create New API Token'")
        print("   3. Salve o arquivo kaggle.json em ~/.kaggle/")
        return False
    
    return True

if __name__ == '__main__':
    download_dataset()
