# report-G4

<div align="center">

# Universidad Peruana de Ciencias Aplicadas

### Facultad de Ingeniería
### Carrera: Ingeniería de Software

**9.º ciclo**

**Nombre del curso:** Arquitecturas de Software Emergentes
**Sección:** 9075
**Código del curso:** : 1ASI0728 
**Periodo:** 202620  

**Nombre del profesor:** Wilder Aurelio Vega Calero

<br>

# *Informe de Trabajo Final*

<br>

**Nombre del Startup:** FreshEat  
**Nombre del Producto:** FreshSense

<br>

### Relación de Integrantes

| Apellidos y Nombres | Código |
|:-------------------:|:------:|
| Tuesta Marin, Romina Alejandra | U202211706 |
| Mostajo Orosco, Maria Fernanda | U202312874 |


<br>

**Septiembre 2026**

</div>

<div style="page-break-after: always;"></div>

# Registro de Versiones del Informe

| Versión | Fecha | Autor | Descripción de modificación |
|:------:|:-----:|:-----|:----------------------------|
| 1.0 | 08/09/2026 | Romina Tuesta Marin | Cargó archivos y actualizó la descripción de la Startup |

<div style="page-break-after: always;"></div>

# Project Report Collaboration Insights

**AV1:**

![Project Report Collaboration Insights](assets/.png)

<div style="page-break-after: always;"></div>

# Tabla de contenidos

- [Student Outcome](#student-outcome)

- [Capítulo I: Introducción](#capítulo-i-introducción)
  - [1.1. Startup Profile](#11-startup-profile)
    - [1.1.1. Descripción de la Startup](#111-descripción-de-la-startup)
    - [1.1.2. Perfiles de integrantes del equipo](#112-perfiles-de-integrantes-del-equipo)
  - [1.2. Solution Profile](#12-solution-profile)
    - [1.2.1. Antecedentes y problemática](#121-antecedentes-y-problemática)
    - [1.2.2. Lean UX Process](#122-lean-ux-process)
      - [1.2.2.1. Lean UX Problem Statements](#1221-lean-ux-problem-statements)
      - [1.2.2.2. Lean UX Assumptions](#1222-lean-ux-assumptions)
      - [1.2.2.3. Lean UX Hypothesis Statements](#1223-lean-ux-hypothesis-statements)
      - [1.2.2.4. Lean UX Canvas](#1224-lean-ux-canvas)
  - [1.3. Segmentos objetivo](#13-segmentos-objetivo)

- [Capítulo II: Requirements Elicitation & Analysis](#capítulo-ii-requirements-elicitation--analysis)
  - [2.1. Competidores](#21-competidores)
    - [2.1.1. Análisis competitivo](#211-análisis-competitivo)
    - [2.1.2. Estrategias y tácticas frente a competidores](#212-estrategias-y-tácticas-frente-a-competidores)
  - [2.2. Entrevistas](#22-entrevistas)
    - [2.2.1. Diseño de entrevistas](#221-diseño-de-entrevistas)
    - [2.2.2. Registro de entrevistas](#222-registro-de-entrevistas)
    - [2.2.3. Análisis de entrevistas](#223-análisis-de-entrevistas)
  - [2.3. Needfinding](#23-needfinding)
    - [2.3.1. User Personas](#231-user-personas)
    - [2.3.2. User Task Matrix](#232-user-task-matrix)
    - [2.3.3. Empathy Mapping](#233-empathy-mapping)
    - [2.3.4. As-is Scenario Mapping](#234-as-is-scenario-mapping)
  - [2.4. Ubiquitous Language](#24-ubiquitous-language)

- [Capítulo III: Requirements Specification](#capítulo-iii-requirements-specification)
  - [3.1. To-Be Scenario Mapping](#31-to-be-scenario-mapping)
  - [3.2. User Stories](#32-user-stories)
  - [3.3. Impact Mapping](#33-impact-mapping)
  - [3.4. Product Backlog](#34-product-backlog)

- [Capítulo IV: Strategic-Level Software Design](#capítulo-iv-strategic-level-software-design)
  - [4.1. Strategic-Level Attribute-Driven Design](#41-strategic-level-attribute-driven-design)
    - [4.1.1. Design Purpose](#411-design-purpose)
    - [4.1.2. Attribute-Driven Design Inputs](#412-attribute-driven-design-inputs)
      - [4.1.2.1. Primary Functionality (Primary User Stories)](#4121-primary-functionality-primary-user-stories)
      - [4.1.2.2. Quality Attribute Scenarios](#4122-quality-attribute-scenarios)
      - [4.1.2.3. Constraints](#4123-constraints)
    - [4.1.3. Architectural Drivers Backlog](#413-architectural-drivers-backlog)
    - [4.1.4. Architectural Design Decisions](#414-architectural-design-decisions)
    - [4.1.5. Quality Attribute Scenario Refinements](#415-quality-attribute-scenario-refinements)
  - [4.2. Strategic-Level Domain-Driven Design](#42-strategic-level-domain-driven-design)
    - [4.2.1. EventStorming](#421-eventstorming)
    - [4.2.2. Candidate Context Discovery](#422-candidate-context-discovery)
    - [4.2.3. Domain Message Flows Modeling](#423-domain-message-flows-modeling)
    - [4.2.4. Bounded Context Canvases](#424-bounded-context-canvases)
    - [4.2.5. Context Mapping](#425-context-mapping)
  - [4.3. Software Architecture](#43-software-architecture)
    - [4.3.1. Software Architecture System Landscape Diagram](#431-software-architecture-system-landscape-diagram)
    - [4.3.2. Software Architecture Context Level Diagrams](#432-software-architecture-context-level-diagrams)
    - [4.3.3. Software Architecture Container Level Diagrams](#433-software-architecture-container-level-diagrams)
    - [4.3.4. Software Architecture Deployment Diagrams](#434-software-architecture-deployment-diagrams)

- [Capítulo V: Tactical-Level Software Design](#capítulo-v-tactical-level-software-design)
  - [5.X. Bounded Context: &lt;Bounded Context Name&gt;](#5x-bounded-context-bounded-context-name)
    - [5.X.1. Domain Layer](#5x1-domain-layer)
    - [5.X.2. Interface Layer](#5x2-interface-layer)
    - [5.X.3. Application Layer](#5x3-application-layer)
    - [5.X.4. Infrastructure Layer](#5x4-infrastructure-layer)
    - [5.X.6. Bounded Context Software Architecture Component Level Diagrams](#5x6-bounded-context-software-architecture-component-level-diagrams)
    - [5.X.7. Bounded Context Software Architecture Code Level Diagrams](#5x7-bounded-context-software-architecture-code-level-diagrams)
      - [5.X.7.1. Bounded Context Domain Layer Class Diagrams](#5x71-bounded-context-domain-layer-class-diagrams)
      - [5.X.7.2. Bounded Context Database Design Diagram](#5x72-bounded-context-database-design-diagram)

- [Capítulo VI: Solution UX Design](#capítulo-vi-solution-ux-design)
  - [6.1. Style Guidelines](#61-style-guidelines)
    - [6.1.1. General Style Guidelines](#611-general-style-guidelines)
    - [6.1.2. Web, Mobile & Devices Style Guidelines](#612-web-mobile--devices-style-guidelines)
  - [6.2. Information Architecture](#62-information-architecture)
    - [6.2.2. Labeling Systems](#622-labeling-systems)
    - [6.2.3. Searching Systems](#623-searching-systems)
    - [6.2.4. SEO Tags and Meta Tags](#624-seo-tags-and-meta-tags)
    - [6.2.5. Navigation Systems](#625-navigation-systems)
  - [6.3. Landing Page UI Design](#63-landing-page-ui-design)
    - [6.3.1. Landing Page Wireframe](#631-landing-page-wireframe)
    - [6.3.2. Landing Page Mock-up](#632-landing-page-mock-up)
  - [6.4. Applications UX/UI Design](#64-applications-uxui-design)
    - [6.4.1. Applications Wireframes](#641-applications-wireframes)
    - [6.4.2. Applications Wireflow Diagrams](#642-applications-wireflow-diagrams)
    - [6.4.3. Applications Mock-ups](#643-applications-mock-ups)
    - [6.4.4. Applications User Flow Diagrams](#644-applications-user-flow-diagrams)
  - [6.5. Applications Prototyping](#65-applications-prototyping)

- [Capítulo VII: Product Implementation, Validation & Deployment](#capítulo-vii-product-implementation-validation--deployment)
  - [7.1. Software Configuration Management](#71-software-configuration-management)
    - [7.1.1. Software Development Environment Configuration](#711-software-development-environment-configuration)
    - [7.1.2. Source Code Management](#712-source-code-management)
    - [7.1.3. Source Code Style Guide & Conventions](#713-source-code-style-guide--conventions)
    - [7.1.4. Software Deployment Configuration](#714-software-deployment-configuration)
  - [7.2. Solution Implementation](#72-solution-implementation)
    - [7.2.X. Sprint n](#72x-sprint-n)
      - [7.2.X.1. Sprint Planning n](#72x1-sprint-planning-n)
      - [7.2.X.2. Sprint Backlog n](#72x2-sprint-backlog-n)
      - [7.2.X.3. Development Evidence for Sprint Review](#72x3-development-evidence-for-sprint-review)
      - [7.2.X.4. Testing Suite Evidence for Sprint Review](#72x4-testing-suite-evidence-for-sprint-review)
      - [7.2.X.5. Execution Evidence for Sprint Review](#72x5-execution-evidence-for-sprint-review)
      - [7.2.X.6. Services Documentation Evidence for Sprint Review](#72x6-services-documentation-evidence-for-sprint-review)
      - [7.2.X.7. Software Deployment Evidence for Sprint Review](#72x7-software-deployment-evidence-for-sprint-review)
      - [7.2.X.8. Team Collaboration Insights during Sprint](#72x8-team-collaboration-insights-during-sprint)
  - [7.3. Validation Interviews](#73-validation-interviews)
    - [7.3.1. Diseño de Entrevistas](#731-diseño-de-entrevistas)
    - [7.3.2. Registro de Entrevistas](#732-registro-de-entrevistas)
    - [7.3.3. Evaluaciones según heurísticas](#733-evaluaciones-según-heurísticas)
  - [7.4. Video About-the-Product](#74-video-about-the-product)

- [Conclusiones](#conclusiones)
- [Conclusiones y recomendaciones](#conclusiones-y-recomendaciones)
- [Video About-the-Team](#video-about-the-team)
- [Bibliografía](#bibliografía)
- [Anexos](#anexos)

<div style="page-break-after: always;"></div>

# Student Outcome

El curso contribuye al cumplimiento del Student Outcome ABET.

**ABET – EAC - Student Outcome 3**

Criterio: Capacidad de comunicarse efectivamente con un rango de audiencias.

| Criterio específico | Acciones realizadas | Conclusiones |
|:--------------------|:--------------------|:-------------|
| Comunica oralmente sus ideas y/o resultados con objetividad a público de diferentes especialidades y niveles jerarquicos, en el marco del desarrollo de un proyecto en ingeniería. | | |
| Comunica en forma escrita ideas y/o resultados con objetividad a público de diferentes especialidades y niveles jerarquicos, en el marco del desarrollo de un proyecto en ingeniería | | |

<div style="page-break-after: always;"></div>

# Capítulo I: Introducción

## 1.1. Startup Profile

### 1.1.1. Descripción de la Startup

### 1.1.2. Perfiles de integrantes del equipo

## 1.2. Solution Profile

### 1.2.1. Antecedentes y problemática

### 1.2.2. Lean UX Process

#### 1.2.2.1. Lean UX Problem Statements

#### 1.2.2.2. Lean UX Assumptions

#### 1.2.2.3. Lean UX Hypothesis Statements

#### 1.2.2.4. Lean UX Canvas

## 1.3. Segmentos objetivo

<div style="page-break-after: always;"></div>

# Capítulo II: Requirements Elicitation & Analysis

## 2.1. Competidores

### 2.1.1. Análisis competitivo

### 2.1.2. Estrategias y tácticas frente a competidores

## 2.2. Entrevistas

### 2.2.1. Diseño de entrevistas

### 2.2.2. Registro de entrevistas

### 2.2.3. Análisis de entrevistas

## 2.3. Needfinding

### 2.3.1. User Personas

### 2.3.2. User Task Matrix

### 2.3.3. Empathy Mapping

### 2.3.4. As-is Scenario Mapping

## 2.4. Ubiquitous Language

<div style="page-break-after: always;"></div>

# Capítulo III: Requirements Specification

## 3.1. To-Be Scenario Mapping

<figure id="fig-cmap" style="margin:1.5em 0;text-align:center">
<img src="Assets/To Be Scenario Mapping.png" alt="Context Map consolidado — ocho bounded contexts de FreshSense." style="max-width:100%;height:auto"/>
<figcaption style="font-size:0.9em;color:#555;margin-top:0.4em"><em>To-Be Scenario Mapping.</em></figcaption>
</figure>

## 3.2. User Stories

| User Story ID | Título | Descripción | Criterios de Aceptación | Relacionado con (Epic ID) |
|---|---|---|---|---|
| **US01** | Visualización de la propuesta de valor | Como visitante representante de un restaurante pequeño o negocio de alimentos fríos, deseo conocer la propuesta de valor de FreshSense para evaluar cómo puede ayudar a reducir las pérdidas ocasionadas por el deterioro de productos perecibles. | **Escenario 1: Consulta de propuesta de valor**<br>**Dado que** un visitante accede al sitio informativo de FreshSense<br>**Cuando** consulta la información principal de la solución<br>**Entonces** el sistema presenta los beneficios relacionados con monitoreo, conservación de productos y reducción de mermas.<br><br>**Escenario 2: Identificación del problema atendido**<br>**Dado que** el visitante revisa la información de FreshSense<br>**Cuando** consulta los beneficios de la solución<br>**Entonces** puede identificar que FreshSense busca reducir las pérdidas ocasionadas por condiciones inadecuadas de conservación. | **EP01** |
| **US02** | Información según segmento objetivo | Como visitante representante de un restaurante pequeño o negocio de alimentos fríos, deseo consultar información relacionada con mi tipo de negocio para comprender cómo FreshSense puede atender mis necesidades particulares. | **Escenario 1: Información para restaurantes**<br>**Dado que** el visitante pertenece al segmento de restaurantes pequeños<br>**Cuando** consulta la información correspondiente a su segmento<br>**Entonces** el sistema presenta beneficios relacionados con conservación de insumos, inventario, alertas y reducción de mermas.<br><br>**Escenario 2: Información para negocios de alimentos fríos**<br>**Dado que** el visitante pertenece al segmento de negocios de alimentos fríos<br>**Cuando** consulta la información correspondiente a su segmento<br>**Entonces** el sistema presenta beneficios relacionados con monitoreo de condiciones, productos almacenados, lotes y alertas. | **EP01** |
| **US03** | Solicitud de contacto y demostración | Como visitante interesado en FreshSense, deseo enviar una solicitud de contacto para coordinar una demostración y obtener mayor información sobre la solución. | **Escenario 1: Solicitud válida**<br>**Dado que** el visitante proporciona los datos obligatorios de contacto<br>**Cuando** envía la solicitud<br>**Entonces** el sistema registra correctamente la solicitud de contacto.<br><br>**Escenario 2: Información incompleta**<br>**Dado que** el visitante no proporciona todos los datos obligatorios<br>**Cuando** intenta enviar la solicitud<br>**Entonces** el sistema no registra la solicitud e informa que existen datos pendientes. | **EP01** |
| **US04** | Solicitud de demostración comercial | Como visitante interesado en adoptar FreshSense, deseo iniciar una solicitud de demostración para evaluar la solución antes de incorporarla a mi negocio. | **Escenario 1: Inicio de solicitud**<br>**Dado que** el visitante ha revisado la propuesta de FreshSense<br>**Cuando** decide solicitar una demostración<br>**Entonces** el sistema permite iniciar el proceso de contacto comercial.<br><br>**Escenario 2: Asociación con segmento**<br>**Dado que** el visitante identifica el tipo de negocio al que pertenece<br>**Cuando** inicia la solicitud<br>**Entonces** el sistema registra el segmento asociado con la solicitud comercial. | **EP01** |
| **US05** | Acceso desde diferentes dispositivos | Como propietario, gerente o encargado de un negocio, deseo acceder a FreshSense desde computadoras, tablets y dispositivos móviles para consultar la información de mis productos durante la operación diaria. | **Escenario 1: Acceso compatible**<br>**Dado que** el usuario accede desde un dispositivo compatible<br>**Cuando** utiliza las funcionalidades disponibles<br>**Entonces** puede consultar y gestionar la información de su negocio sin pérdida de contenido.<br><br>**Escenario 2: Consistencia de información**<br>**Dado que** el usuario utiliza FreshSense desde diferentes dispositivos<br>**Cuando** consulta la información de su negocio<br>**Entonces** el sistema presenta los mismos datos actualizados independientemente del dispositivo utilizado. | **EP05** |
| **US06** | Monitoreo IoT de condiciones de conservación | Como encargado de un restaurante o negocio de alimentos fríos, deseo monitorear continuamente la temperatura y humedad de las zonas de conservación para detectar condiciones que puedan ocasionar el deterioro de los productos. | **Escenario 1: Registro de mediciones**<br>**Dado que** un dispositivo FreshSense se encuentra asociado con una zona de conservación<br>**Cuando** registra una medición válida de temperatura y humedad<br>**Entonces** el sistema almacena la medición asociándola con el dispositivo y la zona correspondiente.<br><br>**Escenario 2: Actualización de condiciones**<br>**Dado que** existen nuevas mediciones válidas<br>**Cuando** el sistema procesa las mediciones<br>**Entonces** actualiza el estado de las condiciones de conservación de la zona monitoreada. | **EP02** |
| **US07** | Estado de conservación de productos | Como propietario, gerente o encargado de un negocio, deseo consultar el estado de conservación de los productos para identificar aquellos que presentan mayor riesgo de deterioro. | **Escenario 1: Determinación del estado**<br>**Dado que** existen productos asociados con zonas monitoreadas<br>**Cuando** el sistema analiza sus condiciones de conservación y vencimiento<br>**Entonces** determina el nivel de riesgo correspondiente a cada producto.<br><br>**Escenario 2: Consulta de producto**<br>**Dado que** existe información registrada sobre un producto<br>**Cuando** el usuario consulta su estado<br>**Entonces** el sistema proporciona su identificación, lote, vencimiento, ubicación y condiciones registradas. | **EP02** |
| **US08** | Alertas preventivas de conservación | Como encargado de un restaurante o negocio de alimentos fríos, deseo recibir alertas cuando las condiciones de conservación se encuentren fuera de los rangos establecidos para actuar antes de que los productos resulten afectados. | **Escenario 1: Condición fuera de rango**<br>**Dado que** una medición supera los límites establecidos para una zona de conservación<br>**Cuando** el sistema procesa la medición<br>**Entonces** genera una alerta asociada con la zona afectada.<br><br>**Escenario 2: Condiciones normales**<br>**Dado que** las mediciones permanecen dentro de los rangos establecidos<br>**Cuando** el sistema procesa las mediciones<br>**Entonces** no genera una alerta por desviación de las condiciones. | **EP03** |
| **US09** | Configuración de alertas | Como administrador del negocio, deseo configurar las preferencias y responsables de las alertas para asegurar que las incidencias sean comunicadas a las personas correspondientes. | **Escenario 1: Configuración válida**<br>**Dado que** el administrador posee permisos para gestionar alertas<br>**Cuando** establece responsables y niveles de prioridad<br>**Entonces** el sistema almacena la configuración definida.<br><br>**Escenario 2: Aplicación de configuración**<br>**Dado que** existe una configuración activa de alertas<br>**Cuando** se genera una incidencia<br>**Entonces** el sistema utiliza dicha configuración para determinar a los responsables que deben ser notificados. | **EP03** |
| **US10** | Registro de productos e insumos | Como encargado del inventario, deseo registrar productos o insumos de manera rápida para mantener actualizado el inventario sin afectar las actividades diarias del negocio. | **Escenario 1: Registro válido**<br>**Dado que** el encargado proporciona la información obligatoria de un producto<br>**Cuando** registra el producto<br>**Entonces** el sistema almacena su identificación, cantidad, categoría, lote y vencimiento cuando corresponda.<br><br>**Escenario 2: Información incompleta**<br>**Dado que** falta información obligatoria del producto<br>**Cuando** se intenta completar el registro<br>**Entonces** el sistema no registra información incompleta. | **EP04** |
| **US11** | Actualización del inventario | Como encargado del inventario, deseo actualizar las cantidades disponibles de los productos para mantener información confiable sobre las existencias del negocio. | **Escenario 1: Actualización válida**<br>**Dado que** un producto se encuentra registrado<br>**Cuando** el encargado modifica su cantidad utilizando un valor válido<br>**Entonces** el sistema actualiza las existencias y registra la modificación.<br><br>**Escenario 2: Cantidad inválida**<br>**Dado que** el encargado proporciona una cantidad no permitida<br>**Cuando** intenta guardar la modificación<br>**Entonces** el sistema rechaza la actualización y mantiene la cantidad anterior. | **EP04** |
| **US12** | Reporte de mermas y pérdidas | Como propietario o gerente de un negocio, deseo consultar reportes periódicos de productos descartados y pérdidas económicas para identificar oportunidades de reducción de mermas. | **Escenario 1: Generación de reporte**<br>**Dado que** existen productos registrados como merma durante un periodo<br>**Cuando** el usuario solicita el reporte correspondiente<br>**Entonces** el sistema consolida las cantidades descartadas y su valor económico registrado.<br><br>**Escenario 2: Periodo sin mermas**<br>**Dado que** no existen productos registrados como merma durante el periodo seleccionado<br>**Cuando** el usuario solicita el reporte<br>**Entonces** el sistema informa que no existen mermas registradas para dicho periodo. | **EP06** |
| **US13** | Priorización de productos próximos a deteriorarse | Como propietario o gerente de un restaurante pequeño, deseo identificar los insumos próximos a deteriorarse o vencer para priorizar su aprovechamiento y reducir el desperdicio. | **Escenario 1: Identificación de producto en riesgo**<br>**Dado que** un insumo se encuentra próximo a vencer o presenta riesgo de deterioro<br>**Cuando** el sistema analiza el inventario<br>**Entonces** identifica el producto como de atención prioritaria.<br><br>**Escenario 2: Priorización de múltiples productos**<br>**Dado que** existen varios productos con diferentes niveles de riesgo<br>**Cuando** el usuario consulta los productos prioritarios<br>**Entonces** el sistema los ordena según su riesgo de deterioro o proximidad al vencimiento. | **EP04** |
| **US14** | Filtrado de productos y lotes | Como encargado del inventario, deseo filtrar los productos por zona de conservación, lote, categoría y fecha de vencimiento para localizar rápidamente aquellos que requieren atención. | **Escenario 1: Filtrado válido**<br>**Dado que** existen productos registrados con diferentes características<br>**Cuando** el usuario aplica uno o más criterios de filtrado<br>**Entonces** el sistema devuelve únicamente los productos que cumplen los criterios seleccionados.<br><br>**Escenario 2: Sin resultados**<br>**Dado que** ningún producto cumple los criterios establecidos<br>**Cuando** el usuario ejecuta el filtrado<br>**Entonces** el sistema informa que no existen resultados coincidentes. | **EP04** |
| **US15** | Inducción de nuevos colaboradores | Como administrador del negocio, deseo que los nuevos colaboradores dispongan de una guía inicial de uso para facilitar la adopción de FreshSense. | **Escenario 1: Primer acceso**<br>**Dado que** un colaborador utiliza FreshSense por primera vez<br>**Cuando** inicia su proceso de incorporación<br>**Entonces** el sistema proporciona información sobre las funcionalidades necesarias para sus actividades.<br><br>**Escenario 2: Inducción completada**<br>**Dado que** el colaborador ya completó la inducción<br>**Cuando** vuelve a utilizar FreshSense<br>**Entonces** puede continuar con sus actividades sin repetir obligatoriamente el proceso inicial. | **EP05** |
| **US16** | Experiencia accesible para entornos operativos | Como colaborador de un restaurante o negocio de alimentos fríos, deseo utilizar una experiencia clara y accesible para realizar mis actividades de manera sencilla durante la operación diaria. | **Escenario 1: Comprensión de información**<br>**Dado que** el colaborador consulta información del sistema<br>**Cuando** realiza una actividad relacionada con sus responsabilidades<br>**Entonces** puede identificar claramente la información necesaria para completarla.<br><br>**Escenario 2: Operaciones accesibles**<br>**Dado que** el colaborador dispone de los permisos requeridos<br>**Cuando** ejecuta una operación habitual<br>**Entonces** puede completarla sin requerir conocimientos técnicos especializados. | **EP05** |
| **US17** | Análisis de rotación de inventario | Como propietario o gerente de un negocio, deseo analizar la rotación de mis productos para mejorar las decisiones relacionadas con compra, reposición y utilización del inventario. | **Escenario 1: Análisis de periodo**<br>**Dado que** existe información histórica de movimientos de inventario<br>**Cuando** el usuario selecciona un periodo de análisis<br>**Entonces** el sistema calcula indicadores relacionados con entradas, salidas, rotación y mermas.<br><br>**Escenario 2: Información insuficiente**<br>**Dado que** no existe suficiente información para calcular un indicador<br>**Cuando** el usuario solicita el análisis<br>**Entonces** el sistema identifica los indicadores que no pueden ser calculados. | **EP06** |
| **US18** | Impacto económico de las pérdidas evitadas | Como propietario o gerente de un negocio, deseo consultar una estimación del valor económico asociado con los productos que evitaron convertirse en merma para evaluar los beneficios obtenidos mediante una mejor gestión del inventario. | **Escenario 1: Estimación disponible**<br>**Dado que** existen productos registrados con información de costo y estado<br>**Cuando** el sistema identifica productos utilizados o comercializados antes de convertirse en merma<br>**Entonces** calcula una estimación del valor económico correspondiente.<br><br>**Escenario 2: Datos insuficientes**<br>**Dado que** un producto no cuenta con información suficiente de costo<br>**Cuando** se realiza la estimación<br>**Entonces** el sistema excluye dicho producto del cálculo e identifica la información faltante. | **EP06** |
| **US19** | Asignación de responsables de alertas | Como administrador del negocio, deseo asignar responsables para las alertas críticas para asegurar que las incidencias sean atendidas por las personas correspondientes. | **Escenario 1: Asignación válida**<br>**Dado que** existen colaboradores registrados<br>**Cuando** el administrador asigna un responsable a un tipo de alerta<br>**Entonces** el sistema guarda la asociación correspondiente.<br><br>**Escenario 2: Generación de alerta crítica**<br>**Dado que** existe un responsable asignado a una alerta<br>**Cuando** se detecta una incidencia correspondiente<br>**Entonces** el sistema dirige la notificación al responsable configurado. | **EP03** |
| **US20** | Categorización de productos y zonas | Como encargado del inventario, deseo crear categorías personalizadas para organizar los productos y zonas de conservación de acuerdo con las necesidades del negocio. | **Escenario 1: Creación de categoría**<br>**Dado que** el encargado requiere una nueva clasificación<br>**Cuando** registra una categoría válida<br>**Entonces** el sistema almacena la categoría para su posterior utilización.<br><br>**Escenario 2: Asociación con categoría**<br>**Dado que** existe una categoría registrada<br>**Cuando** el encargado asocia un producto o zona con dicha categoría<br>**Entonces** el sistema conserva la relación correspondiente. | **EP04** |
| **US21** | Historial de inventario y mermas | Como propietario, encargado o responsable administrativo, deseo consultar y exportar el historial de productos, lotes y mermas para analizar incidencias y mantener evidencia de las operaciones realizadas. | **Escenario 1: Consulta histórica**<br>**Dado que** existen movimientos registrados durante un periodo<br>**Cuando** el usuario consulta el historial<br>**Entonces** el sistema presenta los movimientos de inventario, lotes y mermas correspondientes.<br><br>**Escenario 2: Exportación del historial**<br>**Dado que** existe información histórica disponible<br>**Cuando** el usuario solicita su exportación<br>**Entonces** el sistema genera un archivo con los registros del periodo seleccionado. | **EP06** |
| **US22** | Sugerencias de reposición de inventario | Como responsable de compras o inventario, deseo recibir sugerencias de reposición basadas en el comportamiento histórico de los productos para reducir el sobrestock y las pérdidas. | **Escenario 1: Información histórica suficiente**<br>**Dado que** existe suficiente información sobre los movimientos de un producto<br>**Cuando** el sistema analiza sus patrones históricos<br>**Entonces** genera una sugerencia de reposición basada en la información disponible.<br><br>**Escenario 2: Información histórica insuficiente**<br>**Dado que** no existen suficientes registros de un producto<br>**Cuando** se solicita una sugerencia<br>**Entonces** el sistema informa que todavía no dispone de información suficiente para generarla. | **EP06** |
| **US23** | Vinculación de dispositivos FreshSense | Como encargado de un negocio, deseo vincular cada dispositivo FreshSense con la zona de conservación correspondiente para identificar el origen de las mediciones recibidas. | **Escenario 1: Vinculación válida**<br>**Dado que** existe un dispositivo FreshSense disponible<br>**Cuando** el encargado lo asocia con una zona de conservación válida<br>**Entonces** el sistema registra la relación entre el dispositivo y la zona.<br><br>**Escenario 2: Dispositivo previamente vinculado**<br>**Dado que** el dispositivo ya se encuentra asociado con otra zona<br>**Cuando** se intenta realizar una nueva asociación<br>**Entonces** el sistema evita mantener asociaciones simultáneas incompatibles. | **EP02** |
| **US24** | Gestión de zonas de conservación | Como propietario o encargado de un negocio, deseo registrar y organizar las diferentes zonas de conservación para monitorear independientemente las condiciones de cada una. | **Escenario 1: Registro de zona**<br>**Dado que** existe una zona de conservación no registrada<br>**Cuando** el encargado proporciona su información requerida<br>**Entonces** el sistema registra la nueva zona.<br><br>**Escenario 2: Asociación con dispositivo**<br>**Dado que** existe una zona registrada<br>**Cuando** se vincula un dispositivo FreshSense con dicha zona<br>**Entonces** las futuras mediciones del dispositivo quedan asociadas con la zona correspondiente. | **EP02** |
| **US25** | Registro de causas de merma | Como encargado o responsable del negocio, deseo registrar la causa asociada con el descarte de un producto para analizar posteriormente los principales motivos de las mermas. | **Escenario 1: Registro de merma**<br>**Dado que** un producto es registrado como descartado<br>**Cuando** el usuario indica una causa válida de merma<br>**Entonces** el sistema almacena la causa junto con el registro del descarte.<br><br>**Escenario 2: Consulta de causas**<br>**Dado que** existen registros de merma con causas asociadas<br>**Cuando** se genera un reporte de pérdidas<br>**Entonces** el sistema puede agrupar las mermas según las causas registradas. | **EP04** |
| **US26** | Recuperación de contraseña | Como colaborador registrado, deseo recuperar el acceso a mi cuenta cuando olvide mi contraseña para continuar utilizando FreshSense de manera segura. | **Escenario 1: Solicitud válida**<br>**Dado que** existe una cuenta asociada con el correo proporcionado<br>**Cuando** el usuario solicita recuperar su contraseña<br>**Entonces** el sistema genera un mecanismo temporal de recuperación y lo envía al correo registrado.<br><br>**Escenario 2: Mecanismo inválido**<br>**Dado que** el mecanismo de recuperación ha expirado o ya fue utilizado<br>**Cuando** el usuario intenta utilizarlo nuevamente<br>**Entonces** el sistema rechaza la solicitud de cambio de contraseña. | **EP08** |
| **US27** | Administración de usuarios y roles | Como administrador del negocio, deseo gestionar los roles y permisos de los colaboradores para controlar las funcionalidades a las que puede acceder cada usuario. | **Escenario 1: Asignación de rol**<br>**Dado que** existe un colaborador registrado<br>**Cuando** el administrador le asigna un rol válido<br>**Entonces** el sistema aplica los permisos correspondientes al rol asignado.<br><br>**Escenario 2: Operación no autorizada**<br>**Dado que** el colaborador no posee el permiso requerido<br>**Cuando** intenta ejecutar una operación restringida<br>**Entonces** el sistema impide la operación. | **EP08** |
| **US28** | Gestión de colaboradores | Como propietario o gerente de un negocio, deseo incorporar colaboradores a FreshSense para que puedan realizar las actividades correspondientes a sus responsabilidades. | **Escenario 1: Incorporación de colaborador**<br>**Dado que** el propietario o gerente posee permisos administrativos<br>**Cuando** registra o invita a un nuevo colaborador<br>**Entonces** el sistema asocia al colaborador con el negocio correspondiente.<br><br>**Escenario 2: Asignación de responsabilidades**<br>**Dado que** el colaborador pertenece al negocio<br>**Cuando** se le asigna un rol<br>**Entonces** obtiene los permisos correspondientes a dicho rol. | **EP08** |
| **US29** | Consulta de facturación | Como responsable administrativo del negocio, deseo consultar los comprobantes asociados con la suscripción de FreshSense para mantener el control de los gastos relacionados con el servicio. | **Escenario 1: Comprobante disponible**<br>**Dado que** existe un pago procesado asociado con el negocio<br>**Cuando** el responsable consulta la facturación<br>**Entonces** el sistema permite obtener el comprobante correspondiente.<br><br>**Escenario 2: Periodo sin comprobantes**<br>**Dado que** no existen pagos registrados durante el periodo seleccionado<br>**Cuando** el responsable consulta la facturación<br>**Entonces** el sistema informa que no existen comprobantes disponibles para dicho periodo. | **EP07** |
| **US30** | Búsqueda de productos y lotes | Como encargado del inventario, deseo buscar productos y lotes registrados para localizar rápidamente su información y zona de almacenamiento. | **Escenario 1: Coincidencia encontrada**<br>**Dado que** existe un producto o lote registrado<br>**Cuando** el usuario realiza una búsqueda utilizando información identificable<br>**Entonces** el sistema devuelve los registros coincidentes y su información relevante.<br><br>**Escenario 2: Sin coincidencias**<br>**Dado que** ningún producto o lote coincide con el criterio proporcionado<br>**Cuando** el usuario realiza la búsqueda<br>**Entonces** el sistema informa que no se encontraron resultados. | **EP04** |
| **TS41** | API de ingesta de telemetría IoT | Como Developer, deseo disponer de un servicio de ingesta para recibir de manera segura las mediciones de temperatura y humedad enviadas por los dispositivos FreshSense para almacenarlas y procesarlas dentro de la plataforma. | **Escenario 1: Recepción de telemetría válida**<br>**Dado que** un dispositivo FreshSense autenticado envía una solicitud con una medición válida de temperatura, humedad, identificador del dispositivo y fecha de registro<br>**Cuando** el servicio valida y procesa la solicitud<br>**Entonces** almacena la medición asociada con el dispositivo correspondiente y devuelve una respuesta exitosa.<br><br>**Escenario 2: Dispositivo no autorizado**<br>**Dado que** un dispositivo envía una solicitud sin credenciales válidas<br>**Cuando** el servicio intenta validar la solicitud<br>**Entonces** rechaza la operación y no almacena las mediciones recibidas.<br><br>**Escenario 3: Información inválida**<br>**Dado que** un dispositivo autenticado envía una medición incompleta o inválida<br>**Cuando** el servicio valida los datos recibidos<br>**Entonces** rechaza la solicitud e informa que los datos proporcionados no son válidos. | **EP02** |
| **TS42** | Servicio de procesamiento de notificaciones | Como Developer, deseo disponer de un servicio encargado de procesar y distribuir las alertas generadas por FreshSense para notificar oportunamente a los responsables configurados. | **Escenario 1: Procesamiento de alerta válida**<br>**Dado que** FreshSense genera una alerta asociada con una incidencia de conservación<br>**Cuando** el servicio recibe el evento correspondiente<br>**Entonces** identifica a los responsables configurados y procesa el envío de la notificación.<br><br>**Escenario 2: Ausencia de responsable**<br>**Dado que** se genera una alerta sin un responsable válido configurado<br>**Cuando** el servicio intenta procesarla<br>**Entonces** registra la incidencia para evitar que la alerta sea descartada silenciosamente.<br><br>**Escenario 3: Fallo del servicio externo**<br>**Dado que** el proveedor utilizado para enviar una notificación no se encuentra disponible<br>**Cuando** el servicio intenta completar el envío<br>**Entonces** registra el fallo y conserva la notificación pendiente para un intento posterior. | **EP03** |
| **TS43** | Servicio de autenticación y autorización basada en roles | Como Developer, deseo implementar mecanismos de autenticación y autorización basada en roles para proteger los recursos de FreshSense y limitar las operaciones de acuerdo con los permisos de cada usuario. | **Escenario 1: Usuario autorizado**<br>**Dado que** un usuario presenta credenciales válidas y posee los permisos requeridos<br>**Cuando** solicita acceder a un recurso protegido<br>**Entonces** el servicio permite realizar la operación solicitada.<br><br>**Escenario 2: Usuario autenticado sin permisos**<br>**Dado que** un usuario se encuentra autenticado pero no posee el permiso requerido<br>**Cuando** solicita realizar una operación restringida<br>**Entonces** el servicio rechaza la operación por autorización insuficiente.<br><br>**Escenario 3: Usuario no autenticado**<br>**Dado que** una solicitud no presenta credenciales válidas<br>**Cuando** intenta acceder a un recurso protegido<br>**Entonces** el servicio rechaza la solicitud sin ejecutar la operación solicitada. | **EP08** |
| **TS44** | Integración de pagos y suscripciones | Como Developer, deseo integrar un servicio de procesamiento de pagos recurrentes para actualizar automáticamente el estado de las suscripciones contratadas por los negocios. | **Escenario 1: Pago confirmado**<br>**Dado que** el proveedor de pagos confirma una transacción válida asociada con una suscripción<br>**Cuando** FreshSense recibe la confirmación del pago<br>**Entonces** actualiza la vigencia de la suscripción correspondiente y registra la transacción.<br><br>**Escenario 2: Pago rechazado**<br>**Dado que** el proveedor informa que una transacción no fue procesada correctamente<br>**Cuando** FreshSense recibe la respuesta<br>**Entonces** mantiene el estado anterior de la suscripción y registra el intento fallido.<br><br>**Escenario 3: Notificación duplicada**<br>**Dado que** el proveedor envía nuevamente una confirmación de pago previamente procesada<br>**Cuando** FreshSense recibe la notificación duplicada<br>**Entonces** evita registrar nuevamente la misma transacción o extender incorrectamente la vigencia de la suscripción. | **EP07** |
| **TS45** | Optimización de consultas frecuentes | Como Developer, deseo implementar un mecanismo de almacenamiento temporal para optimizar las consultas frecuentes de inventario y productos sin comprometer la consistencia de la información. | **Escenario 1: Información disponible en almacenamiento temporal**<br>**Dado que** existe información válida almacenada temporalmente para una consulta frecuente<br>**Cuando** se recibe una nueva solicitud equivalente<br>**Entonces** el servicio obtiene la información disponible sin realizar nuevamente el procesamiento completo de la consulta.<br><br>**Escenario 2: Información inexistente o expirada**<br>**Dado que** la información solicitada no se encuentra disponible o ha expirado<br>**Cuando** se recibe la consulta<br>**Entonces** el servicio obtiene los datos desde la fuente principal y actualiza el almacenamiento temporal.<br><br>**Escenario 3: Actualización de inventario**<br>**Dado que** un registro de inventario utilizado por una consulta almacenada temporalmente ha sido modificado<br>**Cuando** se confirma la modificación<br>**Entonces** el sistema invalida o actualiza la información temporal relacionada para evitar devolver datos desactualizados. | **EP04** |

### Epics (Épicas)

| Epic ID | Título de la Épica | Alcance y Descripción Corta |
|---|---|---|
| **EP01** | **Portal Informativo y Conversión Comercial** | Comprende las funcionalidades del sitio informativo de FreshSense orientadas a comunicar la propuesta de valor a los segmentos objetivo, presentar información específica para restaurantes pequeños y negocios de alimentos fríos, y permitir que los potenciales clientes soliciten contacto o una demostración de la solución. |
| **EP02** | **Monitoreo IoT y Gestión de Zonas de Conservación** | Comprende la captura y consulta de las mediciones de temperatura y humedad obtenidas mediante los dispositivos FreshSense, así como la asociación de dispositivos con las diferentes zonas de conservación del negocio. Permite conocer las condiciones ambientales de cada zona e identificar productos que puedan encontrarse en riesgo de deterioro. |
| **EP03** | **Alertas Preventivas y Gestión de Incidencias** | Comprende la detección de condiciones de conservación fuera de los rangos establecidos y la generación de alertas preventivas. Permite configurar prioridades, responsables y criterios de notificación para facilitar una respuesta oportuna ante situaciones que puedan afectar los productos almacenados. |
| **EP04** | **Gestión de Inventario, Productos y Lotes** | Comprende el registro, actualización, organización, búsqueda y consulta de productos, insumos y lotes. Incluye funcionalidades para identificar productos próximos a deteriorarse, clasificarlos mediante categorías, registrar causas de merma y facilitar el control de las existencias durante las actividades diarias del negocio. |
| **EP05** | **Experiencia de Usuario y Adopción de la Plataforma** | Comprende las funcionalidades orientadas a facilitar el uso de FreshSense durante las actividades operativas del negocio. Incluye acceso desde diferentes dispositivos, una experiencia clara y accesible, y mecanismos de inducción que permitan a nuevos colaboradores comprender las funcionalidades necesarias para sus responsabilidades. |
| **EP06** | **Analítica de Mermas, Rotación y Reposición** | Comprende el análisis de la información histórica generada por el inventario para apoyar la toma de decisiones. Incluye reportes de mermas y pérdidas económicas, análisis de rotación, estimaciones del impacto económico de las pérdidas evitadas, consulta y exportación de históricos y sugerencias de reposición basadas en el comportamiento registrado. |
| **EP07** | **Suscripción y Facturación** | Comprende la gestión de los aspectos asociados con el modelo de suscripción de FreshSense, incluyendo el procesamiento de los pagos del servicio, la actualización de la vigencia de la suscripción y la consulta de los comprobantes correspondientes por parte de los responsables administrativos del negocio. |
| **EP08** | **Gestión de Usuarios, Colaboradores y Control de Acceso** | Comprende las funcionalidades necesarias para administrar las cuentas asociadas con cada negocio. Incluye incorporación de colaboradores, asignación de roles y permisos, recuperación de credenciales y mecanismos de autorización para restringir las operaciones según las responsabilidades de cada usuario. |

## 3.3. Impact Mapping

<figure id="fig-cmap" style="margin:1.5em 0;text-align:center">
<img src="Assets/Impact map 1.png" alt="Context Map consolidado — ocho bounded contexts de FreshSense." style="max-width:100%;height:auto"/>
<figcaption style="font-size:0.9em;color:#555;margin-top:0.4em"><em>Impact Mapping - User Persona 1.</em></figcaption>
</figure>

<figure id="fig-cmap" style="margin:1.5em 0;text-align:center">
<img src="Assets/Impact map_2.png" alt="Context Map consolidado — ocho bounded contexts de FreshSense." style="max-width:100%;height:auto"/>
<figcaption style="font-size:0.9em;color:#555;margin-top:0.4em"><em>Impact Mapping - User Persona 2.</em></figcaption>
</figure>

## 3.4. Product Backlog

El Product Backlog de FreshSense reúne y prioriza las User Stories y Technical Stories definidas para la solución. 
Para la estimación relativa se utiliza la escala de Fibonacci de 1, 2, 3, 5 y 8 Story Points.

| # Orden | User Story Id | Título | Descripción | Story Points |
|---:|---|---|---|---:|
| **1** | **US01** | Visualización de la propuesta de valor | Como visitante representante de un restaurante pequeño o negocio de alimentos fríos, deseo conocer la propuesta de valor de FreshSense para evaluar cómo puede ayudar a reducir las pérdidas ocasionadas por el deterioro de productos perecibles. | **2** |
| **2** | **US02** | Información según segmento objetivo | Como visitante representante de un restaurante pequeño o negocio de alimentos fríos, deseo consultar información relacionada con mi tipo de negocio para comprender cómo FreshSense puede atender mis necesidades particulares. | **3** |
| **3** | **US03** | Solicitud de contacto y demostración | Como visitante interesado en FreshSense, deseo enviar una solicitud de contacto para coordinar una demostración y obtener mayor información sobre la solución. | **3** |
| **4** | **US04** | Solicitud de demostración comercial | Como visitante interesado en adoptar FreshSense, deseo iniciar una solicitud de demostración para evaluar la solución antes de incorporarla a mi negocio. | **2** |
| **5** | **US06** | Monitoreo IoT de condiciones de conservación | Como encargado de un restaurante o negocio de alimentos fríos, deseo monitorear continuamente la temperatura y humedad de las zonas de conservación para detectar condiciones que puedan ocasionar el deterioro de los productos. | **8** |
| **6** | **TS41** | API de ingesta de telemetría IoT | Como Developer, deseo disponer de un servicio de ingesta para recibir de manera segura las mediciones de temperatura y humedad enviadas por los dispositivos FreshSense para almacenarlas y procesarlas dentro de la plataforma. | **8** |
| **7** | **US23** | Vinculación de dispositivos FreshSense | Como encargado de un negocio, deseo vincular cada dispositivo FreshSense con la zona de conservación correspondiente para identificar el origen de las mediciones recibidas. | **5** |
| **8** | **US24** | Gestión de zonas de conservación | Como propietario o encargado de un negocio, deseo registrar y organizar las diferentes zonas de conservación para monitorear independientemente las condiciones de cada una. | **5** |
| **9** | **US08** | Alertas preventivas de conservación | Como encargado de un restaurante o negocio de alimentos fríos, deseo recibir alertas cuando las condiciones de conservación se encuentren fuera de los rangos establecidos para actuar antes de que los productos resulten afectados. | **5** |
| **10** | **TS42** | Servicio de procesamiento de notificaciones | Como Developer, deseo disponer de un servicio encargado de procesar y distribuir las alertas generadas por FreshSense para notificar oportunamente a los responsables configurados. | **8** |
| **11** | **US10** | Registro de productos e insumos | Como encargado del inventario, deseo registrar productos o insumos de manera rápida para mantener actualizado el inventario sin afectar las actividades diarias del negocio. | **5** |
| **12** | **US11** | Actualización del inventario | Como encargado del inventario, deseo actualizar las cantidades disponibles de los productos para mantener información confiable sobre las existencias del negocio. | **3** |
| **13** | **US07** | Estado de conservación de productos | Como propietario, gerente o encargado de un negocio, deseo consultar el estado de conservación de los productos para identificar aquellos que presentan mayor riesgo de deterioro. | **5** |
| **14** | **US13** | Priorización de productos próximos a deteriorarse | Como propietario o gerente de un restaurante pequeño, deseo identificar los insumos próximos a deteriorarse o vencer para priorizar su aprovechamiento y reducir el desperdicio. | **5** |
| **15** | **US14** | Filtrado de productos y lotes | Como encargado del inventario, deseo filtrar los productos por zona de conservación, lote, categoría y fecha de vencimiento para localizar rápidamente aquellos que requieren atención. | **3** |
| **16** | **US30** | Búsqueda de productos y lotes | Como encargado del inventario, deseo buscar productos y lotes registrados para localizar rápidamente su información y zona de almacenamiento. | **3** |
| **17** | **US20** | Categorización de productos y zonas | Como encargado del inventario, deseo crear categorías personalizadas para organizar los productos y zonas de conservación de acuerdo con las necesidades del negocio. | **3** |
| **18** | **US25** | Registro de causas de merma | Como encargado o responsable del negocio, deseo registrar la causa asociada con el descarte de un producto para analizar posteriormente los principales motivos de las mermas. | **3** |
| **19** | **US12** | Reporte de mermas y pérdidas | Como propietario o gerente de un negocio, deseo consultar reportes periódicos de productos descartados y pérdidas económicas para identificar oportunidades de reducción de mermas. | **5** |
| **20** | **US21** | Historial de inventario y mermas | Como propietario, encargado o responsable administrativo, deseo consultar y exportar el historial de productos, lotes y mermas para analizar incidencias y mantener evidencia de las operaciones realizadas. | **5** |
| **21** | **US17** | Análisis de rotación de inventario | Como propietario o gerente de un negocio, deseo analizar la rotación de mis productos para mejorar las decisiones relacionadas con compra, reposición y utilización del inventario. | **5** |
| **22** | **US18** | Impacto económico de las pérdidas evitadas | Como propietario o gerente de un negocio, deseo consultar una estimación del valor económico asociado con los productos que evitaron convertirse en merma para evaluar los beneficios obtenidos mediante una mejor gestión del inventario. | **5** |
| **23** | **US22** | Sugerencias de reposición de inventario | Como responsable de compras o inventario, deseo recibir sugerencias de reposición basadas en el comportamiento histórico de los productos para reducir el sobrestock y las pérdidas. | **8** |
| **24** | **US09** | Configuración de alertas | Como administrador del negocio, deseo configurar las preferencias y responsables de las alertas para asegurar que las incidencias sean comunicadas a las personas correspondientes. | **5** |
| **25** | **US19** | Asignación de responsables de alertas | Como administrador del negocio, deseo asignar responsables para las alertas críticas para asegurar que las incidencias sean atendidas por las personas correspondientes. | **3** |
| **26** | **US05** | Acceso desde diferentes dispositivos | Como propietario, gerente o encargado de un negocio, deseo acceder a FreshSense desde computadoras, tablets y dispositivos móviles para consultar la información de mis productos durante la operación diaria. | **5** |
| **27** | **US16** | Experiencia accesible para entornos operativos | Como colaborador de un restaurante o negocio de alimentos fríos, deseo utilizar una experiencia clara y accesible para realizar mis actividades de manera sencilla durante la operación diaria. | **5** |
| **28** | **US15** | Inducción de nuevos colaboradores | Como administrador del negocio, deseo que los nuevos colaboradores dispongan de una guía inicial de uso para facilitar la adopción de FreshSense. | **3** |
| **29** | **US28** | Gestión de colaboradores | Como propietario o gerente de un negocio, deseo incorporar colaboradores a FreshSense para que puedan realizar las actividades correspondientes a sus responsabilidades. | **5** |
| **30** | **US27** | Administración de usuarios y roles | Como administrador del negocio, deseo gestionar los roles y permisos de los colaboradores para controlar las funcionalidades a las que puede acceder cada usuario. | **5** |
| **31** | **TS43** | Servicio de autenticación y autorización basada en roles | Como Developer, deseo implementar mecanismos de autenticación y autorización basada en roles para proteger los recursos de FreshSense y limitar las operaciones de acuerdo con los permisos de cada usuario. | **8** |
| **32** | **US26** | Recuperación de contraseña | Como colaborador registrado, deseo recuperar el acceso a mi cuenta cuando olvide mi contraseña para continuar utilizando FreshSense de manera segura. | **3** |
| **33** | **US29** | Consulta de facturación | Como responsable administrativo del negocio, deseo consultar los comprobantes asociados con la suscripción de FreshSense para mantener el control de los gastos relacionados con el servicio. | **5** |
| **34** | **TS44** | Integración de pagos y suscripciones | Como Developer, deseo integrar un servicio de procesamiento de pagos recurrentes para actualizar automáticamente el estado de las suscripciones contratadas por los negocios. | **8** |
| **35** | **TS45** | Optimización de consultas frecuentes | Como Developer, deseo implementar un mecanismo de almacenamiento temporal para optimizar las consultas frecuentes de inventario y productos sin comprometer la consistencia de la información. | **5** |

<div style="page-break-after: always;"></div>

# Capítulo IV: Strategic-Level Software Design

## 4.1. Strategic-Level Attribute-Driven Design

### 4.1.1. Design Purpose

### 4.1.2. Attribute-Driven Design Inputs

#### 4.1.2.1. Primary Functionality (Primary User Stories)

#### 4.1.2.2. Quality Attribute Scenarios

#### 4.1.2.3. Constraints

### 4.1.3. Architectural Drivers Backlog

### 4.1.4. Architectural Design Decisions

### 4.1.5. Quality Attribute Scenario Refinements

## 4.2. Strategic-Level Domain-Driven Design

### 4.2.1. EventStorming

### 4.2.2. Candidate Context Discovery

### 4.2.3. Domain Message Flows Modeling

### 4.2.4. Bounded Context Canvases

### 4.2.5. Context Mapping

## 4.3. Software Architecture

### 4.3.1. Software Architecture System Landscape Diagram

### 4.3.2. Software Architecture Context Level Diagrams

### 4.3.3. Software Architecture Container Level Diagrams

### 4.3.4. Software Architecture Deployment Diagrams

<div style="page-break-after: always;"></div>

# Capítulo V: Tactical-Level Software Design

## 5.X. Bounded Context: <Bounded Context Name>

### 5.X.1. Domain Layer

### 5.X.2. Interface Layer

### 5.X.3. Application Layer

### 5.X.4. Infrastructure Layer

### 5.X.6. Bounded Context Software Architecture Component Level Diagrams

### 5.X.7. Bounded Context Software Architecture Code Level Diagrams

#### 5.X.7.1. Bounded Context Domain Layer Class Diagrams

#### 5.X.7.2. Bounded Context Database Design Diagram

<div style="page-break-after: always;"></div>

# Capítulo VI: Solution UX Design

## 6.1. Style Guidelines

### 6.1.1. General Style Guidelines

### 6.1.2. Web, Mobile & Devices Style Guidelines

## 6.2. Information Architecture

### 6.2.2. Labeling Systems

### 6.2.3. Searching Systems

### 6.2.4. SEO Tags and Meta Tags

### 6.2.5. Navigation Systems

## 6.3. Landing Page UI Design

### 6.3.1. Landing Page Wireframe

### 6.3.2. Landing Page Mock-up

## 6.4. Applications UX/UI Design

### 6.4.1. Applications Wireframes

### 6.4.2. Applications Wireflow Diagrams

### 6.4.3. Applications Mock-ups

### 6.4.4. Applications User Flow Diagrams

## 6.5. Applications Prototyping

<div style="page-break-after: always;"></div>

# Capítulo VII: Product Implementation, Validation & Deployment

## 7.1. Software Configuration Management

### 7.1.1. Software Development Environment Configuration

### 7.1.2. Source Code Management

### 7.1.3. Source Code Style Guide & Conventions

### 7.1.4. Software Deployment Configuration

## 7.2. Solution Implementation

### 7.2.X. Sprint n

#### 7.2.X.1. Sprint Planning n

#### 7.2.X.2. Sprint Backlog n

#### 7.2.X.3. Development Evidence for Sprint Review

#### 7.2.X.4. Testing Suite Evidence for Sprint Review

#### 7.2.X.5. Execution Evidence for Sprint Review

#### 7.2.X.6. Services Documentation Evidence for Sprint Review

#### 7.2.X.7. Software Deployment Evidence for Sprint Review

#### 7.2.X.8. Team Collaboration Insights during Sprint

## 7.3. Validation Interviews

### 7.3.1. Diseño de Entrevistas

### 7.3.2. Registro de Entrevistas

### 7.3.3. Evaluaciones según heurísticas

## 7.4. Video About-the-Product

<div style="page-break-after: always;"></div>

# Conclusiones

# Conclusiones y recomendaciones

# Video About-the-Team

# Bibliografía

# Anexos
