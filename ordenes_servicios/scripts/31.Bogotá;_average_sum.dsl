load "ordenes_servicio.csv";
filter column "ciudad" == "Bogotá";
aggregate sum column "costo_estimado";
aggregate average column "calificacion_cliente";
print;