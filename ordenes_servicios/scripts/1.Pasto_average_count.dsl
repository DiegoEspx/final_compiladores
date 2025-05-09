load "ordenes_servicio.csv";
filter column "ciudad" == "Pasto" AND filter column "estado_servicio" == "Completado";
aggregate average column "costo_estimado";
aggregate count column "cliente";
print;