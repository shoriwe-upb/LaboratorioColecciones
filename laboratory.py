from custom_functions.temperature_methods import Analisys
from argparse import ArgumentParser
from sys import stderr


# Variable to store the results when the user make tests
local_results = []

def __other_print(value):
	if type(value) != tuple:
		value = tuple(value)
	local_results.append(value)

def main(args=None):
	local_args = False
	if not args:
		parser = ArgumentParser()
		parser.add_argument(
			'OPTION', help='Option to use', choices=dir(Analisys)[27:])
		parser.add_argument('FILE', help='csv file')
		parser.add_argument(
			'-a', help='You can use "help" here to check how a option works', dest='ARG', default=None)
		args = vars(parser.parse_args())
		print_func = print
		print_error = stderr.write
	else:
		print_func = __other_print
		print_error = lambda value: local_results.append(value)
		local_args = True
	file = open(args['FILE'])
	lines = file.readlines()
	file.close()

	data = {}
	for line in lines:
		department, values = line.strip().split(',')
		data[department] = tuple(map(lambda value: float(value), values.split(';')))

	setup_ = Analisys(data)
	try:
		function_ = getattr(setup_, args['OPTION'])
		results = function_(args['ARG'])
		try:
			if type(results) == str:
				raise TypeError
			if not local_args:
				for result in results:
					print_func(result)
			else:
				print_func(results)
		except TypeError:
			print_func(results)
	except Exception as e:
		if type(e) == TypeError:
			print_error("\033[1;31m" + f"\"{args['OPTION']}\" is not a valid option\n" + "\033[0;0m")
		elif type(e) == KeyError:
			print_error("\033[1;31m" + f"\"{args['ARG']}\" apparently not in the data set\n" + "\033[0;0m")


if __name__ == '__main__':
	main()
