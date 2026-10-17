"""
CommunityLab — Asistente de Configuración de Secrets para Streamlit
===================================================================
Este script toma el archivo JSON de la Service Account de Google Cloud
(descargado directamente desde Google Cloud Console) y el ID de tu Google Sheet,
y genera automáticamente `.streamlit/secrets.toml` con el formato exacto requerido.

Uso rápido desde terminal:
    python configurar_secrets.py credenciales.json "1nY40IJ4ludaHQcTEV8nDlHNi6ikl-4x5CUJocvrsHfk"
    
O uso interactivo (te preguntará los datos paso a paso):
    python configurar_secrets.py
"""

import json
import os
import re
import sys
from pathlib import Path


def extraer_spreadsheet_id(texto: str) -> str:
    """Extrae el ID del Google Sheet si el usuario pasó la URL completa."""
    match = re.search(r"/spreadsheets/d/([a-zA-Z0-9-_]+)", texto)
    if match:
        return match.group(1)
    return texto.strip()


def main():
    print("=" * 70)
    print("🛡️  CommunityLab — Generador Automático de Secrets (.streamlit/secrets.toml)")
    print("=" * 70)

    json_path = None
    spreadsheet_input = None
    worksheet_name = "Curaduria"

    # 1. Leer argumentos si fueron pasados por CLI
    if len(sys.argv) >= 3:
        json_path = sys.argv[1]
        spreadsheet_input = sys.argv[2]
        if len(sys.argv) >= 4:
            worksheet_name = sys.argv[3]
    else:
        # Modo interactivo
        print("\n👉 Modo interactivo:")
        archivos_json = [f for f in os.listdir(".") if f.endswith(".json") and not f.startswith("package")]
        sugerencia_json = archivos_json[0] if archivos_json else "service_account.json"

        entrada_json = input(f"1. Ruta al archivo JSON de GCP [{sugerencia_json}]: ").strip()
        json_path = entrada_json or sugerencia_json

        entrada_sheet = input("2. ID o URL completa de tu Google Sheet: ").strip()
        while not entrada_sheet:
            entrada_sheet = input("   ⚠️ Por favor ingresa el ID o la URL de tu Google Sheet: ").strip()
        spreadsheet_input = entrada_sheet

        entrada_pestana = input("3. Nombre de la pestaña [Curaduria]: ").strip()
        if entrada_pestana:
            worksheet_name = entrada_pestana

    # Validar archivo JSON
    if not os.path.exists(json_path):
        print(f"\n❌ Error: No se encontró el archivo '{json_path}'.")
        print("Asegúrate de colocar el archivo JSON de tu Service Account en esta carpeta.")
        sys.exit(1)

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            creds = json.load(f)
    except Exception as e:
        print(f"\n❌ Error al leer el JSON '{json_path}': {e}")
        sys.exit(1)

    # Validar campos esenciales de la Service Account
    campos_requeridos = ["type", "project_id", "private_key", "client_email"]
    for campo in campos_requeridos:
        if campo not in creds:
            print(f"\n❌ Error: El archivo JSON no parece ser una Service Account válida (falta '{campo}').")
            sys.exit(1)

    spreadsheet_id = extraer_spreadsheet_id(spreadsheet_input)

    # Asegurar que private_key tenga saltos de línea escapados para TOML
    raw_key = creds.get("private_key", "")
    escaped_key = raw_key.replace("\r", "").replace("\n", "\\n")

    # Construir contenido TOML
    toml_content = f"""# =============================================================================
# CommunityLab — Configuración de Secretos de Streamlit
# Generado automáticamente por configurar_secrets.py
# =============================================================================

spreadsheet_id = "{spreadsheet_id}"
worksheet_name = "{worksheet_name}"

[gcp_service_account]
type = "{creds.get('type', 'service_account')}"
project_id = "{creds.get('project_id', '')}"
private_key_id = "{creds.get('private_key_id', '')}"
private_key = "{escaped_key}"
client_email = "{creds.get('client_email', '')}"
client_id = "{creds.get('client_id', '')}"
auth_uri = "{creds.get('auth_uri', 'https://accounts.google.com/o/oauth2/auth')}"
token_uri = "{creds.get('token_uri', 'https://oauth2.googleapis.com/token')}"
auth_provider_x509_cert_url = "{creds.get('auth_provider_x509_cert_url', 'https://www.googleapis.com/oauth2/v1/certs')}"
client_x509_cert_url = "{creds.get('client_x509_cert_url', '')}"
"""

    # Guardar en .streamlit/secrets.toml
    out_dir = Path(".streamlit")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "secrets.toml"

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(toml_content)

    print("\n" + "=" * 70)
    print(f"✅ ¡Archivo generado exitosamente en: {out_file}!")
    print("=" * 70)
    print("\n📌 INFORMACIÓN IMPORTANTE:")
    print(f"1. Email del Service Account:  {creds.get('client_email')}")
    print(f"2. Google Sheet ID vinculado: {spreadsheet_id}")
    print(f"3. Pestaña:                   {worksheet_name}")
    print("\n⚠️ PASO OBLIGATORIO FINAL:")
    print(f"   Debes compartir tu Google Sheet con este correo:")
    print(f"   👉 {creds.get('client_email')}")
    print("   con rol de 'Editor' para que la app pueda leer y escribir aprobaciones.\n")

    print("-" * 70)
    print("☁️ SI DESEAS DESPLEGAR EN STREAMLIT COMMUNITY CLOUD:")
    print("   Copia todo el bloque TOML de arriba y pégalo en:")
    print("   share.streamlit.io -> Tu App -> Settings -> Secrets.")
    print("-" * 70)


if __name__ == "__main__":
    main()
