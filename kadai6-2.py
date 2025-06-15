import requests

url = "https://opendata.city.minato.tokyo.jp/dataset/1cb38aa1-d066-4a57-b127-aedbdae50124/resource/6dfab8e2-e784-4f64-89a4-f11e513f094b/download/shinryoujyo.json"

response = requests.get(url)
geojson = response.json()

features = geojson['features']

# 施設名称を抽出
names = [f['properties']['施設名称'] for f in features]

for name in names:
    print(name)


# データ名称：港区診療所
# 概要：東京都港区の診療所の名称情報
# エンドポイント："https://opendata.city.minato.tokyo.jp/dataset/1cb38aa1-d066-4a57-b127-aedbdae50124/resource/6dfab8e2-e784-4f64-89a4-f11e513f094b/download/shinryoujyo.json"
# 機能:港区内の診療所の施設名称を取得できる
