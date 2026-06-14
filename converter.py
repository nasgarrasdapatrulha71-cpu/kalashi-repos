import json
import requests

# Baixar repositório original
url = "https://repos.gabrx.eu.org/nabzclan.json"
response = requests.get(url)
dados = response.json()

# Montar JSON no formato que o Feather aceita (mesmo do manual)
resultado = {
    "name": "Nabzclan Feather Repo",
    "identifier": "com.nabzclan.feather",
    "iconURL": "https://cdn.nabzclan.vip/sidelix/images/logo/logosidelix.jpg",
    "apps": []
}

for app in dados.get("apps", []):
    if app.get("down"):
        resultado["apps"].append({
            "name": app.get("name"),
            "bundleIdentifier": app.get("bundleID"),
            "version": app.get("version"),
            "downloadURL": app.get("down"),
            "iconURL": app.get("iconURL", ""),
            "size": app.get("size", 0)
        })

with open("nabzclan.feather.json", "w") as f:
    json.dump(resultado, f, indent=2)

print(f"OK: {len(resultado['apps'])} apps convertidos")
