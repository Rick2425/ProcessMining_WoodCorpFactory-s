import base64
from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ------------------------------------------------------------------
# Configuración de la página
# ------------------------------------------------------------------
st.set_page_config(page_title="Caso WoodCorp - Factory", layout="wide")

# ------------------------------------------------------------------
# Encabezado con logos
# Los archivos deben estar en la misma carpeta que este script.
# ------------------------------------------------------------------
CARPETA = Path(__file__).parent
ALTURA_LOGO = 90  # px; todos los logos se ajustan a esta altura manteniendo su proporción

LOGOS = [
    ("escudo unalm.jpg", "image/jpeg", "Escudo UNALM"),
    ("escudo facultad.png", "image/png", "Facultad de Economía y Planificación"),
    ("daeilogo.jpg", "image/jpeg", "DAEI - UNALM"),
]


def logo_html(nombre, mime, alt):
    ruta = CARPETA / nombre
    if not ruta.exists():
        return f"<small>⚠️ Falta: {nombre}</small>"
    datos = base64.b64encode(ruta.read_bytes()).decode()
    return (f'<img src="data:{mime};base64,{datos}" alt="{alt}" '
            f'style="height:{ALTURA_LOGO}px; width:auto;">')


cols = st.columns([1, 1, 1, 7], vertical_alignment="center")
for col, (nombre, mime, alt) in zip(cols[:3], LOGOS):
    col.markdown(logo_html(nombre, mime, alt), unsafe_allow_html=True)
cols[3].title("Caso WoodCorp - Factory")

st.markdown("---")

# ------------------------------------------------------------------
# KPIs generales (extraídos del dashboard de Celonis)
# ------------------------------------------------------------------
kpi_actual = 64
meta = 80
costo_penalidades = 11824768.50
volumen_total = 47740004

# ------------------------------------------------------------------
# Datos
# ------------------------------------------------------------------
datos_plantas = pd.DataFrame({
    'Planta': ['Essen', 'Aachen', 'Bonn', 'Crefeld', 'Duisburg', 'Wuppertal'],
    'Volumen (kg)': [30682060, 13543511, 2634529, 496785, 247324, 135795],
    'Entregas a Tiempo (%)': [66, 61, 69, 70, 69, 88],
    'Penalidades (€)': [7591272.00, 3374145.00, 632161.50, 162244.50, 62973.00, 1972.50]
})

datos_tipo = pd.DataFrame({
    'Tipo de Almacén': ['Automated', 'Non-automated'],
    'Volumen de Despacho (kg)': [102681, 47637323],
    'Entregas a Tiempo (%)': [79.59, 64.42],
    'Penalización Generada (€)': [14001.75, 11810766.75]
})

datos_detalle = pd.DataFrame({
    'Planta': ['Essen', 'Aachen', 'Bonn', 'Crefeld', 'Duisburg', 'Wuppertal',
               'Bonn', 'Aachen', 'Duisburg', 'Wuppertal'],
    'Tipo de Almacén': ['Non-automated'] * 6 + ['Automated'] * 4,
    'Volumen (kg)': [30682060, 13535524, 2555069, 496785, 232845, 135040,
                     79460, 7987, 14479, 755],
    'Entregas a Tiempo (%)': [65.62, 61.42, 68.76, 70.11, 67.72, 85.71,
                              77.78, 66.67, 100.00, 100.00],
    'Penalidades (€)': [7591272.00, 3372582.00, 619722.75, 162244.50, 62973.00,
                        1972.50, 12438.75, 1563.00, 0.00, 0.00]
})

# Pareto de penalidades por planta
pareto = datos_plantas.sort_values('Penalidades (€)', ascending=False).reset_index(drop=True)
pareto['% Acumulado'] = pareto['Penalidades (€)'].cumsum() / pareto['Penalidades (€)'].sum() * 100
pct_top2 = pareto.loc[1, '% Acumulado']  # Essen + Aachen

# Penalidades mensuales por fábrica (gráfico de Celonis 2018-2019).
# Si existe "penalidades_mensuales.csv" junto al script (columnas: Mes, Essen,
# Aachen, Bonn, Others) se usa ese archivo con los datos reales. Si no, se usa
# una aproximación leída del gráfico, reescalada a los totales por planta.
ARCHIVO_MENSUAL = CARPETA / "penalidades_mensuales.csv"


@st.cache_data
def cargar_penalidades_mensuales():
    if ARCHIVO_MENSUAL.exists():
        return pd.read_csv(ARCHIVO_MENSUAL, parse_dates=['Mes']), False

    meses = pd.date_range('2018-01-01', periods=24, freq='MS')
    estimado_miles = {
        'Essen':  [302, 287, 308, 385, 474, 306, 449, 287, 198, 249, 319, 519,
                   349, 580, 298, 329, 404, 223, 385, 338, 411, 215, 5, 10],
        'Aachen': [147, 140, 168, 142, 115, 128, 124, 88, 139, 139, 135, 177,
                   202, 222, 203, 245, 231, 130, 225, 124, 119, 41, 3, 2],
        'Bonn':   [48, 48, 31, 59, 58, 14, 9, 11, 26, 58, 60, 40,
                   24, 54, 13, 3, 2, 43, 17, 18, 2, 0, 0, 0],
        'Others': [10, 3, 6, 3, 9, 6, 9, 8, 8, 11, 9, 12,
                   17, 15, 6, 17, 18, 6, 8, 18, 5, 8, 3, 0],
    }
    totales = {
        'Essen': 7591272.00,
        'Aachen': 3374145.00,
        'Bonn': 632161.50,
        'Others': 162244.50 + 62973.00 + 1972.50,  # Crefeld + Duisburg + Wuppertal
    }
    df = pd.DataFrame({'Mes': meses})
    for fabrica, valores in estimado_miles.items():
        serie = pd.Series(valores, dtype=float)
        df[fabrica] = serie * totales[fabrica] / serie.sum()
    return df, True

# ------------------------------------------------------------------
# Pestañas
# ------------------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 1. Presentación del Caso y KPI",
    "📦 2. Conformidad y Entregas a Tiempo",
    "🏭 3. Distribución de Almacenes",
    "✅ 4. Conclusiones y Recomendaciones",
])

# ------------------------------------------------------------------
# TAB 1
# ------------------------------------------------------------------
with tab1:
    st.header("Presentación del Caso WoodCorp y Definición de KPI")
    st.markdown(f'''
    **Contexto del Problema:** WoodCorp enfrenta altos costos por penalidades asociadas a entregas que no cumplen con los tiempos establecidos.

    **Métrica Principal (KPI):** Porcentaje de Entregas a Tiempo.
    - **Meta de Cumplimiento Ideal:** {meta}%
    - **Desempeño Actual (Global):** {kpi_actual}%
    ''')

    col1, col2, col3 = st.columns(3)
    col1.metric(
        label="Tasa de Entregas a Tiempo",
        value=f"{kpi_actual}%",
        delta=f"{kpi_actual - meta} pp vs meta",
        delta_color="normal",  # negativo = rojo
    )
    col2.metric(label="Costo Total por Penalidades", value=f"€ {costo_penalidades:,.2f}")
    col3.metric(label="Volumen Total Despachado (kg)", value=f"{volumen_total:,}")

    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=kpi_actual,
        delta={'reference': meta, 'position': "top"},
        title={'text': "Tasa de Entregas a Tiempo (%)"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#1f2937"},
            'steps': [
                {'range': [0, kpi_actual], 'color': "#d62728"},
                {'range': [kpi_actual, meta], 'color': "#ff7f0e"},
                {'range': [meta, 100], 'color': "#2ca02c"},
            ],
            'threshold': {'line': {'color': "black", 'width': 4},
                          'thickness': 0.75, 'value': meta},
        }
    ))
    st.plotly_chart(fig_gauge, width="stretch")

# ------------------------------------------------------------------
# TAB 2
# ------------------------------------------------------------------
with tab2:
    st.header("Conformidad del Volumen de Despacho y Entregas a Tiempo")

    st.dataframe(
        datos_plantas.style.format({
            'Volumen (kg)': '{:,.0f}',
            'Entregas a Tiempo (%)': '{:.0f}%',
            'Penalidades (€)': '€ {:,.2f}',
        }),
        hide_index=True,
        width="stretch",
    )

    col1, col2 = st.columns(2)
    with col1:
        fig_vol = px.bar(
            datos_plantas.sort_values('Volumen (kg)', ascending=True),
            x='Volumen (kg)', y='Planta', orientation='h',
            title='Volumen de Entrega por Planta',
            color_discrete_sequence=['#8c92ac'],
        )
        st.plotly_chart(fig_vol, width="stretch")

    with col2:
        fig_time = px.bar(
            datos_plantas.sort_values('Entregas a Tiempo (%)', ascending=True),
            x='Entregas a Tiempo (%)', y='Planta', orientation='h',
            title='Tasa de Entregas a Tiempo por Planta',
            color_discrete_sequence=['#4cb18c'],
            hover_data=['Volumen (kg)'],
        )
        fig_time.add_vline(x=meta, line_dash="dash", line_color="red",
                           annotation_text=f"Meta ({meta}%)")
        st.plotly_chart(fig_time, width="stretch")

    # Penalidades mensuales por fábrica
    st.subheader("Penalidades generadas por las Fábricas entre los años 2018-2020")
    df_mensual, es_estimado = cargar_penalidades_mensuales()
    df_largo = df_mensual.melt(id_vars='Mes', var_name='Fábrica',
                               value_name='Penalidades (€)')
    orden = ['Essen', 'Aachen', 'Bonn', 'Others']
    fig_mensual = px.line(
        df_largo, x='Mes', y='Penalidades (€)', color='Fábrica',
        category_orders={'Fábrica': orden},
        color_discrete_map={'Essen': '#1a2fd6', 'Aachen': '#3d5afe',
                            'Bonn': '#8fa8f0', 'Others': '#7f8398'},
    )
    fig_mensual.update_traces(line=dict(width=2.5))
    fig_mensual.update_layout(
        hovermode='x unified',
        legend=dict(orientation='h', y=-0.25, x=0.5, xanchor='center'),
    )
    fig_mensual.update_xaxes(title='Mes', tickformat='%b %Y')
    fig_mensual.update_yaxes(tickformat=',.0f')
    st.plotly_chart(fig_mensual, width="stretch")
    st.caption(f"Essen y Aachen concentran el {pct_top2:.1f}% de las penalidades totales.")
    if es_estimado:
        st.caption(
            "ℹ️ Valores mensuales aproximados, leídos del gráfico de Celonis y "
            "reescalados para coincidir con los totales por planta. Para usar los datos "
            "exactos, agrega `penalidades_mensuales.csv` junto a la app."
        )

# ------------------------------------------------------------------
# TAB 3
# ------------------------------------------------------------------
with tab3:
    st.header("Distribución de Almacenes: Automáticos vs Manuales")

    pct_vol_auto = datos_tipo.loc[0, 'Volumen de Despacho (kg)'] / datos_tipo['Volumen de Despacho (kg)'].sum() * 100
    st.info(
        f"⚠️ Los almacenes automatizados manejan solo el {pct_vol_auto:.2f}% del volumen total. "
        "Su mejor desempeño proviene de muestras muy pequeñas y no es comparable "
        "directamente con el de los almacenes no automatizados."
    )

    st.dataframe(
        datos_tipo.style.format({
            'Volumen de Despacho (kg)': '{:,.0f}',
            'Entregas a Tiempo (%)': '{:.2f}%',
            'Penalización Generada (€)': '€ {:,.2f}',
        }),
        hide_index=True,
        width="stretch",
    )

    st.subheader("Desempeño Detallado por Planta y Tipo de Almacén")
    st.dataframe(
        datos_detalle.style.format({
            'Volumen (kg)': '{:,.0f}',
            'Entregas a Tiempo (%)': '{:.2f}%',
            'Penalidades (€)': '€ {:,.2f}',
        }),
        hide_index=True,
        width="stretch",
    )

    fig_tech = px.bar(
        datos_detalle, x='Planta', y='Entregas a Tiempo (%)',
        color='Tipo de Almacén', barmode='group',
        title='Tasa de Entregas a Tiempo por Planta y Tipo de Tecnología',
        hover_data=['Volumen (kg)', 'Penalidades (€)'],
    )
    fig_tech.add_hline(y=meta, line_dash="dash", line_color="red",
                       annotation_text=f"Meta ({meta}%)")
    st.plotly_chart(fig_tech, width="stretch")

# ------------------------------------------------------------------
# TAB 4
# ------------------------------------------------------------------
with tab4:
    st.header("Conclusiones y Recomendaciones")

    st.subheader("Hallazgos principales")
    st.markdown(f'''
    - La tasa global de entregas a tiempo es de **{kpi_actual}%**, **{meta - kpi_actual} pp por debajo** de la meta de {meta}%.
    - Las penalidades totales ascienden a **€ {costo_penalidades:,.2f}**.
    - **Essen y Aachen concentran el {pct_top2:.1f}% de las penalidades**, por su alto volumen y su desempeño bajo la meta (66% y 61%).
    - Los almacenes automatizados cumplen mejor ({datos_tipo.loc[0, 'Entregas a Tiempo (%)']:.2f}%), pero representan solo el {pct_vol_auto:.2f}% del volumen: la evidencia no basta para atribuir la mejora a la tecnología.
    - Wuppertal es la única planta que supera la meta (88%), aunque con un volumen reducido.
    ''')

    st.subheader("Recomendaciones sugeridas")
    st.markdown('''
    1. **Priorizar Essen y Aachen** en el análisis de causa raíz de los retrasos (mayor impacto en costo).
    2. **Analizar las prácticas de Wuppertal** y evaluar si son replicables en plantas de mayor volumen.
    3. **Evaluar un piloto de automatización** en Essen o Aachen antes de decidir una inversión, con seguimiento del KPI y de las penalidades.
    4. **Monitorear el KPI de forma continua** por planta y tipo de almacén, con alertas cuando caiga bajo la meta.
    ''')