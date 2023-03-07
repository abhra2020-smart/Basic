from basic.runner import Runner
from basic.errors import FunctionRecursionError

while True:
	try:
		text = input('> ')
		if text.strip() == "": continue
		result, error = Runner.run('<stdin>', text)

		if error:
			print(error.as_string())
		elif result:
			if len(result.elements) <= 1:
				print(repr(result.elements[0]))
			else:
				print(repr(result))
	except KeyboardInterrupt:
		exit(0)
	except RecursionError:
		error = FunctionRecursionError()
		print(error.as_string())
	except Exception as error:
		print(f'The interpreter crashed. Please start an issue on the GitHub page (https://github.com/abhra2020-smart/Basic) and provide the\nnecessary code files and the following error message: \n\033[31m{error}\033[0m')
		exit(1)