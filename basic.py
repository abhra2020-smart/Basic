import argparse

from basic.runner import Runner

parser = argparse.ArgumentParser(
    prog='BASIC',
    description='This will run a BASIC file'
)

parser.add_argument('filename')

args = parser.parse_args()
result, error = Runner.run(f'{args.filename}', f'RUN({args.filename})')

if error:
		print(error.as_string())
	elif result:
		if len(result.elements) <= 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
