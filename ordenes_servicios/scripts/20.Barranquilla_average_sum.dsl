load "ordenes_servicio.csv";
filter column "ciudad" == "Barranquilla" AND filter column "estado_servicio" == "Cancelado";
aggregate average column "calificacion_cliente";
aggregate sum column "costo_estimado";
print;