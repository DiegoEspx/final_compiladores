load "ordenes_servicio.csv";
filter column "ciudad" == "Bogotá" AND filter column "estado_servicio" == "Pendiente";
aggregate average column "calificacion_cliente";
aggregate count column "cliente";
aggregate between column "costo_estimado";
print;
