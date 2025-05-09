load "ordenes_servicio.csv";
filter column "ciudad" == "Pasto";
aggregate count column "cliente";
print;