load "ordenes_servicio.csv";
filter column "ciudad" == "Cali" AND filter column "estado_servicio" == "Pendiente";
aggregate sum column "costo_estimado";
print;