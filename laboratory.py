from custom_functions.temperature_methods import Analisys, load_data_from_file
from argparse import ArgumentParser
from sys import stderr


def main():
	parser = ArgumentParser()
	parser.add_argument(
		'OPTION', help='Option to use', choices=['department_med', 'med_of_most_hot_month_of_departments',
												 'most_hot', 'most_hot_med', 'most_hot_month_of_year', 'national_med',
												 'standard_deviation'])
	parser.add_argument('FILE', help='csv file')
	parser.add_argument(
		'-a', help='You can use "help" here to check how a option works', dest='ARG', default=None)
	args = vars(parser.parse_args())

	data = load_data_from_file(args["FILE"])

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
			stderr.write("\033[1;31m" + f"\"{args['OPTION']}\" is not a valid option\n" + "\033[0;0m")
		elif type(e) == KeyError:
			stderr.write("\033[1;31m" + f"\"{args['ARG']}\" apparently not in the data set\n" + "\033[0;0m")


if __name__ == '__main__':
	main()
