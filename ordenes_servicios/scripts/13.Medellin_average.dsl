load "ordenes_servicio.csv";
filter column "ciudad" == "Medellín" AND filter column "estado_servicio" == "Completado";
aggregate average column "calificacion_cliente";
print;