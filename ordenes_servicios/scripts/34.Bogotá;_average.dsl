load "ordenes_servicio.csv";
filter column "ciudad" == "Bogotá";
aggregate average column "costo_estimado";
print;