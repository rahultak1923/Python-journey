marks = { 
    "rahul": 100,
    "kaalu": 32,
    "chaalu":32
}

print(marks, type(marks))
print(marks["rahul"])
print(marks.items())
print(marks.values())
print(marks.keys())

marks.update({"chaalu":34, "maanu":97})
print(marks)

print(marks.get("maanu")) # this name is worng then is show none but
print(marks["maanu"]) # this name is worng then is show returns an error 