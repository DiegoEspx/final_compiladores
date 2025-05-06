load "ordenes_servicio.csv";
filter column "ciudad" == "Pasto" AND filter column "estado_servicio" == "Completado";
aggregate count column "id_orden";
aggregate sum column "costo_estimado";
aggregate average column "calificacion_cliente";
aggregate between column "costo_estimado";
print;
