load "ordenes_servicio.csv";
filter column "ciudad" == "Barranquilla" AND filter column "estado_servicio" == "Pendiente";
aggregate average column "calificacion_cliente";
aggregate between column "costo_estimado";
aggregate sum column "costo_estimado";
print;