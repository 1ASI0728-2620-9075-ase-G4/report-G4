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

## 3.2. User Stories

## 3.3. Impact Mapping

## 3.4. Product Backlog

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

FreshSense establece un conjunto de lineamientos visuales y de interacción orientados a mantener una experiencia consistente entre el Landing Page, la aplicación web, la aplicación móvil y la experiencia asociada al dispositivo IoT.

La solución está dirigida principalmente a **empresas de distribución y cadena de frío** y a **empresas productoras y comercializadoras de alimentos perecibles**. Por ello, la experiencia visual prioriza claridad, confiabilidad y rápida interpretación de información relacionada con monitoreo ambiental, lotes, dispositivos, alertas y trazabilidad.

Los recursos visuales del producto, como logotipos, imágenes, tipografías y demás elementos gráficos, se centralizarán en la carpeta `Assets/` del repositorio para mantener una referencia común entre todos los integrantes del equipo.

### 6.1.1. General Style Guidelines

Los lineamientos generales de FreshSense definen la identidad visual y comunicacional utilizada en los diferentes productos digitales que forman parte de la solución.

#### Branding

La identidad de FreshSense está orientada a transmitir **frescura, control, trazabilidad, tecnología y confiabilidad**.

La marca busca representar una solución tecnológica que permita a las empresas monitorear las condiciones de conservación de productos perecibles durante su almacenamiento y distribución, facilitando la detección de desviaciones y reduciendo las pérdidas asociadas al deterioro de productos.

El diseño visual mantiene una apariencia limpia y profesional, evitando interfaces excesivamente cargadas. Los elementos relacionados con monitoreo, conservación, alertas, dispositivos y trazabilidad deben utilizarse de manera consistente en todos los productos digitales.

#### Typography

FreshSense utiliza la familia tipográfica **Poppins** debido a su apariencia moderna, limpia y legible en interfaces digitales.

Se establece la siguiente jerarquía tipográfica:

- **H1:** títulos principales de páginas y mensajes de mayor importancia.
- **H2:** títulos de secciones.
- **H3:** subtítulos y encabezados de componentes.
- **Body:** contenido descriptivo, datos y textos de apoyo.
- **Labels:** nombres de campos, indicadores, filtros y estados.

La jerarquía debe mantenerse de manera consistente en las experiencias Web y Mobile para facilitar la lectura y comprensión de la información.

#### Colors

La paleta cromática de FreshSense está compuesta principalmente por verde, azul, tonos neutros y blanco.

| Color | Uso principal |
|---|---|
| **Green - Primary** | Acciones principales, indicadores de condiciones adecuadas y elementos asociados a conservación. |
| **Blue - Secondary** | Monitoreo, información tecnológica, gráficos y componentes secundarios. |
| **Gray - Neutral** | Textos secundarios, etiquetas, íconos y divisores. |
| **White - Background** | Fondos principales, tarjetas y espacios de contenido. |
| **Text - Base** | Información principal y contenido de alta prioridad. |

Los estados que requieran atención podrán utilizar indicadores visuales diferenciados según su nivel de severidad. Sin embargo, el color no será el único mecanismo de comunicación; cada estado deberá estar acompañado por texto o iconografía que permita comprender claramente la situación.

#### Spacing & Layout

FreshSense utiliza una estructura modular para mantener consistencia entre páginas y componentes.

**Base Unit**

- Size: `8 px`
- Uso: unidad base para márgenes, paddings y separación entre elementos.

**Grid System**

- Grid: `12 columnas`
- Gutter: `22 px`
- Margins: proporcionales a la unidad base.

**Section Spacing**

- Standard section: `56 px`
- Hero section: `72 px`
- Footer: `36–56 px`

**Cards & Components**

- Internal padding: `18–22 px`
- Border radius: `16 px`
- Elevation: `0 10px 25px rgba(0,0,0,.08)`

**Alignment**

- Contenido principal dentro de un contenedor máximo de `1120 px` o `92%` del ancho disponible.
- El contenido textual se alinea principalmente a la izquierda para facilitar su lectura.
- Los indicadores críticos y métricas principales deberán tener mayor jerarquía visual.
- Se utilizarán espacios amplios entre grupos de información para diferenciar claramente cada sección.

#### Tone of Voice

El tono de comunicación de FreshSense busca transmitir profesionalismo, confianza y claridad, debido a que la solución presenta información utilizada para supervisar las condiciones de conservación de productos perecibles.

| Dimensión | Orientación de FreshSense | Justificación |
|---|---|---|
| Divertido / Serio | **Serio** | Los datos de monitoreo y las alertas requieren una comunicación clara y confiable. |
| Formal / Casual | **Formal** | La solución está orientada a organizaciones y procesos empresariales. |
| Respetuoso / Irreverente | **Respetuoso** | Los mensajes deben orientar al usuario sin generar confusión. |
| Entusiasta / Sereno | **Sereno** | Las incidencias deben comunicarse con claridad sin utilizar mensajes alarmistas. |

Los mensajes del sistema deben ser breves, precisos y orientados a una acción concreta.

Ejemplos:

- `Temperature above allowed range`
- `Device disconnected`
- `Cold chain deviation detected`
- `Reading updated successfully`
- `Lot requires attention`

### 6.1.2. Web, Mobile & Devices Style Guidelines

FreshSense mantiene una identidad visual consistente entre sus diferentes interfaces. Los usuarios deben reconocer los mismos colores, tipografía, iconografía, indicadores y terminología independientemente de si utilizan la aplicación web o móvil.

#### Web Style Guidelines

El Landing Page y la aplicación web utilizarán principios de **Material Design**, manteniendo consistencia en componentes como botones, formularios, tarjetas, tablas, menús, indicadores y mensajes de estado.

Para la versión Desktop del Landing Page se utilizará principalmente el **patrón de lectura Z**, dirigiendo inicialmente la atención hacia la marca, propuesta de valor y Call-to-Action principal.

Posteriormente, el contenido presentará el funcionamiento de FreshSense, sus principales beneficios y la solución específica para cada segmento empresarial.

En pantallas de menor tamaño, el contenido adoptará una estructura principalmente vertical.

La aplicación web priorizará la visualización de información relacionada con:

- Dashboard.
- Monitoring.
- Inventory.
- Lots.
- Devices.
- Alerts.
- Traceability.
- Reports.

Los datos provenientes del dispositivo IoT, como temperatura, humedad, última lectura y estado de conexión, se presentarán mediante tarjetas, tablas, indicadores y gráficos que permitan identificar rápidamente desviaciones o situaciones que requieran atención.

#### Mobile Style Guidelines

La aplicación móvil mantendrá los mismos principios visuales definidos para la aplicación web, adaptando la distribución a pantallas de menor tamaño.

Se priorizarán las funcionalidades que requieren consulta rápida:

- Estado general del monitoreo.
- Alertas activas.
- Lecturas recientes.
- Estado de dispositivos.
- Estado de lotes.

La información se organizará principalmente en una sola columna y se priorizarán los eventos o condiciones que requieran atención inmediata.

Los nombres, colores, iconos y estados serán equivalentes a los utilizados en Web para reducir la curva de aprendizaje entre plataformas.

#### Device Style Guidelines

El dispositivo IoT actual de FreshSense funciona como un nodo de monitoreo encargado de registrar las condiciones ambientales relacionadas con la conservación de productos perecibles.

El prototipo utiliza un microcontrolador **ESP32** junto con un sensor **DHT22** para obtener periódicamente información de temperatura y humedad.

Las mediciones son transmitidas mediante Wi-Fi hacia el Edge API y posteriormente enviadas al backend de FreshSense para su almacenamiento, procesamiento y visualización.

El prototipo físico actual no incorpora una pantalla ni controles de interacción directa documentados. Por ello, la interacción del usuario con el dispositivo se realiza principalmente mediante las aplicaciones digitales de FreshSense.

Los principales elementos relacionados con el dispositivo utilizarán etiquetas simples y consistentes:

| Elemento | Label |
|---|---|
| Estado del dispositivo | `Connected` / `Disconnected` |
| Temperatura | `Temperature` |
| Humedad | `Humidity` |
| Última medición | `Last Reading` |
| Estado del monitoreo | `Monitoring Status` |
| Identificador | `Device ID` |

La interfaz debe permitir que el usuario comprenda el estado del dispositivo y de las condiciones monitoreadas sin necesidad de conocer detalles técnicos como el funcionamiento del ESP32, DHT22, JSON o Edge API.

#### Internationalization & Accessibility

FreshSense considera dos locales principales:

- `en_US` - English.
- `es_419` - Latin American Spanish.

El idioma predeterminado de las interfaces será **English**, manteniendo disponible la estructura necesaria para presentar los mismos contenidos en español latinoamericano.

En las experiencias Web se utilizarán atributos ARIA para facilitar el uso de tecnologías de asistencia.

Asimismo, los estados importantes no serán representados únicamente mediante colores, sino también mediante texto, iconos u otros indicadores reconocibles.

La estructura visual, las etiquetas y los componentes mantendrán consistencia entre ambos idiomas.

## 6.2. Information Architecture

La arquitectura de información de FreshSense está diseñada para que los visitantes y usuarios puedan comprender rápidamente la propuesta del producto y acceder a información relacionada con monitoreo, dispositivos, productos perecibles, alertas y trazabilidad sin recorrer estructuras complejas.

La organización considera las necesidades de los dos segmentos principales:

- **Empresas de distribución y cadena de frío:** organizaciones encargadas del transporte, distribución o almacenamiento de productos perecibles que requieren supervisar continuamente las condiciones de conservación.
- **Empresas productoras y comercializadoras de alimentos perecibles:** organizaciones que producen, almacenan o comercializan alimentos y necesitan controlar las condiciones de sus productos y reducir pérdidas asociadas al deterioro.

La arquitectura considera el Landing Page, la aplicación web, la aplicación móvil y las funcionalidades asociadas al monitoreo mediante dispositivos IoT.

### 6.2.2. Labeling Systems

El sistema de etiquetado de FreshSense utiliza términos breves, consistentes y fáciles de reconocer.

Se evita mostrar terminología técnica relacionada con la implementación cuando no aporta valor directo al usuario.

#### Landing Page

| Label | Propósito |
|---|---|
| `Home` | Regresar al inicio. |
| `Solution` | Presentar la solución FreshSense. |
| `How It Works` | Explicar el funcionamiento general del sistema. |
| `Benefits` | Presentar los principales beneficios. |
| `For Cold Chain` | Información dirigida a empresas de distribución y cadena de frío. |
| `For Producers` | Información dirigida a productores y comercializadores. |
| `Contact` | Presentar los medios de contacto. |
| `Sign In` | Acceder a la plataforma. |
| `Get Started` | Iniciar el proceso de acceso o registro. |

#### Web and Mobile Applications

| Label | Información asociada |
|---|---|
| `Dashboard` | Resumen general del sistema e indicadores principales. |
| `Monitoring` | Visualización de las condiciones registradas por los dispositivos. |
| `Inventory` | Información de los productos registrados. |
| `Lots` | Gestión y seguimiento de lotes. |
| `Devices` | Gestión de dispositivos IoT asociados. |
| `Alerts` | Eventos o desviaciones que requieren atención. |
| `Traceability` | Historial de eventos y condiciones asociadas a productos o lotes. |
| `Reports` | Información consolidada y resultados de monitoreo. |

#### IoT Monitoring

| Label | Información asociada |
|---|---|
| `Device` | Dispositivo IoT registrado. |
| `Device ID` | Identificador único del dispositivo. |
| `Connected` | Dispositivo comunicándose correctamente. |
| `Disconnected` | Dispositivo sin comunicación con el sistema. |
| `Temperature` | Temperatura obtenida mediante el sensor. |
| `Humidity` | Humedad obtenida mediante el sensor. |
| `Last Reading` | Fecha y hora de la lectura más reciente. |
| `Monitoring Status` | Estado actual del proceso de monitoreo. |

Las etiquetas se mantendrán equivalentes entre las experiencias Web y Mobile para evitar que un mismo concepto tenga diferentes nombres dependiendo de la plataforma.

### 6.2.3. Searching Systems

El sistema de búsqueda se concentra principalmente en las aplicaciones Web y Mobile, donde el volumen de información puede aumentar debido al registro de dispositivos, lotes, productos, lecturas y alertas.

El Landing Page no requiere un buscador interno debido a que su contenido está organizado en un número reducido de secciones accesibles mediante navegación directa.

#### Lots Search

El usuario podrá buscar lotes mediante:

- Lot ID.
- Producto.
- Ubicación.

Los resultados podrán filtrarse según:

- Monitoring Status.
- Fecha.
- Ubicación.
- Producto.

Cada resultado mostrará información relevante del lote y su estado actual.

#### Device Search

Los dispositivos podrán buscarse mediante:

- Device ID.
- Ubicación.

Los resultados podrán filtrarse según:

- Connected.
- Disconnected.
- Fecha de última lectura.

Cada resultado mostrará como mínimo:

- Device ID.
- Connection Status.
- Temperature.
- Humidity.
- Last Reading.

#### Monitoring Search

La información de monitoreo podrá consultarse utilizando:

- Device.
- Lot.
- Rango de fechas.
- Ubicación.

Los resultados mostrarán las principales mediciones registradas durante el período seleccionado.

#### Alerts Search

Las alertas podrán filtrarse según:

- Estado.
- Severidad.
- Fecha.
- Tipo de evento.
- Device.
- Lot.

Por defecto, se mostrarán primero las alertas más recientes y aquellas que requieran mayor atención.

#### Traceability Search

La información de trazabilidad podrá consultarse mediante:

- Lot ID.
- Producto.
- Device.
- Período.

Los resultados se mostrarán cronológicamente para facilitar la revisión de los eventos registrados durante el almacenamiento o distribución del producto.

Cuando una búsqueda no presente coincidencias, la interfaz mostrará un mensaje claro y permitirá modificar o eliminar los filtros aplicados.

### 6.2.4. SEO Tags and Meta Tags

FreshSense utilizará SEO Tags y Meta Tags para representar adecuadamente el contenido del Landing Page y de la aplicación web.

#### Landing Page

| Element | Value |
|---|---|
| **Title** | `FreshSense | Smart Cold Chain Monitoring for Perishable Foods` |
| **Description** | `FreshSense helps companies monitor temperature and humidity conditions during the storage and distribution of perishable food products using IoT technology.` |
| **Keywords** | `cold chain monitoring, perishable food, IoT monitoring, temperature monitoring, humidity monitoring, food traceability, cold storage` |
| **Author** | `FreshSense Team` |

#### Web Application

| Element | Value |
|---|---|
| **Title** | `FreshSense Platform | Monitor Your Cold Chain` |
| **Description** | `Monitor devices, environmental conditions, lots, alerts and traceability information for perishable food products with FreshSense.` |
| **Keywords** | `FreshSense, cold chain, IoT monitoring, food traceability, temperature, humidity, logistics` |
| **Author** | `FreshSense Team` |

#### Mobile Application - ASO

En caso de publicación de la aplicación móvil mediante un App Store, se utilizarán los siguientes elementos:

| Element | Value |
|---|---|
| **App Title** | `FreshSense` |
| **App Subtitle** | `Smart Cold Chain Monitoring` |
| **App Keywords** | `cold chain, food, monitoring, temperature, humidity, traceability, IoT` |
| **App Description** | `FreshSense helps companies monitor environmental conditions, connected devices and alerts related to the storage and distribution of perishable food products.` |

### 6.2.5. Navigation Systems

La navegación de FreshSense busca mantener recorridos simples y consistentes entre el Landing Page y las diferentes aplicaciones.

#### Landing Page - Desktop

La versión Desktop utilizará una barra de navegación superior con acceso a las principales secciones:

`Home | Solution | How It Works | Benefits | For Cold Chain | For Producers | Contact`

Además, se mostrarán las principales acciones:

`Sign In | Get Started`

Los Call-to-Action permitirán dirigir a los usuarios hacia el acceso a la plataforma o hacia información específica relacionada con su segmento.

#### Landing Page - Mobile

En pantallas móviles, las mismas opciones estarán agrupadas en un menú compacto para reducir el espacio utilizado y priorizar el contenido principal.

El orden y significado de las secciones serán equivalentes a los utilizados en Desktop.

#### Web Application

Una vez autenticado, el usuario tendrá acceso a los principales módulos de FreshSense:

`Dashboard | Monitoring | Inventory | Lots | Devices | Alerts | Traceability | Reports`

El **Dashboard** funcionará como punto inicial de la experiencia y permitirá visualizar información relevante como:

- Estado general del monitoreo.
- Dispositivos conectados.
- Alertas activas.
- Lecturas recientes.
- Lotes que requieren atención.

#### Mobile Application

La navegación móvil priorizará las funcionalidades que requieren consulta frecuente:

- Dashboard.
- Monitoring.
- Alerts.
- Devices.
- Lots.

Las funcionalidades complementarias, como Inventory, Traceability y Reports, permanecerán disponibles desde la navegación secundaria.

#### IoT Device Navigation

La interacción con los dispositivos IoT se realiza principalmente mediante las aplicaciones Web y Mobile.

El recorrido principal será:

`Devices → Select Device → Monitoring → Reading Details`

Para el seguimiento de productos, se utilizará:

`Lots → Select Lot → Traceability → Event Details`

Desde estas vistas, el usuario podrá conocer el estado de conexión de los dispositivos, consultar las mediciones de temperatura y humedad y revisar los eventos asociados al monitoreo de cada lote.

Esta organización evita que el usuario necesite interactuar directamente con componentes técnicos como el ESP32 o el sensor DHT22 para utilizar las funciones principales de FreshSense.

## 6.3. Landing Page UI Design

### 6.3.1. Landing Page Wireframe

A continuación se realizaron los wireframes de la landing page de FreshSense, siguiendo los user stories como referencia, para conocer las necesidades y preferencias de los usuarios visitantes:

**Figura 1.** Wireframe de la página principal 
![Hero](Assets/LP_HERO.PNG)

**Figura 2.** Como funciona FreshSense
![Hero](Assets/LP_HTW.PNG) 

**Figura 3.** Vistazo inicial a los beneficios 
![Hero](Assets/LP_BENEFITS.PNG) 

**Figura 4.** Modelo inicial para los planes de subscripción.
![Hero](Assets/LP_PLANS.PNG) 

**Figura 5.** Wireframe para los testimonios
![Hero](Assets/LP_TESTIMONIALS.PNG) 

**Figura 6.** Wireframe para el formulario y se incluye el footer
![Hero](Assets/LP_FORM.PNG)

### 6.3.2. Landing Page Mock-up

Una vez se realizaron los wireframes, usamos los Style Guidelines, para desarrollar el siguiente paso, los mock ups, utilizamos los colores y modelos referidos en los guidelines, los colores verdes y azules predominantes en el diseño, aluden a la escencia de la aplicación:

**Figura 7.** Mock-Up de la página principal 
![Hero](Assets/MK_LP_HERO.PNG) 

**Figura 8.** Mock-Up se muestra las funciones de FreshSense
![Hero](Assets/MK_LP_HIW.PNG) 

**Figura 9.** Vistazo inicial a los beneficios 
![Hero](Assets/MK_LP_BENEFITS.PNG) 

**Figura 10.** Mock-Up para los planes de subscripción.
![Hero](Assets/MK_LP_PLANS.PNG) 

**Figura 11.** Mock-Up para los testimonios
![Hero](Assets/MK_LP_TESTIMONIALS.PNG) 

**Figura 12.** Mock-Up para el formulario y se incluye el footer
![FORM](Assets/MK_LP_FORM.PNG)

## 6.4. Applications UX/UI Design

En la sección de Applications UX/UI Design nos enfocamos en el diseño de la interfaz y la experiencia de usuario de la aplicación web de FreshSenser, donde incluimos una visualización funcional por cada parte del aplicativo con sus flujos de interacción completos. Se elaboraron wireframes en formato mobile que facilitan la disposición de las funciones de la plataforma a través de su dispositivo móvil frecuente, con elementos en pantallas que son la introducción al app, el login up, el sign up, el home o dashboard, el menú, el inventario de insumos, el detalle de cada insumo, el monitoreo de insumos, alertas, recetas, reportes, logros y soporte. En base a estos esquemas se diseñaron los mockups con alta fidelidad. En los siguientes sprints se muestra el desarrollo de cada vista de la app y cómo estas interactúan.

### 6.4.1. Applications Wireframes

En esta sección se presentan los wireframes en formato mobile que facilitan la disposición de las funciones de la plataforma.

![wireframeapp1](Assets/wireframeapp1.png)
![wireframeapp2](Assets/wireframeapp2.png)
![wireframeapp3](Assets/wireframeapp3.png)
![wireframeapp4](Assets/wireframeapp4.png)
![wireframeapp5](Assets/wireframeapp5.png)
![wireframeapp6](Assets/wireframeapp6.png)
![wireframeapp7](Assets/wireframeapp7.png)

### 6.4.2. Applications Wireflow Diagrams

Para este apartado, el wireflow se diseñó para representar de forma detallada el proceso de uso desde el inicio de sesión hasta las funcionalidades principales, como la gestión del inventario de alimentos, el monitoreo en tiempo real, la recepción de alertas, la consulta de recetas, el seguimiento de logros y la personalización de ajustes. De esta manera, se asegura que la navegación sea coherente, intuitiva y centrada en mejorar la experiencia del usuario final.

![alt text](Assets/FreshSense_Web_Applications_Wireflow_Diagrams.png)

### 6.4.3. Applications Mock-ups

![mockupapp1](Assets/mockupapp1.png)
![mockupapp2](Assets/mockupapp2.png)
![mockupapp3](Assets/mockupapp3.png)
![mockupapp4](Assets/mockupapp4.png)
![mockupapp5](Assets/mockupapp5.png)
![mockupapp6](Assets/mockupapp6.png)
![mockupapp7](Assets/mockupapp7.png)

### 6.4.4. Applications User Flow Diagrams

![alt text](Assets/cuadritosFLOW.jpg)

Cada figura del diagrama tiene un significado específico dentro del flujo de usuario:

- Start: punto de inicio del recorrido.

- Page: pantalla normal de la aplicación.

- Option Page: menú o sección con varias opciones.

- End: final del flujo o salida de la app.

- Input: ingreso de datos por parte del usuario.

- Decision: condición que define diferentes caminos.

- Result: acción realizada con éxito.

- Notification: mensaje o alerta mostrado al usuario.

![alt text](Assets/FreshSense_Web_Applications_Userflow_Diagrams.jpg)

Ahora representamos los User Flow Diagrams de la aplicación web FreshSense, los cuales permiten visualizar de manera clara el recorrido que realiza el usuario dentro del sistema, desde que abre la aplicación hasta que cierra sesión. Este diagrama utiliza convenciones gráficas específicas para identificar los distintos tipos de pantallas, acciones, decisiones, resultados y notificaciones que intervienen en la experiencia del usuario. Gracias a esta representación, se facilita el análisis de la interacción, la detección de posibles mejoras en la navegación y la validación de que todos los escenarios de uso estén contemplados.

## 6.5. Applications Prototyping

Para validar la navegación y la interacción de los usuarios con FreshSense se desarrolló un prototipo interactivo de la aplicación. Este prototipo permite recorrer las principales vistas y funcionalidades definidas durante el proceso de diseño UX/UI, simulando el comportamiento esperado de la solución antes de su implementación completa.

El prototipo facilita la validación de los flujos de navegación, la organización de las pantallas y las interacciones entre las diferentes funcionalidades de la aplicación.

El prototipo interactivo de FreshSense puede consultarse en el siguiente enlace:

[Prototipo interactivo de FreshSense en Figma](https://www.figma.com/proto/WMu6m6D3rPs3AI4HYKKbNJ/WireFrames-LandingPage?node-id=159-1605&p=f&t=tnVLge8rsFfHhU1S-1&scaling=min-zoom&content-scaling=fixed&page-id=159%3A1603)

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
