import argparse
from basic.runner import Runner

parser = argparse.ArgumentParser(
    prog='BASIC',
    description='This will run a BASIC file'
)

parser.add_argument('filename')

args = parser.parse_args()
with open(args.filename, 'r') as f:
	result, error = Runner.run(args.filename, f.read())

if error:
		print(error.as_string())
elif result:
	if len(result.elements) <= 1:
		print(repr(result.elements[0]))
	else:
		print(repr(result))
