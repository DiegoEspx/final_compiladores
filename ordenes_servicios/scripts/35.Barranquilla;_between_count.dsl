load "ordenes_servicio.csv";
filter column "ciudad" == "Barranquilla";
aggregate between column "costo_estimado";
aggregate count column "cliente";
print;