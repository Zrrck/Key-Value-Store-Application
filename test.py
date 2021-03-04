import unittest
import requests


class TestKeyValue(unittest.TestCase):

  def get_fresh_link(self):
    return "http://localhost:3000/keys"

  def test_getputdelete(self):
    link = self.get_fresh_link()+'/'
    key = "test"
    value = "value"

    r = requests.put(link, data=key+":"+value)
    self.assertTrue(r.status_code == 201 or r.status_code == 409)

    r = requests.get(link+key)
    self.assertEqual(r.status_code, 200)
    self.assertEqual(r.text, "value")

    r = requests.delete(link+key)
    self.assertEqual(r.status_code, 200)

  def test_headworks(self):
    link = self.get_fresh_link()+'/'
    key = "test"
    value = "value"
    r = requests.put(link, data=key+":"+value)
    self.assertTrue(r.status_code == 201 or r.status_code == 409)

    r = requests.head(link+key)
    self.assertEqual(r.status_code,200)

    r = requests.delete(link+key)
    self.assertEqual(r.status_code, 200)

    r = requests.head(link+key)
    self.assertEqual(r.status_code,404)

  def test_deleteworks(self):
    key = "test"
    link = self.get_fresh_link()+'/'

    r = requests.put(link, data=f"{key}:value")
    self.assertEqual(r.status_code, 201)

    r = requests.delete(link+key)
    self.assertEqual(r.status_code, 200)

    r = requests.get(link+key)
    self.assertEqual(r.status_code, 404)

  def test_doubledelete(self):
    key = "test"
    link = self.get_fresh_link()+'/'

    r = requests.put(link, data=f"{key}:value")
    self.assertEqual(r.status_code, 201)

    r = requests.delete(link+key)
    self.assertEqual(r.status_code, 200)

    r = requests.delete(link+key)
    self.assertEqual(r.status_code, 500)

  def test_doubleputsame(self):
    key = "test"
    link = self.get_fresh_link()+'/'

    r = requests.put(link, data=f"{key}:value")
    self.assertEqual(r.status_code, 201)

    r = requests.put(link, data=f"{key}:value")
    self.assertEqual(r.status_code, 409)

  def test_doubleputdifferent(self):
    key1 = "test1"
    key2 = "test2"
    link = self.get_fresh_link()+'/'

    r = requests.put(link, data=f"{key1}:value")
    self.assertEqual(r.status_code, 201)

    r = requests.put(link, data=f"{key2}:value")
    self.assertEqual(r.status_code, 201)

  def test_deleteall(self):
    link = self.get_fresh_link()

    r = requests.delete(link)
    self.assertTrue(r.status_code == 200 or r.status_code == 204)
    
  def test_getall(self):
    key = "test"
    link = self.get_fresh_link()+'/'

    r = requests.put(link, data=f"{key}:value")
    self.assertTrue(r.status_code == 201 or r.status_code == 409)

    r = requests.get(link)
    self.assertEqual(r.status_code, 200)

  def test_10keys(self):
    print("0")
    keys = [ "test"+ str(i) for i in range(10)]
    link = self.get_fresh_link()+'/'

    for k in keys:
      r = requests.put(link, data=f"{k}:value")
      self.assertTrue(r.status_code == 201 or r.status_code == 409)

    for k in keys:
      r = requests.get(link+k)
      self.assertEqual(r.status_code, 200)
      self.assertEqual(r.text, "value")

    for k in keys:
      r = requests.delete(link+k)
      self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
  unittest.main()
