import requests
import pytest

URL = 'https://qa-internship.avito.com/api/1/item'

correct_uid = 'b5854b15-48eb-4088-9ed4-b68758d4ab6b'
uncorrect_uid = 'b5854b15-48eb-4088-9ed4-b68758d4abcd'
seller_id = 664328
uncorrect_seller_id = 'abc'
seller_with_no_obj = 664329


valid_data = {
    "sellerID": 6953127,
  "name": "стол",
  "price": 5000,
  "statistics":{
    "contacts":1,
    "likes":1,
    "viewCount":1
  }
} 

invalid_data  = {
  "sellerID": 6953127,
  "price": 5000,
  "statistics":{
    "contacts":1,
    "likes":1,
    "viewCount":1
  }
}

invalid_field_data = {
  "sellerID": 6953127,
  "name": "стол",
  "price": "цена",
  "statistics":{
    "contacts":1,
    "likes":1,
    "viewCount":1
  }
}

def test_post_with_valid_data():
  response = requests.post('https://qa-internship.avito.com/api/1/item', json=valid_data)
  assert response.status_code == 200

  ans = response.json()
  assert "status" in ans

def test_post_with_invalid_data():
  response = requests.post('https://qa-internship.avito.com/api/1/item', json=invalid_data)
  assert response.status_code == 400

  ans = response.json()
  assert "result" in  ans

def test_post_with_invalid_field_data():
  response = requests.post('https://qa-internship.avito.com/api/1/item', json=invalid_field_data)
  assert response.status_code == 400

  ans = response.json()
  assert "result" in  ans


def test_get_obj_with_correct_uid():
  correct_uid = 'b5854b15-48eb-4088-9ed4-b68758d4ab6b'
  response = requests.get(f"https://qa-internship.avito.com/api/1/item/{correct_uid}")

  assert response.status_code == 200

  ans = response.json()
  assert len(ans) > 0


def test_get_obj_with_uncorrect_uid():
 
  response = requests.get(f"https://qa-internship.avito.com/api/1/item/{uncorrect_uid}")

  assert response.status_code == 404

  ans = response.json()
  assert "result" in ans

def test_get_stat_with_correct_uid():
  
  response = requests.get(f"https://qa-internship.avito.com/api/1/statistic/{correct_uid}")

  assert response.status_code == 200

  ans = response.json()
  assert len(ans) > 0

def test_get_stat_with_uncorrect_uid():
  response = requests.get(f"https://qa-internship.avito.com/api/1/statistic/{uncorrect_uid}")
  assert response.status_code == 404

  ans = response.json()
  assert "result" in ans

def test_get_obj_seller_with_correct_id():
  response = requests.get(f"https://qa-internship.avito.com/api/1/{seller_id}/item")
  assert response.status_code == 200

  ans = response.json()
  assert len(ans) > 0

def test_get_obj_seller_with_uncorrect_id():
  response = requests.get(f"https://qa-internship.avito.com/api/1/{uncorrect_seller_id}/item")
  assert response.status_code == 400

  ans = response.json() 
  assert "result" in ans

def test_get_obj_seller_with_no_obj():
  response = requests.get(f"https://qa-internship.avito.com/api/1/{seller_with_no_obj}/item")
  assert response.status_code == 200

  ans = response.json()
  assert len(ans) == 0
