load "ordenes_servicio.csv";
filter column "ciudad" == "Pasto" AND filter column "estado_servicio" == "Pendiente";
aggregate between column "costo_estimado";
aggregate average column "costo_estimado";
aggregate sum column "costo_estimado";
print;