load "ordenes_servicio.csv";
filter column "ciudad" == "Pasto";
aggregate count column "id_orden";
aggregate average column "costo_estimado";
print;
