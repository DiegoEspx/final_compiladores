load "ordenes_servicio.csv";
filter column "ciudad" == "Bogotá" AND filter column "estado_servicio" == "Pendiente";
aggregate sum column "costo_estimado";
aggregate between column "costo_estimado";
print;