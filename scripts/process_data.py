#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para processar e limpar o dataset de salários de cientistas de dados.
"""

import pandas as pd
from pathlib import Path

def load_raw_data():
    """
    Carrega o arquivo CSV bruto.
    """
    data_dir = Path('data/raw')
    csv_files = list(data_dir.glob('*.csv'))
    
    if not csv_files:
        print("❌ Nenhum arquivo CSV encontrado em data/raw/")
        print("Execute primeiro: python scripts/download_dataset.py")
        return None
    
    file_path = csv_files[0]
    print(f"📂 Carregando arquivo: {file_path.name}")
    
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    """
    Realiza limpeza e transformação dos dados.
    """
    print("\n🧹 Iniciando limpeza dos dados...")
    
    # Copiar dataframe
    df_cleaned = df.copy()
    
    # Remover duplicatas
    duplicates_before = len(df_cleaned)
    df_cleaned = df_cleaned.drop_duplicates()
    duplicates_removed = duplicates_before - len(df_cleaned)
    if duplicates_removed > 0:
        print(f"  - Removidas {duplicates_removed} linhas duplicadas")
    
    # Tratar valores ausentes
    missing_values = df_cleaned.isnull().sum()
    if missing_values.sum() > 0:
        print(f"  - Valores ausentes encontrados:")
        print(missing_values[missing_values > 0])
        df_cleaned = df_cleaned.dropna()
    
    # Converter tipos de dados
    if 'work_year' in df_cleaned.columns:
        df_cleaned['work_year'] = df_cleaned['work_year'].astype('int32')
    if 'salary' in df_cleaned.columns:
        df_cleaned['salary'] = df_cleaned['salary'].astype('float64')
    if 'salary_usd' in df_cleaned.columns:
        df_cleaned['salary_usd'] = df_cleaned['salary_usd'].astype('float64')
    
    print(f"\n✅ Dados limpos. Total de linhas: {len(df_cleaned)}")
    return df_cleaned

def save_processed_data(df):
    """
    Salva os dados processados.
    """
    output_dir = Path('data/processed')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = output_dir / 'data_scientists_salaries_processed.csv'
    df.to_csv(output_file, index=False)
    print(f"💾 Dados processados salvos em: {output_file}")
    
    return output_file

def show_statistics(df):
    """
    Exibe estatísticas dos dados.
    """
    print("\n📊 Estatísticas dos Dados:")
    print(f"  - Total de registros: {len(df)}")
    print(f"  - Total de colunas: {len(df.columns)}")
    print(f"  - Anos cobertos: {df['work_year'].min()} a {df['work_year'].max()}")
    
    if 'salary_usd' in df.columns:
        print(f"\n💰 Salário (USD):")
        print(f"  - Mínimo: ${df['salary_usd'].min():,.2f}")
        print(f"  - Máximo: ${df['salary_usd'].max():,.2f}")
        print(f"  - Média: ${df['salary_usd'].mean():,.2f}")
        print(f"  - Mediana: ${df['salary_usd'].median():,.2f}")
    
    if 'experience_level' in df.columns:
        print(f"\n📈 Distribuição por Nível de Experiência:")
        exp_counts = df['experience_level'].value_counts()
        for level, count in exp_counts.items():
            print(f"  - {level}: {count} ({count/len(df)*100:.1f}%)")
    
    if 'job_title' in df.columns:
        print(f"\n💼 Top 5 Cargos Mais Comuns:")
        top_jobs = df['job_title'].value_counts().head(5)
        for job, count in top_jobs.items():
            print(f"  - {job}: {count}")

def main():
    """
    Executa o pipeline de processamento.
    """
    print("="*60)
    print("Processamento de Dados - Salários de Cientistas de Dados")
    print("="*60)
    
    # Carregar dados
    df = load_raw_data()
    if df is None:
        return
    
    # Limpar dados
    df_cleaned = clean_data(df)
    
    # Salvar dados processados
    save_processed_data(df_cleaned)
    
    # Mostrar estatísticas
    show_statistics(df_cleaned)
    
    print("\n✨ Processamento concluído com sucesso!")

if __name__ == '__main__':
    main()
