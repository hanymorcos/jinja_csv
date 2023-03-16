from helpers.arg_procesor import get_arguments
from helpers.csv_reader import read_csv
from helpers.Template import Template
from helpers.generate_jinja import produce_report
import logging

def main(): 
    args = get_arguments()
    logging.debug(args)

    table = read_csv(args.csv)
    logging.debug(table)

    data_package = Template(args.nested_object, args.select_by, args.api_name, table)
    output = produce_report(data_package)
    print(output)

if __name__ == "__main__":
    main()