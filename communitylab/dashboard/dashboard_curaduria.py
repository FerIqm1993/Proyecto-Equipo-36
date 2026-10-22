"""
CommunityLab — Dashboard de Curaduría & Observabilidad v2.2 (Streamlit)
Submódulo en communitylab/dashboard/dashboard_curaduria.py
(Mantiene paridad total con app.py en la raíz)
"""

import sys
from pathlib import Path

# Añadir la raíz al path para importar cualquier utilidad compartida
root_path = Path(__file__).resolve().parents[2]
if str(root_path) not in sys.path:
    sys.path.insert(0, str(root_path))

# Re-exportar o ejecutar la misma lógica
with open(root_path / "app.py", "r", encoding="utf-8") as f:
    code = f.read()

exec(code, globals())