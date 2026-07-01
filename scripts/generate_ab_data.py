# scripts/generate_ab_data.py
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from datetime import datetime

# ============================================
# KONFIGURASI DATABASE
# ============================================
DB_HOST = "db.qnspkmnmxnajcywwiwgk.supabase.co"
DB_USER = "postgres"
DB_PASSWORD = "AbTesting2024!"   # password Supabase
DB_NAME = "postgres"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# ============================================
# GENERATE DATA SIMULASI A/B TEST
# ============================================
np.random.seed(42)
n_users = 10000

# Buat data
df = pd.DataFrame({
    'user_id': range(1, n_users + 1),
    'group': np.random.choice(['A', 'B'], size=n_users, p=[0.5, 0.5]),
    'converted': np.random.choice([0, 1], size=n_users, p=[0.9, 0.1]),
    'timestamp': datetime.now()
})

# Tingkatkan conversion rate Group B (misal: A=10%, B=15%)
mask_b = df['group'] == 'B'
n_b = mask_b.sum()
df.loc[mask_b, 'converted'] = np.random.choice([0, 1], size=n_b, p=[0.85, 0.15])

# Simpan ke PostgreSQL
df.to_sql('ab_experiment', engine, if_exists='replace', index=False)

print(f"[OK] Data berhasil di-generate! {len(df)} baris.")
print(f"   Group A: {len(df[df['group']=='A'])} users")
print(f"   Group B: {len(df[df['group']=='B'])} users")
print(f"   Conversion A: {df[df['group']=='A']['converted'].mean()*100:.2f}%")
print(f"   Conversion B: {df[df['group']=='B']['converted'].mean()*100:.2f}%")
