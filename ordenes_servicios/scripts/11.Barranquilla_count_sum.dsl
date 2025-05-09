load "ordenes_servicio.csv";
filter column "ciudad" == "Barranquilla";
aggregate count column "id_orden";
aggregate sum column "costo_estimado";
print;