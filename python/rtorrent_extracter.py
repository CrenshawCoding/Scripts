import os, sys
extractable_endings = ['.rar', '.zip']
extractable = None
if not sys.argv[1]:
    quit()
for file in os.listdir(sys.argv[1]):
	for ending in extractable_endings:
		if file.endswith(ending):
			extractable = file
if extractable:
	os.system('7z e -oc {1} {2}'.format(sys.argv[1], extractable))