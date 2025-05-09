load "ordenes_servicio.csv";
filter column "ciudad" == "Medellín" AND filter column "estado_servicio" == "Cancelado";
aggregate sum column "costo_estimado";
aggregate between column "costo_estimado";
aggregate count column "id_orden";
print;