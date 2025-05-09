load "ordenes_servicio.csv";
filter column "ciudad" == "Medellín";
aggregate between column "costo_estimado";
aggregate count column "cliente";
aggregate average column "costo_estimado";
print;