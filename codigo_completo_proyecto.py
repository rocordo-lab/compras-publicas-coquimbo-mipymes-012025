# Oportunidades de Compra Ágil en Coquimbo para nuevas MiPymes
# ============================================================
# Proyecto de Data Analyst - Análisis de compras públicas
# Fuente: Datos Abiertos ChileCompra (Mercado Público)
# Perí¿©do: Enero 2025
# Región: Coquimbo

# =============================================================================
# 1. IMPORTAR LIBRERÍ¡AS
# =============================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ConfiguraciÓ´n de visualizaciÓ´n
plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 12

# =============================================================================
# 2. MONTAR GOOGLE DRIVE
# =============================================================================
from google.colab import drive
drive.mount('/content/drive')

# =============================================================================
# 3. CARGAR DATOS
# =============================================================================
ruta_carpeta = "/content/drive/MyDrive/Proyecto_CompraAgil"

# Cargar CSV con separador correcto
df1 = pd.read_csv(
    ruta_carpeta + "/COT1_2025-01.csv",
    encoding="latin1",
    sep=";",
    engine="python",
    low_memory=False
)

print(f"✓ COT1 cargado: {len(df1)} registros")

# =============================================================================
# 4. CONVERTIR FECHAS Y MONTOS
# =============================================================================
df1['FechaPublicacionParaCotizar'] = pd.to_datetime(df1['FechaPublicacionParaCotizar'], errors='coerce')
df1['MontoTotal'] = pd.to_numeric(df1['MontoTotal'], errors='coerce')

# =============================================================================
# 5. FILTRAR POR COQUIMBO Y ENERO 2025
# =============================================================================
df_coquimbo = df1[df1['Region'].str.contains('Coquimbo', na=False)]
print(f"✓ Coquimbo: {len(df_coquimbo)} cotizaciones")

df_enero_2025 = df_coquimbo[
    (df_coquimbo['FechaPublicacionParaCotizar'] >= '2025-01-01') & 
    (df_coquimbo['FechaPublicacionParaCotizar'] <= '2025-01-31')
]
print(f"✓ Enero 2025: {len(df_enero_2025)} cotizaciones")

# =============================================================================
# 6. RESUMEN DE MØ©TRICAS
# =============================================================================
printφε"
"="*60)
print("RESUMEN DE MØ©TRICAS")
print("="*60)
print(f"Gasto total: ${df_enero_2025['MontoTotal'].sum():.0f} CLP")
print(f"Cotizaciones: {len(df_enero_2025)}")
print(f"Ticket promedio: ${df_enero_2025['MontoTotal'].mean():.0f} CLP")
print(f"Ticket máximo: ${df_enero_2025['MontoTotal'].max():.0f} CLP")
print(f"Ticket mínimo: ${df_enero_2025['MontoTotal'].min():.0f} CLP")

# =============================================================================
# 7. TOP 10 ORGANISMOS POR GASTO
# =============================================================================
top_organismos = df_enero_2025.groupby('RazonSocialUnidaddeCompra')['MontoTotal'].sum().sort_values(ascending=False).head(10)
print(φ"
"="*60)
print("TOP 10 ORGANISMOS POR GASTO")
print("="*60)
print(top_organismos)

# =============================================================================
# 8. TOP 10 RUBROS POR GASTO
# =============================================================================
top_rubros = df_enero_2025.groupby('NombreProductoGenerico')['MontoTotal'].sum().sort_values(ascending=False).head(10)
print(φ"
"="*60)
print("TOP 10 RUBROS POR GASTO")
print("="*60)
print(top_rubros)

# =============================================================================
# 9. TOP 10 RUBROS POR FRECUENCIA
# =============================================================================
top_rubros_frecuencia = df_enero_2025.groupby('NombreProductoGenerico')['CodigoCotizacion'].count().sort_values(ascending=False).head(10)
print(φ"
"="*60)
print("TOP 10 RUBROS POR FRECUENCIA")
print("="*60)
print(top_rubros_frecuencia)

# =============================================================================
# 10. TOP 10 PROVEEDORES POR COTIZACIONES
# =============================================================================
top_proveedores = df_enero_2025.groupby('RazonSocialProveedor')['CodigoCotizacion'].count().sort_values(ascending=False).head(10)
print(φ"
"="*60)
print("TOP 10 PROVEEDORES POR COTIZACIONES")
print("="*60)
print(top_proveedores)

# =============================================================================
# 11. Ó­NDICE DE OPORTUNIDAD PARA MiPyme
# =============================================================================
metrics_rubro = df_enero_2025.groupby('NombreProductoGenerico').agg({
    'MontoTotal': ['sum', 'mean', 'count'],
    'CodigoCotizacion': 'count'
})

metrics_rubro.columns = ['gasto_total', 'ticket_avg', 'frecuencia', 'freq_cot']

num_org_rubro = df_enero_2025.groupby('NombreProductoGenerico')['RazonSocialUnidaddeCompra'].nunique()
metrics_rubro['num_org'] = num_org_rubro

metrics_rubro['concentracion'] = 1 / metrics_rubro['num_org']

metrics_rubro['indice_oportunidad'] = (
    metrics_rubro['frecuencia'] * 
    (1 / metrics_rubro['ticket_avg']) * 
    (1 / metrics_rubro['concentracion'])
)

metrics_rubro['indice_norm'] = (
    (metrics_rubro['indice_oportunidad'] - metrics_rubro['indice_oportunidad'].min()) / 
    (metrics_rubro['indice_oportunidad'].max() - metrics_rubro['indice_oportunidad'].min()) * 100
)

top_oportunidades = metrics_rubro.sort_values('indice_norm', ascending=False).head(10)
print(φ"
"="*60)
print("TOP 10 RUBROS POR Ó­NDICE DE OPORTUNIDAD (MiPyme)")
print("="*60)
print(top_oportunidades[['gasto_total', 'ticket_avg', 'frecuencia', 'num_org', 'indice_norm']])

# =============================================================================
# 12. GRØ©FICOS
# =============================================================================

# GrØ©fico 1: Top organismos por gasto
top_org = df_enero_2025.groupby('RazonSocialUnidaddeCompra')['MontoTotal'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(14, 8))
plt.barh(top_org.index, top_org.values, color='#01696f')
plt.xlabel('Gasto Total (CLP)')
plt.ylabel('Organismo')
plt.title('Top 10 Organismos por Gasto en Compra Ágil (Coquimbo - enero 2025)')
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1e9:.1f}B'))
plt.tight_layout()
plt.savefig('top_organismos_gasto.png', dpi=300)
print("✓ GrØ©fico 1: top_organismos_gasto.png")

# GrØ©fico 2: Top rubros por frecuencia
top_rubro_freq = df_enero_2025.groupby('NombreProductoGenerico')['CodigoCotizacion'].count().sort_values(ascending=False).head(10)
plt.figure(figsize=(14, 8))
plt.barh(top_rubro_freq.index, top_rubro_freq.values, color='#4ECDC4')
plt.xlabel('Numeor de Cotizaciones')
plt.ylabel('Producto Generi?o')
plt.title('Top 10 Productos por Frecuencia de Cotizaciones (Coquimbo - enero 2025)')
plt.tight_layout()
plt.savefig('top_rubros_frecuencia.png', dpi=300)
print("✓ GrØ©fico 2: top_rubros_frecuencia.png")

# GrØ©fico 3: Ø­ndice de oportunidad
top_op = top_oportunidades.sort_values('indice_norm', ascending=False).head(10)
plt.figure(figsize=(14, 8))
plt.barh(top_op.index, top_op['indice_norm'], color='#FF6B6B')
plt.xlabel('Ø´ndice de Oportunidad (0-100)')
plt.ylabel('Producto Generi?o')
plt.title('Top 10 Rubros con Mayor Oportunidad para MiPyme (Coquimbo - enero 2025)')
plt.tight_layout()
plt.savefig('indice_oportunidad.png', dpi=300)
print("✓ GrØ©fico 3: indice_oportunidad.png")

# =============================================================================
# 13. EXPORTAR RESULTADOS
# =============================================================================
df_enero_2025.to_csv('coquimbo_compra_agil_enero_2025_clean.csv', index=False)
print("✓ Dataset: coquimbo_compra_agil_enero_2025_clean.csv")

df_enero_2025.groupby('RazonSocialUnidaddeCompra').agg({
    'MontoTotal': ['sum', 'mean', 'count']
}).to_csv('metrics_organismos.csv', index=False)
print("✓ MØ©tricas organismos: metrics_organismos.csv")

metrics_rubro.to_csv('metrics_rubros.csv', index=False)
print("✓ MØ©tricas rubros: metrics_rubros.csv")

top_oportunidades.to_csv('top_oportunidades_emt.csv', index=False)
print("✓ Top oportunidades: top_oportunidades_emt.csv")

print(φ"
"="*60)
print("PROYECTO COMPLETO")
print("="*60)
