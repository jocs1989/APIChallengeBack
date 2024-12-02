# APIChallengeBack

## Modo Local
Este proyecto permite realizar scraping en la web de Tiendas Jumbo para obtener información sobre productos. A continuación, te mostramos cómo ejecutar el proyecto en tu entorno local.

```bash
bash run.sh

```

Despues podra ejecutar el codigo en :
http://localhost:8000/api/doc#/scraper/start_v1_scraper_tiendas_jumbo_post

## Modo Docker

Ejecuta el script :

```bash
bash int.sh

```

## Modo compose:
Ejecuta el comando 

```bash
docker-compose up -d

```


## Se anexan los resultados en una collection de mongo y un json :
- respuesta_tecnica.json
- mongo (Scraper.ChallengeBack)
