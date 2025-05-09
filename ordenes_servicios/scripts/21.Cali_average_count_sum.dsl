load "ordenes_servicio.csv";
filter column "ciudad" == "Cali" AND filter column "estado_servicio" == "Completado";
aggregate sum column "costo_estimado";
aggregate count column "cliente";
aggregate average column "calificacion_cliente";
print;