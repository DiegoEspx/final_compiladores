load "ordenes_servicio.csv";
filter column "ciudad" == "Cali";
aggregate between column "costo_estimado";
print;