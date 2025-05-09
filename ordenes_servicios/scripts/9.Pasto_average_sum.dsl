load "ordenes_servicio.csv";
filter column "ciudad" == "Pasto";
aggregate average column "costo_estimado";
aggregate sum column "costo_estimado";
print;