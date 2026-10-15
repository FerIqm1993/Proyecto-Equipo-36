# 🚀 Proyecto Equipo 36 — Hackathon ONE G10

Bienvenido al repositorio oficial del **Equipo 36** para el **Hackathon ONE (Oracle Next Education & Alura)**.

Este repositorio contiene la solución completa de **CommunityLab**: un motor inteligente de ingestión, análisis semántico con IA Generativa, curaduría humana y persistencia en la nube de **Oracle Cloud Infrastructure (OCI)**.

---

## 📁 Estructura del Repositorio

El proyecto se encuentra organizado dentro del módulo [`communitylab/`](communitylab/):

```text
communitylab/
├── README.md                                 # Documentación técnica completa y arquitectura
├── .gitignore                                # Exclusiones de Git
├── workflows/                                # Workflows automatizados de n8n
│   ├── WF1-ingesta-analisis-generacion.json  # Ingesta, análisis semántico con LLM y generación
│   ├── WF2-curaduria-oci.json                # Curaduría hacia OCI Object Storage Always Free
│   └── WF3-metricas-diarias.json             # Cálculo de métricas y observabilidad diaria
├── dashboard/                                # Aplicación de Curaduría en Streamlit
│   ├── dashboard_curaduria.py                # Interfaz Human-in-the-Loop
│   ├── requirements.txt                      # Dependencias Python
│   └── README-dashboard.md                   # Manual de uso del dashboard
└── docs/
    └── capturas/                             # Evidencias de ejecución y capturas
```

---

## ⚡ Enlaces Rápidos

- 📖 **[Documentación Completa del Proyecto](communitylab/README.md)**
- 🤖 **[Workflows de n8n](communitylab/workflows/)**
- 🖥️ **[Dashboard de Curaduría Streamlit](communitylab/dashboard/)**
- 🛡️ **[Guía del Dashboard](communitylab/dashboard/README-dashboard.md)**

---
*Desarrollado con dedicación por el Equipo 36 — Hackathon ONE G10 (Oracle & Alura).*
