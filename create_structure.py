import os

folders = [
    "app/core",
    "app/models",
    "app/schemas",
    "app/repositories",
    "app/services",
    "app/routes",
    "app/utils",
]

files = [
    "app/main.py",
    "app/core/database.py",
    "app/models/__init__.py",
    "app/schemas/__init__.py",
    "app/routes/__init__.py",
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    open(file, "a").close()

print("Estrutura criada com sucesso!")
