students = {
        "Alice":["ID0001",26,"A"],
        "Bob":["ID0002",27,"B"],
        "Chris":["ID0003",19,"C"],
        "David":["ID0004",23,"A"],
        "Elle":["ID0005",25,"B"]
        }

print(students["Chris"][0])
print(students["David"][1:])


students2 = {
        "Alice":{"id":"ID0001","age":26,"grade":"A"},
        "Bob":{"id":"ID0002","age":29,"grade":"B"},
        "Chris":{"id":"ID0003","age":19,"grade":"C"},
        "David":{"id":"ID0004","age":27,"grade":"B"},
        "Elle":{"id":"ID0005","age":23,"grade":"A"},
        }

print(students2["David"]["age"])
print(students2["Elle"]["id"], students2["Elle"]["grade"])
