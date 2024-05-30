docker-compose up -d influxdb grafana
Write-Output "--------------------------------------------------------------------------------------"
Write-Output "Load testing with Grafana dashboard http://localhost:3000/d/Bw_rWDBIz/k6-load"
Write-Output "--------------------------------------------------------------------------------------"
docker-compose run --rm k6 run /scripts/stressTest.js
