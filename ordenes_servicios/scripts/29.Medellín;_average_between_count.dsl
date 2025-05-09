load "ordenes_servicio.csv";
filter column "ciudad" == "Medellín";
aggregate average column "costo_estimado";
aggregate count column "cliente";
aggregate between column "costo_estimado";
print;