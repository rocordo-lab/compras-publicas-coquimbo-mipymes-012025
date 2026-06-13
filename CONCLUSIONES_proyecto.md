# Conclusiones del Proyecto - Oportunidades de Compra Ágil en Coquimbo

## Resumen ejecutivo

Este análisis de **28,864 cotizaciones de Compra Ágil en Coquimbo (enero 2025)** demuestra que:

1. **Existe amplio espacio real para MiPymes** en Compra Ágil
2. **Tó´´´ner es el rubro con mayor oportunidad** (Í´ndice = 100/100)
3. **Municipalidades rurales** son los principales compradores
4. **Ticket promedio de $1.98M** está muy bajo el límite de 100 UTM (~$6.7M)

---

## Hallazgos principales

### 1. Volumen y oportunidad

- **Gasto total**: $57.1B CLP
- **Cotizaciones**: 28,864
- **Ticket promedio**: $1.98M (29.5% del límite)
- **100% MiPymes**: Todas las cotizaciones están clasificadas como MiPyme

**ConclusiÓ´n**: El mercado de Compra Ágil en Coquimbo es **accesible para empresas pequeñas**.

---

### 2. Top oportunidad: Tó´´´ner

**Razones para優先izar tó´´´ner**:

| MØ©trica | Valor |
|----------|-------|
| Frecuencia | 1,157 cotizaciones |
| Gasto total | $1.76B CLP |
| Ticket promedio | $1.5M |
| Ó­rganos compradores | 13 |
| Ó­ndice oportunidad | 100/100 |

**AcciÓ´n**: Ofrecer tó´´´n generiÓ©o o de marca a municipalidades rurales.

---

### 3. Municipalidades pequeñas dominantes

| Municipalidad | Cotizaciones | Gasto |
|---------------|--------------|-------|
| Montepatria | 2,894 | $6.7B |
| Salamanca | 2,445 | $4.8B |
| Canela | 2,353 | $8.2B |
| Coquimbo | 1,929 | $4.2B |

**ConclusiÓ´n**: **Municipalidades rurales** usan Compra Ágil como **mecanismo principal**, no solo para compras menores.

---

### 4. ConcentraciÓ´n de proveedores

- **ISEVEN LIMITADA**: 2,772 cotizaciones (9.6% del total)
- **C & S SPA**: 889 cotizaciones (3.1%)
- **TRANSPORTES CHILE SPA**: 769 cotizaciones (2.7%)

**ConclusiÓ´n**: Existe **concentraciÓ´n moderada** pero no monopolio absoluto.

---

## Recomendaciones para nuevas MiPymes

### 4 rubros prioritarios

1. **Tó´´´ner** (Ó´ndice = 100)
2. **Bolsas de basura** (Ó´ndice = 25.7)
3. **Desinfectantes domØ©sticos** (Ó´ndice = 21.0)
4. **Sillas** (Ó´ndice = 15.6)

### 4 Ó­rganos para acercarse

1. **Municipalidad de Montepatria** (2,894 cotizaciones)
2. **Municipalidad de Salamanca** (2,445 cotizaciones)
3. **Municipalidad de Canela** (2,353 cotizaciones)
4. **Municipalidad de Coquimbo** (1,929 cotizaciones)

---

## Métricas de éxito del proyecto

| Indicador | Valor |
|-----------|-------|
| Datos procesados | 28,864 cotizaciones |
| Organismos analizados | 10+ |
| Rubros analizados | 10+ |
| GrØ©ficos generados | 3 |
| Archivos exportados | 7 |
| Tiempo de análisis | 1 mes (enero 2025) |

---

## Herramientas y técnicas usadas

### Python y pandas

```python
import pandas as pd

# 1. Cargar datos
df1 = pd.read_csv("COT1_2025-01.csv", encoding="latin1")

# 2. Filtrar por región y fecha
df_coquimbo = df1[df1['Region'].str.contains('Coquimbo', na=False)]
df_enero_2025 = df_coquimbo[...]

# 3. Agrupar y sumar
top_organismos = df_enero_2025.groupby('RazonSocialUnidaddeCompra')['MontoTotal'].sum()

# 4. Calcular Ó­ndice
metrics_rubro['indice_oportunidad'] = frecuencia * (1/ticket_avg) * (1/concentracion)
```

### VisualizaciÓ´n

- matplotlib para grØ©ficos de barras
- GrØ©ficos: Top organismos, Top rubros, Ó­ndice de oportunidad

---

## Impacto potencial

### Para MiPymes

- **1,157 cotizaciones de tó´´´ner** = 1,157 oportunidades de venta
- **Ticket promedio $1.5M** = accesible para empresas pequeñas
- **13 Ó­rganos compradores** = diversificaciÓ´n de clientes

### Para Ó­rganos públicos

- **Reducir concentraciÓ´n** de proveedores actuales
- **Aumentar competitividad** en Compra Ágil
- **Acercarse a MiPymes regionales**

---

## Limitaciones del análisis

1. **Solo enero 2025**: No incluye otros meses
2. **Solo Coquimbo**: No compara con otras regiones
3. **Solo Compra Ágil**: No incluye licitaciones o Convenio Marco
4. **No incluye datos de adjudicaciÓ´n**: Solo cotizaciones, no ventas confirmadas

---

## Siguientes pasos recomendados

### Análisis extendido

1. **Anализar 12 meses** (2025 completo)
2. **Comparar con otras regiones** (ValparaO­so, Metropolitana)
3. **Incluir adjudicaciones** (no solo cotizaciones)
4. **Analizar Convenio Marco** y licitaciones

### AcciÓ´n para MiPymes

1. **Contactar municipalidades** objetivo
2. **Crear lista de productos** prioritarios
3. **Inscribirse en Registro de Proveedores**
4. **Participar en capacitaciones** de ChileCompra

---

## ConclusiÓ´n final

**Compra Ágil en Coquimbo es un mercado accesible para MiPymes**, con:

- $57.1B CLP de gasto total
- 28,864 cotizaciones
- Ticket promedio de $1.98M
- Tó´´´ner como rubro principal (Ó´ndice = 100)
- 13 Ó­rganos compradores activos

**RecomendaciÓ´n**: Priorizar **tó´´´ner, bolsas de basura, desinfectantes y sillas** como primeros rubros para entrar al mercado de compras públicas.

---

**Autor**: Proyecto de portafolio de Data Analyst  
**Fecha**: Enero 2025  
**Plataforma**: Google Colab + Python + pandas
