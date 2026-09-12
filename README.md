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

El desperdicio de alimentos es un problema grave en el Perú tanto a nivel económico como ambiental. Según la información explicada en el II Foro Nacional de la Recuperación de Alimentos y Conmemoración del Día de Concienciación sobre la Pérdida y el Desperdicio de Alimentos en el Perú, realizado por la FOA (Organización de la Naciones Unidas para la Alimentación y la
Agricultura) junto con MIDAGRI (Ministerio de Desarrollo Agrario y Riego) y PMA (Programa Mundial de Alimentos), en el país, 12.8 millones de toneladas de alimentos se pierden en la cadena de producción (FOA, 2024). Es un número muy preocupante considerando que el 51% de las familias peruanas está en situación de inseguridad alimentaria (Blas, 2022). A partir de ello, es claro que hay una relación estrecha entre el desperdicio de alimentos y la inseguridad alimentaria; el gobierno se está encargando de mitigar tal desperdicio mediante foros, proyectos, etc. Teniendo en cuenta este contexto, Enrique Román, representante asistente de FAO en Perú señala que los hogares peruanos representan el 16% en el desperdicio de alimentos (FAO, 2024), un porcentaje alarmante. Más aún, acorde a Alberto Huiman, doctor en Ciencias Ambientales, cada peruano genera un desperdicio de 67 kilogramos por año y los restaurantes es alrededor de 500 kilogramos por día. Esto complica gravemente la situación del país respecto a las pérdidas en el aspecto de alimentos.  

Para analizar con más detalle los antecedentes y problemáticas, se realizó con anticipación la técnica 5 ‘W’s & 2 ‘H’s:

#### What? (¿Qué es?)

FreshSense es una aplicación web diseñada para facilitar el monitoreo del inventario alimenticio, y evita el desperdicio de alimentos mediante el uso de alarmas y notificaciones. Esto permite que los usuarios tengan mejor control de lo que tienen en el refrigerador y puedan cocinar acorde a lo que tienen disponible, que es una de las formas óptimas de prevenir el desperdicio (Casimiro & Delgado, 2020, p. 27).

#### Why? (¿Por qué?)

Es necesario realizar una aplicación de monitoreo de inventario por la falta de información precisa y oportuna sobre las condiciones reales dentro del refrigerador (temperatura, humedad, gas etileno) hace que los usuarios no puedan anticipar la descomposición de alimentos, resultando en desperdicio y pérdidas económicas.

#### Where? (¿Dónde?)

Se aplica en la mayoría de los restaurantes y minimarkets en Lima, principalmente dentro de
refrigeradores donde se almacenan frutas, verduras y otros productos perecederos.

#### When? (¿Cuándo?)

El desperdicio ocurre frecuentemente cuando los alimentos permanecen almacenados por tiempos prolongados sin monitoreo adecuado, intensificándose en días o semanas, según el tipo de alimento. Es por ello que la aplicación surgió como una solución para esos problemas.

#### Who? (¿Quién?)

Esta aplicación está enfocada en minimarkets que buscan mantener un monitoreo exhaustivo de sus productos y tiene en cuenta la sostenibilidad ambiental. Asimismo, se incluye
restaurantes, mypes que necesitan una manera eficiente de monitorear su inventario alimenticio.

#### How? (¿Cómo?)

Se desarrolla FreshSense con miras a proveer la mejor experiencia para el usuario, por ello se definen los siguientes puntos importantes sobre su funcionamiento:
• El usuario sube los alimentos que tiene disponibles en el refrigerador
• A partir de esa información, para los hogares genera recetas acordes al inventario. Para los
hogares y restaurantes manda alarmas y notificaciones de los alimentos que están prontos
a vencer. Incluye dashboards para monitorear los comestibles de manera rápida.
• Incluye suscripciones que brindan nuevas funcionalidades a los usuarios.

#### How much? (¿Cuánto?)

El desperdicio de alimentos genera un impacto fuerte en la economía de los hogares, el hecho de que los peruanos desperdicien alrededor de 67 kilogramos en alimentos por año implica un gasto
innecesario.
Para poder mantener FreshSense y monetizar a partir del producto se tiene en cuenta:
• Las suscripciones disponibles en la aplicación (se considera versión mensual y anual)
• Venta del dispositivo sensor (pago único entre 80 a 190 soles)

### 1.2.2. Lean UX Process

#### 1.2.2.1. Lean UX Problem Statements

El estado actual de la conservación de alimentos es deficiente en restaurantes pequeños y minimarkets. En ambos segmentos, los propietarios y gerentes desperdician alimentos debido a la falta de información precisa y anticipada sobre su estado dentro de refrigeradores y almacenes, así como la ausencia de alertas preventivas que les permitan tomar decisiones oportunas respecto a su conservación, rotación de inventario y consumo de los mismos.

Creemos que reducir el desperdicio de alimentos permitirá que los minimarkets y restaurantes pequeños optimicen sus costos operativos mejorando el margen de ganancia. Sabremos que esto es cierto cuando el porcentaje de alimentos reportados como utilizados antes de la fecha de alerta supere el 70% durante el primer mes de uso.
Creemos que permitir el acceso a la aplicación desde múltiples dispositivos (PC, móvil) facilitará que los encargados de cocina y gerentes de minimarket monitoreen el inventario en tiempo real, mejorando la gestión diaria del negocio. Sabremos que esto es cierto cuando al menos el 50% de los usuarios activos inicien sesión desde dos o más tipos de dispositivos en la primera semana tras la adopción.
Creemos que agregar funciones premium como análisis detallado de rotación de inventario, reportes de pérdidas y alertas automáticas de vencimiento incentivarán a los usuarios a suscribirse y optimizar su operación. Sabremos que esto es cierto cuando al menos el 30% de los usuarios activos se suscriban al plan premium dentro de los tres primeros meses de uso.
Creemos que incluir sugerencias inteligentes de menú basadas en ingredientes próximos a vencer motivará a restaurantes pequeños a aprovechar mejor sus insumos y reducir el desperdicio operativo. Sabremos que esto es cierto cuando al menos el 40% de los usuarios implementen las recomendaciones al menos una vez por semana durante el primer mes de uso.

#### 1.2.2.2. Lean UX Assumptions

##### Business Assumptions:

Creemos que nuestros usuarios necesitan una plataforma que les permita monitorear el estado de su inventario alimenticio de manera eficiente y provea soluciones para optimizar la rotación de productos antes de que venzan, reduciendo pérdidas económicas.
Estas necesidades se pueden resolver con una aplicación web intuitiva que brinde un inventario organizado y accesible para todo el equipo, además de un dashboard que muestre toda la información necesaria mediante gráficos, alertas automáticas y reportes de rentabilidad.
Nuestros clientes iniciales son restaurantes pequeños y minimarkets que cuentan con bodegas y refrigeradores comerciales, y buscan una solución que les permita evitar pérdidas económicas por desperdicio, controlar y monitorear productivamente su inventario alimenticio, y optimizar márgenes de ganancia.
El valor #1 que un cliente requiere de nuestro servicio es que muestre la información del estado de sus productos de manera detallada, fácil de entender y en tiempo real para tomar decisiones operativas inmediatas.

El cliente también puede obtener estos beneficios adicionales como sugerencias de menú basadas en productos próximos a vencer, reportes analíticos de rotación de inventario y análisis de márgenes de ganancia por producto.

Adquiriremos a nuestros clientes a través de una landing page que muestre cómo funciona la aplicación, qué beneficios operativos y económicos ofrece, una forma de contactarnos y cómo FreshSense es una herramienta indispensable para el manejo eficiente del inventario alimenticio y la rentabilidad de restaurantes pequeños y minimarkets. Asimismo, tendremos una estrategia de marketing digital y ventas directas B2B enfocada en los segmentos objetivos que hemos definido.

Haremos dinero a través de suscripciones mensuales para servicios premium y funcionalidades avanzadas de análisis.
Nuestra competencia de mercado serán aplicaciones genéricas de inventario, sistemas POS básicos, y métodos tradicionales de control manual de stock con cuadernos o spreadsheets.
Los venceremos porque ofrecemos una solución accesible y especializada para restaurantes y minimarkets, eficiente y basada en las tecnologías más recientes. Nuestro modelo de suscripción brinda más funcionalidades específicas a un costo razonable comparado con sistemas empresariales costosos que no se adaptan a negocios pequeños.
Nuestros mayores riesgos son la preferencia por aplicaciones más básicas, la resistencia al cambio tecnológico, el deseo de mantener un inventario de manera tradicional o manual, y la dificultad de integración con sistemas POS existentes.

Resolveremos esto mediante el desarrollo del producto enfocándonos en las necesidades específicas de usuarios, proveer una solución intuitiva y fácil de usar que no sobrecargue al usuario con funcionalidades complejas, ofrecer integraciones con sistemas POS populares, y brindar soporte técnico dedicado.
Sabremos que hemos tenido éxito cuando observemos estos cambios en el comportamiento de nuestros clientes: reducción de al menos 20% en pérdidas por desperdicio de alimentos, disminución significativa de kilogramos de inventario no utilizado anualmente, y mejora medible en los márgenes de ganancia operativa de cada negocio.
Qué otras suposiciones tenemos que, de probarse falsas, pueden causar que nuestro proyecto fracase: Suponer que nuestros segmentos objetivos (restaurantes pequeños y minimarkets) prefieren una solución tecnológica que sea fácil de acceder mediante dispositivos portátiles (celular, tablet, laptop) e integrable con sus operaciones diarias sin interrupciones.

##### Business Outcomes:
Reducir en al menos un 25% las pérdidas económicas por desperdicio de alimentos en restaurantes pequeños y minimarkets durante el primer año de uso del sistema.
Generar un ahorro económico mensual a los usuarios de al menos 15% en costos de inventario, esto sería medido a través de encuestas y análisis de reportes de la aplicación.
Conseguir una tasa de retención del 60% de los usuarios después de los primeros seis meses de uso de la aplicación.
Alcanzar 200 usuarios (restaurantes pequeños y minimarkets) en los primeros cinco meses tras el lanzamiento del producto.
Conseguir que más del 40% de usuarios pague la suscripción premium ofrecida para acceder a reportes avanzados y análisis de rentabilidad.
User Assumptions:

¿Quiénes serán nuestros usuarios?

##### Nuestros usuarios principales son:

Propietarios y gerentes de restaurantes pequeños (capacidad de 20-100 platos diarios) que están constantemente ocupados en operaciones diarias, pero necesitan gestionar su inventario alimenticio de forma sencilla y eficiente sin dedicar horas a tareas administrativas.
Dueños y encargados de minimarkets que necesitan controlar la frescura de sus productos para garantizar calidad, minimizar pérdidas económicas y optimizar la rotación de stock.
¿Dónde encaja nuestro producto en su vida o trabajo?
Para propietarios y gerentes de restaurantes pequeños con necesidad de gestionar su inventario eficientemente: FreshSense encaja exactamente en un proceso crítico de su operación diaria. El hecho de tener una aplicación que les brinde visibilidad del estado de los alimentos, alertas de vencimiento y sugerencias de menú ahorra tiempo de inspección manual, evita desperdicios costosos, y optimiza el flujo de trabajo de cocina.
Para dueños de minimarkets con necesidad de controlar la frescura de sus productos para garantizar calidad y minimizar pérdidas: FreshSense encaja en un proceso muy importante del negocio: el manejo y monitoreo del inventario. Con esta aplicación, el encargado tiene conocimiento preciso del estado de los productos en tiempo real. Asimismo, brinda la oportunidad de tener reportes semanales sobre rotación de inventario sin necesidad de estar revisando constantemente los estantes y refrigeradores.
¿Qué problemas tiene nuestro producto y cómo se pueden resolver?

##### Problemas:

El control de inventario en restaurantes pequeños y minimarkets se realiza mediante métodos manuales: inspección visual, cuadernos de registro o, en el mejor de los casos, simples spreadsheets.
Los pequeños negocios no tienen visibilidad en tiempo real del estado de sus productos, lo que resulta en compras innecesarias, desperdicio y pérdida de márgenes de ganancia.
La falta de automatización hace que tareas de monitoreo de inventario consuman horas valiosas que podrían dedicarse a mejorar servicio al cliente o crecimiento del negocio.

##### Soluciones:

Mostrar a propietarios y gerentes de restaurantes la facilidad y beneficio financiero inmediato que brinda FreshSense. En este caso, sería necesario incrementar anuncios y testimonios que expresen cómo FreshSense impacta de manera positiva la rentabilidad y eficiencia operativa del negocio.
Promocionar las funcionalidades que ofrece FreshSense a través de demostraciones, casos de estudio y análisis de ROI. De esta manera, los restaurantes pequeños y minimarkets se mostrarán interesados por la solución tecnológica que puede aumentar sus ganancias.
¿Cómo y cuándo es usado nuestro producto?

FreshSense es utilizada por los propietarios, gerentes y encargados que necesitan una manera de monitorear su inventario de alimentos en restaurantes pequeños y minimarkets. En el caso de los restaurantes, permite controlar el estado de los ingredientes, recibir alertas de vencimiento, y obtener sugerencias de menú basadas en productos próximos a vencer para optimizar su uso y evitar desperdicio. Por otro lado, para los minimarkets, lo utilizan porque necesitan asegurarse de que los productos estén frescos, controlar rotación de stock, y minimizar pérdidas económicas. Es utilizado a lo largo de toda la jornada operativa: al abrir el negocio, durante el inventario diario, y al cerrar para registrar lo utilizado.

¿Qué características son importantes?
La UI de la aplicación debe de ser clara, intuitiva y profesional para ambos segmentos objetivos. Los usuarios deben de ser capaces de utilizar el producto sin necesidad de tutoriales extensivos, enfocándose en su operación diaria.
Las notificaciones son críticas para alertar al usuario sobre qué alimentos están cerca a su vencimiento, qué productos están agotándose, y cuándo es necesario hacer reorden para que puedan tomar decisiones operativas inmediatas y evitar interrupciones en el servicio.
La capacidad de generar reportes automatizados es importante para que gerentes puedan analizar tendencias de desperdicio, rotación de inventario y márgenes de ganancia sin dedicar tiempo a tareas manuales.

¿Cómo debe verse y comportarse nuestro producto?
El producto debe de estar activo las 24 horas del día, los 7 días a la semana debido a la importancia que significa para las operaciones diarias del negocio, incluyendo acceso móvil para consultas rápidas desde la cocina o el mostrador.
La aplicación debe verse profesional y moderna, con paleta de colores que evoque frescura y naturaleza (tonalidades de verde y azul). Asimismo, cada color debe combinar adecuadamente para una visualización clara que facilite la lectura rápida de información crítica.
La navegación debe permitir acceso rápido a información crítica (productos próximos a vencer, nivel bajo de stock, reportes diarios) sin necesidad de múltiples clics.

##### User Outcomes:
Adopción de prácticas de gestión de inventario más eficientes y basadas en datos, reduciendo pérdidas económicas.
Uso frecuente de las sugerencias de menú que provee la aplicación para optimizar uso de ingredientes y mejorar márgenes de ganancia.
Revisión del estado de inventario de manera frecuente a través de la aplicación web y móvil durante operaciones diarias.
Reducción significativa de acumulación de productos olvidados o vencidos en bodegas y refrigeradores.
Mejora en la planificación de compras y reórdenes, basada en datos reales de consumo y rotación.
Mayor confianza en la calidad de productos servidos al cliente final gracias a visibilidad mejorada del estado de ingredientes.

##### Features Assumptions:
Desde la cuenta de un propietario o gerente de restaurante pequeño:
Los usuarios deben poder agregar los alimentos e ingredientes que tienen en bodega y refrigeradores, además de la fecha de vencimiento, cantidad disponible, y costo unitario. Asimismo, pueden proveer una descripción breve y categoría de dicho producto.
Recibir notificaciones automáticas que alerten de los alimentos que están próximos a su vencimiento para que puedan incorporarlos en el menú del día o planificación de platos especiales.
Acceder a sugerencias inteligentes de menú basadas en ingredientes disponibles y próximos a vencer, permitiendo que el chef/cocinero optimice el uso de recursos y reduzca desperdicio.
Generar reportes semanales y mensuales que detallen rotación de inventario, productos con mayor desperdicío, márgenes de ganancia por producto, y tendencias de consumo.
Diferentes logros u hitos que puede obtener el negocio al utilizar la aplicación (reducción de desperdicio %, eficiencia operativa, etc.). Esto permite que los usuarios se sientan motivados a mantener buenos hábitos de gestión.
Desde la cuenta de un dueño o encargado de minimarket:
Recibir notificaciones automáticas que les avisen de los productos que están próximos a su vencimiento para hacer reorden o promociones.
Tener disponible información clara y en tiempo real sobre cómo se encuentra el estado del inventario por sección o categoría de productos (perecederos, bebidas, lácteos, etc.).
Acceder a alertas de stock bajo para saber cuándo es necesario hacer reorden y evitar desabastecimiento.
Reportes semanales y mensuales que ayuden al usuario a entender cómo va su inventario, qué productos se rotan más rápido, cuáles generan más pérdidas, y cuál es el impacto económico del desperdicio.
Análisis de patrones de compra y demanda para optimizar futuras compras y maximizar ganancias.

#### 1.2.2.3. Lean UX Hypothesis Statements

Creemos que nuestros usuarios (propietarios y gerentes) necesitan una plataforma que les permita monitorear el estado de su inventario alimenticio de manera eficiente y provea soluciones para utilizar dichos productos antes de que venzan, optimizando rotación de stock.
Estas necesidades se pueden resolver con una aplicación web intuitiva que brinde un inventario organizado y accesible para todo el equipo, además de un dashboard que muestre toda la información necesaria mediante gráficos, alertas automáticas y reportes de rentabilidad.
Nuestros clientes iniciales son restaurantes pequeños y minimarkets que cuentan con bodegas y refrigeradores comerciales, y buscan una solución que les permita evitar pérdidas económicas por desperdicio, controlar y monitorear productivamente su inventario alimenticio.
El valor #1 que un cliente requiere de nuestro servicio es que muestre la información del estado de sus productos de manera detallada, fácil de entender y accesible en tiempo real para tomar decisiones operativas inmediatas.
El cliente también puede obtener estos beneficios adicionales como sugerencias de menú basadas en productos próximos a vencer, reportes analíticos de rotación de inventario y análisis de márgenes de ganancia por producto.
Adquiriremos a nuestros clientes a través de una landing page que muestre cómo funciona la aplicación, qué beneficios operativos y económicos ofrece, una forma de contactarnos y cómo FreshSense es una herramienta indispensable para el manejo eficiente del inventario alimenticio y la rentabilidad de restaurantes pequeños y minimarkets. Asimismo, tendremos una estrategia de marketing digital y ventas directas B2B enfocada en los segmentos objetivos que hemos definido.
Haremos dinero a través de suscripciones mensuales para servicios premium y funcionalidades avanzadas de análisis.
Nuestra competencia de mercado serán aplicaciones genéricas de inventario, sistemas POS básicos, y aplicaciones simples de notas para anotaciones manuales de stock.
Los venceremos porque ofrecemos una solución accesible, especializada para restaurantes y minimarkets, eficiente y basada en las tecnologías más recientes. Nuestro modelo de suscripción brinda más funcionalidades específicas a un costo razonable comparado con sistemas empresariales costosos que no se adaptan a negocios pequeños.
Nuestros mayores riesgos son la preferencia por aplicaciones más básicas, la resistencia al cambio tecnológico, el deseo de mantener un inventario de manera tradicional o manual, y la dificultad de integración con sistemas existentes.
Resolveremos esto mediante el desarrollo del producto enfocándonos en las necesidades específicas de usuarios, proveer una solución intuitiva y fácil de usar que no sobrecargue al usuario con funcionalidades complejas, ofrecer integraciones con sistemas POS populares, y brindar soporte técnico dedicado.
Sabremos que hemos tenido éxito cuando observemos estos cambios en el comportamiento de nuestros clientes: reducción de al menos 20% en pérdidas por desperdicio de alimentos, disminución significativa de kilogramos de inventario no utilizado anualmente, y mejora medible en los márgenes de ganancia operativa de cada negocio.
Qué otras suposiciones tenemos que, de probarse falsas, pueden causar que nuestro proyecto fracase: Suponer que nuestros segmentos objetivos (restaurantes pequeños y minimarkets) prefieren una solución tecnológica que sea fácil de acceder mediante dispositivos portátiles (celular, tablet, laptop) e integrable con sus operaciones diarias sin interrupciones.

#### 1.2.2.4. Lean UX Canvas

## 1.3. Segmentos objetivo

Para el proyecto FreshSense se han seleccionado dos segmentos principales de usuarios a los cuales la solución aporta un valor claro y adaptado a sus necesidades específicas:

Restaurantes pequeños y minimarkets. Esta situación se ve agravada por la falta de herramientas accesibles que permitan monitorear factores críticos como la temperatura, humedad y niveles de gas etileno, estos factores influyen directamente en la conservación y vida útil de los alimentos. Esto se debe a que dichas herramientas están mayormente enfocadas en grandes cadenas comerciales y empresas de distribución, siendo inaccesibles económicamente para negocios pequeños.

En consecuencia, los propietarios y gerentes de restaurantes pequeños y minimarkets sufren de pérdidas económicas constantes por desperdicio de inventario, reducción de márgenes de ganancia, y contribuyen al impacto ambiental negativo generado por el desperdicio de alimentos.

¿Cómo podríamos mejorar el monitoreo y disponibilidad de información sobre el estado de los alimentos en las bodegas y refrigeradores de restaurantes pequeños y minimarkets para que optimicen la rotación de inventario, reduzcan pérdidas económicas y disminuyan el desperdicio de alimentos?

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
