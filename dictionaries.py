dictionaryStudent = {"studentsname":"joshua","studentsclass":"200level" , "studentsdept": "science" }
print(dictionaryStudent["studentsname"])
for x in dictionaryStudent:
    print(dictionaryStudent[x])
dictionaryStudent.update({"studentsname": "michael"})  
print(dictionaryStudent["studentsname"])
   