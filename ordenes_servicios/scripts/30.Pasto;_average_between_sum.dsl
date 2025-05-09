load "ordenes_servicio.csv";
filter column "ciudad" == "Pasto";
aggregate between column "costo_estimado";
aggregate average column "calificacion_cliente";
aggregate sum column "costo_estimado";
print;