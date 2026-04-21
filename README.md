# 🧠 TechBlog Django

TechBlog es una aplicación web tipo blog desarrollada con Django, que permite a los usuarios registrarse, iniciar sesión y gestionar publicaciones mediante operaciones CRUD. El sistema integra autenticación, filtros dinámicos, formularios conectados a base de datos y un panel de administración personalizado.

---

## 🎯 Objetivo del proyecto

El objetivo del proyecto es implementar un sistema web completo utilizando Django, aplicando conceptos como:

- Patrón MTV (Model - Template - View)
- Autenticación de usuarios
- Formularios dinámicos con ModelForm
- Uso del ORM de Django
- Control de accesos
- Administración de datos

---

## 🧱 Arquitectura del sistema

El sistema sigue el patrón **MTV (Model - Template - View)**:

- **Model:** Define la estructura de datos
- **View:** Maneja la lógica del sistema
- **Template:** Presenta la información al usuario

---

## 🧩 Modelos implementados

### 📌 Post
Representa una publicación del blog.

- titulo
- resumen
- contenido
- categoria (ForeignKey)
- autor (User)
- fecha_creacion
- fecha_publicacion
- estado (borrador / publicado)

---

### 📌 Categoria
Clasifica las publicaciones.

- nombre (único)

---

### 📌 Comentario
Permite agregar comentarios a los posts.

- post (relación)
- autor
- contenido
- fecha_creacion

---

## 🔐 Sistema de autenticación

Se utiliza el sistema de autenticación de Django basado en el modelo `User`.

### Funcionalidades:

- Registro de usuarios
- Inicio de sesión personalizado
- Cierre de sesión
- Restricción de acceso a vistas

---

## 👤 Usuarios, roles y permisos

El sistema maneja dos tipos principales de usuarios:

### 👤 Usuario normal
- Puede registrarse desde la web
- Puede iniciar sesión
- Puede visualizar publicaciones
- Puede crear publicaciones únicamente si ha iniciado sesión
- Puede editar únicamente sus propias publicaciones

---

### 🛠️ Administrador (superuser)
- Accede al panel `/admin/`
- Gestiona todos los datos del sistema
- No utiliza la interfaz pública del blog

👉 El acceso del administrador a la web está restringido mediante lógica en las vistas.

--

## 🔒 Control de accesos

Se implementan diferentes niveles de seguridad:

### 1. Autenticación obligatoria

