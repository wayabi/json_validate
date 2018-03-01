
#pip install genson
import os
import sys
import json
from genson import SchemaBuilder

def load_jsons(path):
	jj = []
	if os.path.isdir(path):
		files = os.listdir(path)
		for f in files:
			j = json.load(open("%s/%s" % (path, f)))
			jj.append(j)
			
	else:
		j = json.load(open(path))
		jj.append(j)
	return jj

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("args <path_json_or_dir>")
		exit()
	path = sys.argv[1]

	builder = SchemaBuilder()
	builder.add_schema({"type": "object", "properties": {}})
	jj = load_jsons(path)
	for j in jj:
		#print(jj)
		builder.add_object(j)

	#print(builder.to_schema())
	print(builder.to_json(indent=2))
