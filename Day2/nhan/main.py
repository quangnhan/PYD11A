thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "name": "Nathan"
}
# x = thisdict["name"]
x = thisdict.get("name", "No name")

print(x)