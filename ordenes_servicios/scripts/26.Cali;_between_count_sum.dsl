load "ordenes_servicio.csv";
filter column "ciudad" == "Cali";
aggregate sum column "costo_estimado";
aggregate count column "id_orden";
aggregate between column "costo_estimado";
print;