import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "IPK": 1,
    "Jumlah_Absensi": 2,
    "Waktu_Belajar_Jam": 4,
    "IPK_x_Study": 1 * 4,       # fitur turunan
    "Rasio_Absensi": 2 / 14       # fitur turunan
}

response = requests.post(url, json=data)
print(response.json())
