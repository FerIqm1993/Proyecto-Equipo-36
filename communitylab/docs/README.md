# 📚 Documentación y Evidencias de CommunityLab

Este directorio contiene las guías de apoyo, diagramas y evidencias visuales para la entrega del proyecto en el **Hackathon ONE G10 (Oracle & Alura)**.

---

## 📸 Carpeta de Capturas (`capturas/`)

Para completar la presentación del proyecto o la entrega en Canvas, sugerimos colocar en [`capturas/`](capturas/) las siguientes evidencias de ejecución:

1. **`01_n8n_wf1_ejecucion.png`**:
   - Captura de pantalla de la ejecución exitosa de **WF1** en n8n, mostrando los nodos en verde desde la ingesta hasta la bifurcación y guardado en Google Sheets.
2. **`02_n8n_groq_analisis.png`**:
   - Detalle del nodo HTTP Request hacia Groq LLM mostrando el payload de respuesta JSON con sentimiento y scoring.
3. **`03_dashboard_streamlit_metricas.png`**:
   - Vista superior del Dashboard en Streamlit mostrando las tarjetas de métricas en tiempo real.
4. **`04_dashboard_streamlit_aprobacion.png`**:
   - Vista de un activo siendo revisado o editado con el botón **Aprobar** presionado.
5. **`05_google_sheets_curaduria.png`**:
   - Vista de la hoja de Google Sheets con las columnas actualizadas (`decision = aprobado`, `estado_proceso = pendiente_oci` / `almacenado_oci`).
6. **`06_n8n_wf2_subida_oci.png`**:
   - Ejecución de **WF2** tomando los aprobados y realizando el `PUT` a OCI Object Storage.
7. **`07_oci_object_storage_bucket.png`**:
   - Consola de Oracle Cloud Infrastructure (OCI) mostrando el bucket `communitylab-activos-marketing` con los archivos `.json` persistidos en `activos/`.
8. **`08_n8n_wf3_metricas_diarias.png`**:
   - Ejecución del scheduler diario calculando totales y actualizando la hoja de analítica.

---

## 📑 Recursos Adicionales

- **[README Principal de CommunityLab](../README.md)**: Arquitectura completa, diagramas y acuerdos de datos.
- **[Manual del Dashboard](../dashboard/README-dashboard.md)**: Guía de despliegue local de la aplicación en Streamlit.
- **[Plantilla de Datos Curaduría](../dashboard/plantilla_curaduria.csv)**: Esquema y dataset semilla en formato CSV.
