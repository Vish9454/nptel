person={"name":"Vishal",
        "age":26,
        "sch":"holy cross"}
try:
    print("Name is {name} and age is {age} and school name is {sch} and job is {job}".format(**person))

except KeyError as e:
    print(f"missing key as {e}")

