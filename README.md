# 🛡️ CommunityLab
### Motor Inteligente de Transformación y Distribución para Comunidades Digitales

> **Hackathon ONE G10 · Oracle Next Education & Alura · Octubre 2026**  
> **Equipo 36**  
> *"La IA propone · El humano decide · OCI guarda solo lo aprobado."*

---

## 📌 ¿Qué es CommunityLab?

**CommunityLab** transforma la actividad orgánica de una comunidad digital (testimonios, dudas, logros dispersos en canales como Discord) en activos de marketing listos para distribución — de forma automatizada, con curación humana obligatoria y persistencia en la nube de Oracle.

---

## 🎯 Pilares del Sistema

1. **🤖 Ingesta y Generación Inteligente (n8n + Groq LLM):**
   - Recibe interacciones por webhook o lotes JSON.
   - Analiza el sentimiento, extrae temas clave y calcula un scoring determinístico.
   - Genera automáticamente 3 formatos de marketing:
     - 📢 **Post de LinkedIn** (historias y testimonios).
     - 💡 **FAQ Dinámico** (solución a dudas técnicas recurrentes).
     - 📰 **Newsletter Semanal** (destacados y logros comunitarios).

2. **👨‍💻 Curaduría Humana Obligatoria (*Human-in-the-Loop*):**
   - Estación de trabajo interactiva en **Streamlit** conectada a **Google Sheets**.
   - Los curadores pueden revisar la sugerencia de la IA, editar el copy en línea y decidir si **Aprobar** o **Rechazar**.
   - Ningún activo se publica ni se sube a la nube sin el consentimiento explícito del curador humano.

3. **☁️ Persistencia Cloud (Oracle Cloud Infrastructure - OCI):**
   - Integración nativa con **OCI Object Storage Always Free**.
   - Persistencia segura y organizada por ejecución y período de referencia únicamente para contenidos aprobados.

4. **📊 Observabilidad y Métricas Diarias:**
   - Flujo automatizado que consolida diariamente el volumen de interacciones, distribución de sentimiento y ratio de aprobación.

---

## 📁 Estructura del Repositorio

El código fuente, flujos automatizados y documentación detallada se encuentran organizados dentro del módulo [`communitylab/`](communitylab/):

```text
communitylab/
├── README.md                                 # Documentación técnica completa y arquitectura
├── .gitignore                                # Exclusiones de Git
├── workflows/                                # Workflows exportados de n8n
│   ├── WF1-ingesta-analisis-generacion.json  # Ingesta, análisis semántico con LLM y generación
│   ├── WF2-curaduria-oci.json                # Curaduría hacia OCI Object Storage Always Free
│   └── WF3-metricas-diarias.json             # Cálculo de métricas y observabilidad diaria
├── dashboard/                                # Aplicación de Curaduría en Streamlit
│   ├── dashboard_curaduria.py                # Interfaz Human-in-the-Loop
│   ├── requirements.txt                      # Dependencias Python
│   └── README-dashboard.md                   # Manual de uso y configuración del dashboard
└── docs/
    └── capturas/                             # Evidencias de ejecución y capturas
```

---

## ⚡ Enlaces Rápidos

- 📖 **[Documentación Técnica Completa](communitylab/README.md)** (Arquitectura Mermaid, Contratos de Datos y Matriz de Cumplimiento)
- 🤖 **[Workflows de n8n](communitylab/workflows/)**
- 🖥️ **[Dashboard de Curaduría Streamlit](communitylab/dashboard/)**
- 🛡️ **[Manual del Dashboard](communitylab/dashboard/README-dashboard.md)**

---
*Desarrollado con dedicación por el **Equipo 36** — Hackathon ONE G10 (Oracle & Alura).*
