load "ordenes_servicio.csv";
filter column "ciudad" == "Pasto" AND filter column "estado_servicio" == "Pendiente";
aggregate count column "cliente";
print;