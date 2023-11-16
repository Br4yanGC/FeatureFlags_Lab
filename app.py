from UnleashClient import UnleashClient
from flask import Flask, request, jsonify
import requests
from datetime import datetime
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def search_city():
  email = request.args.get('email')
  city = request.args.get('city')

  client = UnleashClient(
    url="http://localhost:4242/api",
    app_name="new-feature",
    custom_headers={'Authorization': 'default:development.dde5711f05a4550e930c72642c16a1860cee0c49c7a2fc7faebfaf66'}
  )

  client.initialize_client()

  app_context = {"userId": email}
  validate = client.is_enabled("new-feature", app_context)

  with open("output.txt", "a") as file:
      if (validate):
          print(1)
          file.write(f"{email}: TRUE\n")
      else:
          print(2)
          file.write(f"{email}: FALSE\n")

  if (validate):
    # Verifica si se proporcionó el parámetro 'city'
    if not city:
      return jsonify({'error': 'El parámetro "city" es obligatorio'}), 400

    # URL de la API de Nominatim
    api_url = 'https://nominatim.openstreetmap.org/search'

    # Parámetros de la solicitud
    params = {
      'q': city,
      'format': 'json'
    }

    # Realiza la solicitud a la API de Nominatim
    response = requests.get(api_url, params=params)
    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
      data = response.json()
      result = {
      "latitude": data[0]['lat'],
      "longitude": data[0]['lon']
      }   

      return jsonify(result)
    else:
      return jsonify({'error': 'Error al realizar la solicitud a la API'}), 500
  else:
    # Verifica si se proporcionó el parámetro 'city'
    if not city:
      return jsonify({'error': 'El parámetro "city" es obligatorio'}), 400

    # URL de la API de Nominatim
    api_url = 'https://geocoding-api.open-meteo.com/v1/search'

    # Parámetros de la solicitud
    params = {
      'name': city,
      'format': 'json'
    }

    # Realiza la solicitud a la API de Nominatim
    response = requests.get(api_url, params=params)
    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
      data = response.json()
      result = {
        "latitude": data["results"][0]['latitude'],
        "longitude": data["results"][0]['longitude']
      }   

      return jsonify(result)
    else:
      return jsonify({'error': 'Error al realizar la solicitud a la API'}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
