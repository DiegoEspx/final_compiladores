load "ordenes_servicio.csv";
filter column "ciudad" == "Medellín" AND filter column "estado_servicio" == "Cancelado";
aggregate average column "costo_estimado";
aggregate sum column "costo_estimado";
print;