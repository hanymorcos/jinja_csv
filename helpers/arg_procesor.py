import argparse
import logging


def arg_required(arg):
   if arg is None : 
      logging.warning("can't find " + arg)
      exit

def get_arguments(): 
        parser = argparse.ArgumentParser("jinja_swagger")
        parser.add_argument("-a","--api_name", help="Enter API Name (i.e: Navy USM Current Occupation)")
        parser.add_argument("-c","--csv", help="api.csv is the default to overwrite us")
        parser.add_argument("-mo","--main_object", help="The main object name not returned in the JSON ")
        parser.add_argument("-t","--type", help="type array or object")
        parser.add_argument("-s","--select_by", help="Select by ID ")
        parser.add_argument("-ns","--nested_object", help="Object Name in the JSON")
        parser.add_argument("-d","--debug", help= "show debug information")
        args = parser.parse_args()


        if args.debug is not None:
                logging.Logger.setLevel(logging.DEBUG)

        arg_required(args.csv) 
        arg_required(args.api_name)
        arg_required(args.select_by) 
        arg_required(args.nested_object)

        return args