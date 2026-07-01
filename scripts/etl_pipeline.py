import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from scipy.stats import chi2_contingency

# ============================================
# KONFIGURASI DATABASE
# ============================================
DB_USER = "postgres"
DB_PASSWORD = "postgre"  
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "ab_testing"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# ============================================
# ETL PIPELINE
# ============================================
print("[INFO] Memulai ETL Pipeline...")

# --- Extract ---
df = pd.read_sql("SELECT * FROM ab_experiment", engine)
print(f"[OK] Data diekstrak: {len(df)} baris")

# --- Transform ---
# Agregasi per group
summary = df.groupby('group').agg(
    total_users=('user_id', 'count'),
    converted=('converted', 'sum'),
    conversion_rate=('converted', 'mean')
).reset_index()

# A/B Test (Chi-Square)
contingency = pd.crosstab(df['group'], df['converted'])
chi2, p_value, dof, expected = chi2_contingency(contingency)

# Hitung lift (peningkatan relatif)
conv_a = summary[summary['group']=='A']['conversion_rate'].values[0]
conv_b = summary[summary['group']=='B']['conversion_rate'].values[0]
lift = (conv_b - conv_a) / conv_a * 100

# Tambahkan ke summary
summary['p_value'] = p_value
summary['significant'] = p_value < 0.05
summary['lift_pct'] = lift if p_value < 0.05 else 0

# --- Load ---
summary.to_sql('ab_summary', engine, if_exists='replace', index=False)

print("\n[RESULT] HASIL A/B TEST")
print("="*50)
print(f"Group A Conversion: {conv_a*100:.2f}%")
print(f"Group B Conversion: {conv_b*100:.2f}%")
print(f"Lift: {lift:.2f}%")
print(f"P-Value: {p_value:.4f}")
print(f"Signifikan: {'YA' if p_value < 0.05 else 'TIDAK'}")
print("="*50)

if p_value < 0.05:
    print("[RECOMMENDATION] Deploy perubahan! Group B lebih baik secara signifikan.")
else:
    print("[RECOMMENDATION] Jangan deploy. Perbedaan tidak signifikan.")