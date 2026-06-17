# PulseCore DC · Operations Dashboard ◈

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

## Resumen Ejecutivo

**PulseCore DC Operations Center** es una plataforma analítica integral y un panel de control interactivo diseñado para la gestión y monitoreo de un centro de datos ficticio Tier III de misión crítica ubicado en Querétaro, México. 

El proyecto consolida en una sola interfaz las operaciones físicas, la eficiencia energética, el cumplimiento de normativas de seguridad globales y la inteligencia de mercado del sector de Data Centers en México. Esta herramienta está pensada para proporcionar a ingenieros de instalaciones, gerentes de operaciones y tomadores de decisiones una visión de 360 grados sobre el estado de la infraestructura.

---

## Características y Módulos Principales

El proyecto adopta una arquitectura *Multipage* en Streamlit, dividiendo el dominio del negocio en 5 módulos especializados:

### 1. Operaciones (SLA y Mantenimiento) \[`01_operations.py`\]
* **Monitoreo de SLAs:** Seguimiento en tiempo real del tiempo de actividad (*Uptime*) de energía, enfriamiento y red contra el objetivo Tier III (99.982%).
* **Gestión de Incidentes:** Registro detallado de fallas con cálculo dinámico del MTTR (Mean Time To Resolve) y su evolución mensual.
* **Procesos MAC:** Visualización del flujo de solicitudes Move, Add, Change (MAC) para la gestión del piso franco.

### 2. Eficiencia Energética \[`02_energy.py`\]
* **Análisis de PUE (Power Usage Effectiveness):** Comparativa histórica a 12 meses frente al estándar de la industria.
* **Distribución de Carga:** Desglose del consumo total de 14.2 MW (Equipos de TI, Enfriamiento, Distribución).
* **Simulador Interactivo:** Calculadora en tiempo real para estimar el PUE y los costos operativos anuales basados en variaciones de carga TI y tarifas de energía (MXN/kWh).

### 3. Seguridad y Cumplimiento \[`03_security.py`\]
* **Auditoría Continua:** Checklists interactivos de los controles físicos y lógicos requeridos por los frameworks **TIA-942** e **ISO 27001**.
* **Visualización de Dominio:** Gráficos de radar que evalúan el nivel de madurez por dominio de la norma (Control de Accesos, Continuidad de Negocio, Gestión de Activos, etc.).

### 4. Inteligencia de Mercado \[`04_market.py`\]
* **Proyecciones Financieras:** Análisis del tamaño del mercado de Data Centers en México (2024-2030) basado en datos reales (Arizton, Mordor Intelligence).
* **Inversión y Competencia:** Distribución de capacidad instalada por región (ej. Bajío 31.6%) y seguimiento de inversiones de Hyperscalers (AWS, Azure, Google Cloud).

### 5. Tecnologías Emergentes \[`05_emerging_tech.py`\]
* **Radar de Innovación:** Evaluación en 4 cuadrantes (Adoptar, Probar, Evaluar, Pausar) de tecnologías disruptivas como Enfriamiento Líquido (Direct-to-chip), IA/GPUs y Edge Computing.
* **Hoja de Ruta:** Línea de tiempo interactiva de madurez tecnológica de 2024 a 2030.

---

## Arquitectura y Tecnologías

El despliegue de esta aplicación sigue las mejores prácticas de **DevOps e Infraestructura como Código (IaC)**, asegurando que el entorno sea escalable, reproducible y aislado.

### Stack Tecnológico
* **Frontend y Capa de Presentación:** Streamlit (Python 3.11).
* **Ingeniería de Datos y Visualización:** Pandas para manipulación de DataFrames y Plotly para gráficos interactivos de alto rendimiento.
* **Contenedores:** Docker, estandarizando el entorno de ejecución independientemente del sistema operativo anfitrión.
* **Infraestructura (Cloud):** Terraform y Amazon Web Services (AWS). Configurado para desplegar la imagen de Docker en un clúster de **AWS ECS (Elastic Container Service)** utilizando perfiles de red VPC, subredes públicas/privadas y grupos de seguridad.
* **CI/CD:** GitHub Actions (configurado en el directorio `.github/`) para la integración y despliegue continuo.

---

## 🗂️ Estructura del Repositorio

```text
pulsecore-dc-dashboard/
├── .github/                # Flujos de trabajo de CI/CD para automatizar el build de Docker
├── infra/                  # Archivos de Terraform para el despliegue en AWS ECS
│   ├── main.tf             # Definición de VPC, ECS Cluster, Task Definitions y Load Balancers
│   ├── outputs.tf          # URLs y direcciones IP de salida post-despliegue
│   └── variables.tf        # Parametrización (regiones de AWS, tipos de instancia)
├── pages/                  # Vistas modulares de la aplicación Streamlit
│   ├── 01_operations.py    
│   ├── 02_energy.py        
│   ├── 03_security.py      
│   ├── 04_market.py        
│   └── 05_emerging_tech.py 
├── utils/                  
│   ├── __init__.py
│   └── data_loader.py      # Hooks futuros para conexión a bases de datos SQL o APIs externas
├── .gitignore              # Exclusión de credenciales, entornos virtuales y binarios
├── Dockerfile              # Construcción de la imagen multi-capa y Healthchecks
├── app.py                  # Punto de entrada principal (Entrypoint de Streamlit)
└── requirements.txt        # Dependencias de pip bloqueadas por versión
```

Guía de Despliegue y Ejecución
Existen tres vías principales para ejecutar este proyecto, desde desarrollo local hasta un ambiente de producción en la nube.

1. Entorno de Producción en AWS (Terraform + Docker)
Para lanzar la aplicación de manera pública, altamente disponible y escalable utilizando la definición de infraestructura existente en /infra:

Asegúrate de tener configurado el AWS CLI con tus credenciales (aws configure). Inicializa Terraform y aplica los cambios:

Bash
cd infra
terraform init
terraform plan
terraform apply -auto-approve
Terraform devolverá la URL pública (DNS del Load Balancer o IP de la tarea ECS) al finalizar.

2. Ejecución Local con Docker (Aislado)
Ideal para probar el contenedor antes de mandarlo a la nube, garantizando que todo funcione en el puerto 8501.

Bash
# Construir la imagen localmente etiquetándola como 'pulsecore'
docker build -t pulsecore-dashboard .

# Ejecutar el contenedor mapeando el puerto 8501 local al 8501 del contenedor
docker run -p 8501:8501 pulsecore-dashboard
3. Desarrollo Local (Entorno Virtual de Python)
Para desarrollar, editar código en vivo y ver los cambios inmediatamente sin necesidad de reconstruir la imagen de Docker.

Bash
# Clonar repositorio
git clone https://github.com/tu-usuario/pulsecore-dc-dashboard.git
cd pulsecore-dc-dashboard

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # En sistemas Windows usa: venv\Scripts\activate

# Instalar los paquetes necesarios
pip install -r requirements.txt

# Ejecutar la aplicación (se abrirá en tu navegador por defecto)
streamlit run app.py
Trabajo Futuro (Roadmap)
[ ] Integración de Base de Datos: Conectar utils/data_loader.py a una base de datos PostgreSQL o AWS RDS para extraer métricas operativas.

[ ] Autenticación: Implementar un sistema de login integrado con AWS Cognito para restringir el acceso a módulos críticos.

[ ] Alertas en Tiempo Real: Configurar Webhooks para generar alertas automáticas cuando el PUE supere el umbral objetivo de 1.50.

Desarrollado y diseñado para monitoreo de infraestructura de misión crítica.
