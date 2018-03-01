
#pip install jsonschema
import os
import sys
import json
from jsonschema import validate
import jsonschema

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("args <json> <schema>")
		exit()
	jpath = sys.argv[1]
	spath = sys.argv[2]

	j = json.load(open(jpath))
	s = json.load(open(spath))

	try:
		validate(j, s)
		print("ok")
	except jsonschema.exceptions.ValidationError as e:
		print(e)
