<div align="center">
  <img src="escudo%20unalm.jpg" alt="UNALM" height="85">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="escudo%20facultad.png" alt="Facultad de Economía y Planificación" height="85">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="daeilogo.jpg" alt="DAEI" height="85">

  <br><br>

  # 🏭 Caso WoodCorp – Factory View
  ### Análisis de entregas a tiempo y penalidades en las plantas de producción
  *Universidad Nacional Agraria La Molina · Facultad de Economía y Planificación · DAEI*

  <br>
  ![Celonis](https://img.shields.io/badge/Celonis-Process_Mining-blue?style=flat-square)
</div>

<hr>

## 📖 1. Contexto y Problema

**WoodCorp** opera diversas plantas de producción y despacho (Essen, Aachen, Bonn, Crefeld, Duisburg y Wuppertal). Actualmente, la empresa enfrenta **altos costos por penalidades** asociadas a entregas que no cumplen los plazos pactados con sus clientes.

> ⚠️ **Problema Central:** Solo el **64 %** de las entregas llega a tiempo (frente a una meta corporativa del **80 %**), lo que ha generado un impacto financiero acumulado de **€ 11.8 millones** en multas.

El presente análisis parte de los datos extraídos mediante minería de procesos desde un dashboard de **Celonis**, con el propósito de identificar dónde se concentra el cuello de botella y proponer acciones de mitigación.

## 🎯 2. Objetivos

**Objetivo General**  
Reducir el costo de penalidades de WoodCorp identificando las causas raíz de los incumplimientos de entrega y proponiendo acciones de mejora basadas en datos.

**Objetivos Específicos**  
- 📏 **Medir** el desempeño actual de entregas a tiempo, a nivel global y por planta.
- 💶 **Cuantificar** el costo de las penalidades y su concentración según fábrica y tipo de almacén.
- ⚖️ **Comparar** el rendimiento operativo entre los almacenes automatizados y no automatizados.
- 🔍 **Identificar** las plantas y factores críticos que más contribuyen al déficit de puntualidad.
- 💡 **Proponer** recomendaciones estratégicas priorizadas por su impacto económico.

## 📊 3. Indicadores Clave (KPI)

| Indicador | Definición | Valor actual | Meta | Brecha |
| :--- | :--- | :---: | :---: | :---: |
| **Tasa de entregas a tiempo** | % de entregas dentro del plazo | **64 %** | 80 % | **🔴 −16 pp** |
| **Costo total de penalidades** | Multas por entregas tardías | **€ 11,824,768.50** | — | — |
| **Volumen total despachado** | Kilogramos despachados totales | **47,740,004 kg** | — | — |
| **Tarifa de penalidad** | Costo por cada kg entregado tarde | **€ 0.75 / kg** | — | — |
| **Volumen entregado tarde** | Penalidades ÷ tarifa de € 0.75 | **≈ 15.77 M kg** *(33 %)* | — | — |
| **Penalidad prom. por kg** | Penalidades ÷ volumen total | **≈ € 0.25 / kg** | — | — |
| **Concentración de impacto**| % de penalidades en Essen + Aachen | **92.7 %** | — | — |

> *Nota:* El 33 % de volumen tardío (medido en kg) no coincide con el 36 % que resulta del 64 % de entregas a tiempo (medido en número de casos), debido a que los pedidos con entregas tardías poseen un tamaño distinto al promedio.

## 🔎 4. Hallazgos Preliminares

### Desempeño por Planta
| Planta | Volumen (kg) | Entregas a tiempo | Penalidades (€) | % del Total |
| :--- | ---: | :---: | ---: | :---: |
| **Essen** | 30,682,060 | 66 % | 7,591,272.00 | **64.2 %** |
| **Aachen** | 13,543,511 | 61 % | 3,374,145.00 | **28.5 %** |
| **Bonn** | 2,634,529 | 69 % | 632,161.50 | 5.3 % |
| **Crefeld** | 496,785 | 70 % | 162,244.50 | 1.4 % |
| **Duisburg** | 247,324 | 69 % | 62,973.00 | 0.5 % |
| **Wuppertal**| 135,795 | **88 %** | 1,972.50 | 0.02 % |

### Almacenes Automatizados vs. No Automatizados
| Tipo de Almacén | Volumen (kg) | Entregas a tiempo | Penalidades (€) |
| :--- | ---: | :---: | ---: |
| 🤖 **Automated** | 102,681 | **79.59 %** | 14,001.75 |
| 🧑‍🏭 **Non-automated** | 47,637,323 | **64.42 %** | 11,810,766.75 |

### 💡 Lectura Inicial
- **El problema está altamente concentrado:** Essen y Aachen explican el **92.7 %** de las pérdidas financieras y manejan casi todo el volumen de la compañía.
- **Ninguna planta grande cumple la meta:** Solo la operación piloto de Wuppertal supera el 80 %, pero con un volumen marginal.
- **Cuidado con el sesgo de automatización:** Aunque los almacenes automatizados cumplen mucho mejor (79.59 %), mueven apenas el **~0.2 %** del volumen total. Al ser una muestra tan pequeña, se requiere un análisis cruzado antes de atribuir el éxito exclusivamente a la tecnología.

## 🚀 5. Aplicación y Dashboard Interactivo

El diagnóstico principal y las vistas de minería de procesos fueron estructurados en **Celonis**.  
🔗 **[Ver análisis completo en Celonis Studio](https://academic-celonis-uedvyj.eu-2.celonis.cloud/package-manager/ui/studio/ui/spaces/f1fa6bba-cccf-433c-94c8-3310db6df8d4/packages/c7d594c9-2392-47e9-9ed4-f09d5c56be63/nodes/401a632d-c8ba-4e26-9b05-78f4ac5c8157?activeTabs=0bd3d208_b291_43cf_8b11_806dd09ff84b-view:1d479cf7-4000-4172-b7fa-3c882686d542&share=dbe5941b-351c-48c9-aa5d-27d4191598a8&bookmark=false)**

Adicionalmente, se desarrolló una aplicación en **Streamlit** que despliega el dashboard interactivo del proyecto con las siguientes vistas:
1. **Presentación del caso y KPI:** Indicadores generales y medidor de brecha frente a la meta.
2. **Conformidad y entregas a tiempo:** Distribución de volumen, cumplimiento por planta y evolución mensual de penalidades.
3. **Distribución de almacenes:** Rendimiento comparativo Automatizado vs. No automatizado.
4. **Conclusiones y recomendaciones.**

