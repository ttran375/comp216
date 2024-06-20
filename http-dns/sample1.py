import requests

url = "https://httpbin.org/post"

# input = {"k1": "v1", "k2": "v2", "k3": "v3"}
# input = {"k10": "v10", "k20": "v20", "k30": "v30"}

# response = requests.post(url, data=input)
# response = requests.post(url, json=input)

# print(response.headers)
# print(response.json())

filename = "comp216.jpg"
upload_file = open(filename, "rb")

header_values = {
    "Content-Disposition": f"attachment; filename={filename}",
    "Content-Type": "image/jpeg",
}

response_upload = requests.post(
    url, files={"files": upload_file}, headers=header_values
)

upload_file.close()

print(response_upload.json())
