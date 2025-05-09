load "ordenes_servicio.csv";
filter column "ciudad" == "Barranquilla";
aggregate count column "cliente";
print;