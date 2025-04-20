#!/bin/sh

# Esperar a que el servicio db esté listo
until mysql -h db -u root -ptest321 -e "SELECT 1"; do
    echo "Esperando por la base de datos..."
    sleep 1
done

echo "Base de datos lista. Iniciando aplicación..."
exec "$@"
