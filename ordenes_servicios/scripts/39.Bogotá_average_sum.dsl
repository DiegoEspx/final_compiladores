load "ordenes_servicio.csv";
filter column "ciudad" == "Bogotá" AND filter column "estado_servicio" == "Completado";
aggregate average column "costo_estimado";
aggregate sum column "costo_estimado";
print;