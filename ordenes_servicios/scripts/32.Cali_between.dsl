load "ordenes_servicio.csv";
filter column "ciudad" == "Cali" AND filter column "estado_servicio" == "Completado";
aggregate between column "costo_estimado";
print;