#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para análises dos dados de salários de cientistas de dados.
"""

import pandas as pd
import numpy as np
from pathlib import Path

def load_processed_data():
    """
    Carrega os dados processados.
    """
    file_path = Path('data/processed/data_scientists_salaries_processed.csv')
    
    if not file_path.exists():
        print("❌ Arquivo processado não encontrado.")
        print("Execute primeiro: python scripts/process_data.py")
        return None
    
    df = pd.read_csv(file_path)
    return df

def analyze_by_experience(df):
    """
    Análise de salários por nível de experiência.
    """
    print("\n" + "="*60)
    print("Análise: Salários por Nível de Experiência")
    print("="*60)
    
    experience_levels = {
        'EN': 'Entry Level',
        'MI': 'Mid Level',
        'SE': 'Senior',
        'EX': 'Executive'
    }
    
    analysis = df.groupby('experience_level')['salary_usd'].agg([
        ('Count', 'count'),
        ('Mean', 'mean'),
        ('Median', 'median'),
        ('Min', 'min'),
        ('Max', 'max'),
        ('Std Dev', 'std')
    ]).round(2)
    
    analysis.index = analysis.index.map(lambda x: experience_levels.get(x, x))
    print(analysis.to_string())

def analyze_by_country(df):
    """
    Análise de salários por país.
    """
    print("\n" + "="*60)
    print("Análise: Top 10 Países por Salário Médio")
    print("="*60)
    
    country_analysis = df.groupby('employee_residence')['salary_usd'].agg([
        ('Count', 'count'),
        ('Mean', 'mean'),
        ('Median', 'median')
    ]).sort_values('Mean', ascending=False).head(10).round(2)
    
    print(country_analysis.to_string())

def analyze_by_year(df):
    """
    Análise de tendências de salários ao longo dos anos.
    """
    print("\n" + "="*60)
    print("Análise: Tendências de Salários por Ano")
    print("="*60)
    
    year_analysis = df.groupby('work_year')['salary_usd'].agg([
        ('Count', 'count'),
        ('Mean', 'mean'),
        ('Median', 'median'),
        ('Min', 'min'),
        ('Max', 'max')
    ]).round(2)
    
    print(year_analysis.to_string())

def analyze_remote_work(df):
    """
    Análise de impacto do trabalho remoto nos salários.
    """
    print("\n" + "="*60)
    print("Análise: Impacto do Trabalho Remoto nos Salários")
    print("="*60)
    
    remote_mapping = {
        0: 'On-site',
        50: 'Hybrid',
        100: 'Fully Remote'
    }
    
    df['remote_type'] = df['remote_ratio'].map(remote_mapping)
    
    remote_analysis = df.groupby('remote_type')['salary_usd'].agg([
        ('Count', 'count'),
        ('Mean', 'mean'),
        ('Median', 'median')
    ]).round(2)
    
    print(remote_analysis.to_string())

def analyze_company_size(df):
    """
    Análise de salários por tamanho da empresa.
    """
    print("\n" + "="*60)
    print("Análise: Salários por Tamanho da Empresa")
    print("="*60)
    
    size_mapping = {
        'S': 'Small',
        'M': 'Medium',
        'L': 'Large'
    }
    
    df['company_size_name'] = df['company_size'].map(size_mapping)
    
    size_analysis = df.groupby('company_size_name')['salary_usd'].agg([
        ('Count', 'count'),
        ('Mean', 'mean'),
        ('Median', 'median')
    ]).round(2)
    
    print(size_analysis.to_string())

def main():
    """
    Executa todas as análises.
    """
    print("\n" + "#"*60)
    print("# Análises: Salários de Cientistas de Dados")
    print("#"*60)
    
    df = load_processed_data()
    if df is None:
        return
    
    analyze_by_experience(df)
    analyze_by_year(df)
    analyze_by_country(df)
    analyze_remote_work(df)
    analyze_company_size(df)
    
    print("\n" + "#"*60)
    print("# ✨ Análises Concluídas!")
    print("#"*60 + "\n")

if __name__ == '__main__':
    main()
