from custom_methods.temperature_methods import Analisys
from argparse import ArgumentParser
from sys import stderr


def main(args=None):
	if not args:
		parser = ArgumentParser()
		parser.add_argument(
			'OPTION', help='Option to use', choices=dir(Analisys)[27:])
		parser.add_argument('FILE', help='csv file')
		parser.add_argument(
			'-a', help='You can use "help" here to check how a option works', dest='ARG', default=None)
		args = vars(parser.parse_args())
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
			for result in results:
				print(result)
		except TypeError:
			print(results)
	except Exception as e:
		if type(e) == TypeError:
			stderr.write(f"\"{args['OPTION']}\" is not a valid option\n")
		elif type(e) == KeyError:
			stderr.write(f"\"{args['ARG']}\" apparently not in the data set\n")


if __name__ == '__main__':
	main()
