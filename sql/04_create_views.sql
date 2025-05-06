CREATE OR REPLACE VIEW vista_prestamos_detalle AS
SELECT p.id_prestamo, u.nombre, p.sala, p.fecha_reserva, p.hora_reserva
FROM prestamos p
JOIN usuarios u ON p.usuario_id = u.id_usuario;