
# Curso de Django

## Flujo de Trabajo

### 1. Prender el ambiente virtual
```bash
source venv/bin/activate
```

### 2. Descargar la versión actualizada del código
(Asegúrate de hacer `git pull` si estás trabajando con un repositorio remoto.)

### 3. Aplicar migraciones
```bash
python manage.py migrate
```

### 4. Correr servidor local
```bash
python manage.py runserver
```

### 5. Detener servidor local
Para detener el servidor, presiona:
```bash
ctrl-c
```

### 6. Apagar el ambiente virtual
```bash
deactivate
```

---

## Crear Proyectos y Aplicaciones/Módulos

### 1. Crear un nuevo proyecto de Django
```bash
django-admin startproject nombre_proyecto
```

### 2. Crear una nueva app/módulo
```bash
python manage.py startapp nombre_app
```

---

## Generar y Aplicar Migraciones

### 1. Generar migraciones
```bash
python manage.py makemigrations
```

### 2. Aplicar migraciones
```bash
python manage.py migrate
```

---

## Shell

### Abrir el shell interactivo de Django
```bash
python manage.py shell
```

---

## Documentación Relevante
- [Django Official Documentation](https://docs.djangoproject.com/en/5.1/)
