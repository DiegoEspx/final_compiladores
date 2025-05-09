load "ordenes_servicio.csv";
filter column "ciudad" == "Bogotá";
aggregate count column "id_orden";
aggregate sum column "costo_estimado";
aggregate between column "costo_estimado";
print;