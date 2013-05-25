#!/usr/bin/env python
import re, string, uuid, datetime, sys



results = []
startpythonstuff = []

original_file = "test.ahkp"
new_file = "test.ahk"
function_file ="test_python_functions.ahk"
original_file_content = ""
comment_base = "; Python generated Anonymous Functions for Autohotkey."
import_string ="#include " + function_file + "\n"
if (len(sys.argv) > 1):
  original_file = sys.argv[1]
if ( original_file[-4:] == "ahkp"):
  new_file = original_file[:-1]
  function_file = original_file[:-5]+"_python_functions.ahk"
else:
  print "Please pass a file ending in ahkp!"
  exit()

def randomName():
  return re.sub(r'-', '', str(uuid.uuid4()))

def generateCommentLine():
  return comment_base + " Generated @\n" # + str(datetime.time(datetime.datetime.now())) + "\n"



main_pattern = r'\n[ ]*([^\n]*?)(anon)(\(.*?\){.*?})'
with open(original_file, "r") as original:
  regex = re.compile(main_pattern, re.MULTILINE | re.DOTALL)
  original_file_content = original.read()
  results2 = regex.findall(original_file_content)
  for result in results2:
    if (result[0][0] != ";"):
      results.append(result)
  new_content = original_file_content
  function_mapping = []
  for result in results:
    function_mapping.append((randomName(), result) )
    new_content = new_content.replace(result[1]+result[2],"\""+function_mapping[-1][0]+"\"",1)

  print function_mapping
  with open(new_file, "w") as text:
    text.write(new_content)
    text.write("\n"+import_string+"\n")

  with open(function_file, "w") as myfile:
    myfile.write(generateCommentLine())
    for function in function_mapping:
      func = function[0] + function[1][2]
      myfile.write(string.join(func, "")+"\n")



print results




