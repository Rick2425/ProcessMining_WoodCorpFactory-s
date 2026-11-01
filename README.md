<p align="center">
  <img src="escudo%20unalm.jpg" alt="UNALM" height="90">
  &nbsp;&nbsp;&nbsp;
  <img src="escudo%20facultad.png" alt="Facultad de Economía y Planificación" height="90">
  &nbsp;&nbsp;&nbsp;
  <img src="daeilogo.jpg" alt="DAEI" height="90">
</p>

<h1 align="center">Caso WoodCorp – Factory</h1>

<p align="center">
  Análisis de entregas a tiempo y penalidades en las plantas de WoodCorp<br>
  <em>Universidad Nacional Agraria La Molina · Facultad de Economía y Planificación · DAEI</em>
</p>

---

## Tabla de contenidos

1. [Contexto y problema](#1-contexto-y-problema)
2. [Objetivos](#2-objetivos)
3. [Indicadores clave (KPI)](#3-indicadores-clave-kpi)
4. [Hallazgos preliminares](#4-hallazgos-preliminares)
5. [Preguntas de investigación](#5-preguntas-de-investigación)
6. [Hoja de ruta](#6-hoja-de-ruta)
7. [Dashboard](#7-dashboard)
8. [Estructura del repositorio](#8-estructura-del-repositorio)
9. [Fuentes de datos](#9-fuentes-de-datos)
10. [Equipo](#10-equipo)

---

## 1. Contexto y problema

**WoodCorp** opera varias plantas de producción y despacho (Essen, Aachen, Bonn, Crefeld, Duisburg y Wuppertal). La empresa enfrenta **altos costos por penalidades** asociadas a entregas que no cumplen los plazos establecidos.

> **Problema central:** solo el **64 %** de las entregas llega a tiempo, frente a una meta del **80 %**, lo que ha generado **€ 11.8 millones** en penalidades.

El análisis parte de los datos extraídos de un dashboard de **Celonis** y busca identificar dónde se concentra el problema y qué se puede hacer para corregirlo.

## 2. Objetivos

**Objetivo general**

Reducir el costo de penalidades de WoodCorp identificando las causas de los incumplimientos de entrega y proponiendo acciones de mejora.

**Objetivos específicos**

- Medir el desempeño actual de entregas a tiempo, global y por planta.
- Cuantificar el costo de las penalidades y su concentración por planta y tipo de almacén.
- Comparar el desempeño de los almacenes automatizados y no automatizados.
- Identificar las plantas y los factores que más contribuyen al incumplimiento.
- Proponer recomendaciones priorizadas por impacto económico.

## 3. Indicadores clave (KPI)

| Indicador | Definición | Valor actual | Meta | Brecha |
|---|---|---|---|---|
| **Tasa de entregas a tiempo** | % de entregas realizadas dentro del plazo | **64 %** | 80 % | **−16 pp** |
| **Costo total de penalidades** | Penalidades generadas por entregas tardías | **€ 11 824 768.50** | — | — |
| **Volumen total despachado** | Kilogramos despachados | **47 740 004 kg** | — | — |
| **Penalidad por kg despachado** | Costo de penalidades ÷ volumen | **≈ € 0.25 / kg** | — | — |
| **Concentración de penalidades** | % de penalidades en Essen + Aachen | **92.7 %** | — | — |

## 4. Hallazgos preliminares

### Desempeño por planta

| Planta | Volumen (kg) | Entregas a tiempo | Penalidades (€) | % de penalidades |
|---|---:|---:|---:|---:|
| Essen | 30 682 060 | 66 % | 7 591 272.00 | 64.2 % |
| Aachen | 13 543 511 | 61 % | 3 374 145.00 | 28.5 % |
| Bonn | 2 634 529 | 69 % | 632 161.50 | 5.3 % |
| Crefeld | 496 785 | 70 % | 162 244.50 | 1.4 % |
| Duisburg | 247 324 | 69 % | 62 973.00 | 0.5 % |
| Wuppertal | 135 795 | 88 % | 1 972.50 | 0.02 % |

### Almacenes automatizados vs. no automatizados

| Tipo de almacén | Volumen (kg) | Entregas a tiempo | Penalidades (€) |
|---|---:|---:|---:|
| Automated | 102 681 | 79.59 % | 14 001.75 |
| Non-automated | 47 637 323 | 64.42 % | 11 810 766.75 |

### Lectura inicial

- **El problema está concentrado:** Essen y Aachen explican el 92.7 % de las penalidades y manejan un volumen equivalente.
- **Ninguna planta grande cumple la meta:** solo Wuppertal supera el 80 %, con un volumen muy reducido.
- **Cuidado con la automatización:** los almacenes automatizados cumplen mejor, pero mueven apenas ~0.2 % del volumen. Con una muestra tan pequeña, **no se puede atribuir la mejora a la tecnología** sin un análisis más profundo.

## 5. Preguntas de investigación

1. ¿Qué nivel de conformidad tienen las diferentes fábricas respecto a plazos y volumen?
2. ¿Cuál es la distribución de almacenes automatizados frente a no automatizados?
3. ¿Qué recomiendas cambiar?

La aplicación en Streamlit desplegará el dashboard del proyecto, esta tiene cuatro pestañas:

1. **Presentación del caso y KPI:** indicadores generales y medidor frente a la meta.
2. **Conformidad y entregas a tiempo:** volumen, cumplimiento por planta y evolución mensual de penalidades.
3. **Distribución de almacenes:** automatizados vs. no automatizados.
4. **Conclusiones y recomendaciones.**

**Cómo ejecutarlo**

```bash
pip install -r requirements.txt
streamlit run dashboard_woodcorp.py
```

Se abrirá en `http://localhost:8501`.

> Los logos (`escudo unalm.jpg`, `escudo facultad.png`, `daeilogo.jpg`) deben estar en la misma carpeta que `app_woodcorp.py`.```

## 6. Fuentes de datos

- Dashboard de **Celonis** del caso WoodCorp (volúmenes, entregas a tiempo y penalidades por planta y tipo de almacén).
- Los valores mensuales mostrados en el gráfico de penalidades son **aproximados** (leídos del gráfico) mientras no se cargue `penalidades_mensuales.csv`.

## 7. Equipo

| Integrante |
|---|
| Ricardo Gabriel, Cardenas Panduro |
| Edson Gabriel, Chiara Vargas |
| Fabrizio, Rocha Hidalgo|
| Adrian Fabrizio, Zuazo Farje |
| Andree del Piero, De la Torre Cardenas |
**Curso:** Ingenieria de procesos · **Docente:** Valencia Chacón, Raphael Félix · **Ciclo:** _2026-II
