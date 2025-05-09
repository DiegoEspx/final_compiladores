load "ordenes_servicio.csv";
filter column "ciudad" == "Barranquilla" AND filter column "estado_servicio" == "Completado";
aggregate count column "id_orden";
aggregate between column "costo_estimado";
aggregate average column "costo_estimado";
print;