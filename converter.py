import json

with open('original.json') as f:
    o = json.load(f)

feather = {
    'name': 'Nabzclan Feather Repo',
    'identifier': 'com.nabzclan.feather',
    'iconURL': 'https://cdn.nabzclan.vip/sidelix/images/logo/logosidelix.jpg',
    'apps': []
}

for app in o.get('apps', []):
    if app.get('down'):
        feather['apps'].append({
            'name': app.get('name'),
            'bundleIdentifier': app.get('bundleID'),
            'developerName': 'Nabzclan',
            'version': app.get('version'),
            'versionDate': app.get('versionDate', ''),
            'downloadURL': app.get('down'),
            'iconURL': app.get('iconURL', ''),
            'size': app.get('size', 0)
        })

with open('nabzclan.feather.json', 'w') as f:
    json.dump(feather, f, indent=2)

print(f'Convertidos {len(feather['apps'])} apps')
