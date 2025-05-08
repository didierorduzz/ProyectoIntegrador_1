CREATE TABLE usuarios (
  id_usuario NUMBER PRIMARY KEY,
  nombre VARCHAR2(100),
  correo VARCHAR2(100) UNIQUE,
  contrasena VARCHAR2(100),
  rol VARCHAR2(20)
);

CREATE TABLE prestamos (
  id_prestamo NUMBER PRIMARY KEY,
  edificio VARCHAR2(100)
  sala VARCHAR2(50),
  hora_reserva VARCHAR2(10),
  fecha_reserva DATE,
  observaciones VARCHAR2(500)
);

CREATE TABLE profesores_autorizados (
    id NUMBER PRIMARY KEY,
    nombre VARCHAR2(100) NOT NULL,
    correo VARCHAR2(100) NOT NULL UNIQUE
);

CREATE TABLE reportes (
  id_reporte NUMBER PRIMARY KEY,
  usuario VARCHAR2(100),
  sala VARCHAR2(50),
  descripcion VARCHAR2(500),
  fecha_reporte DATE
);