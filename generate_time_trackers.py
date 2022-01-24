#!/usr/bin/env python

import sys, argparse, logging, os
from textwrap import dedent

from datetime import date, timedelta

def all_fridays(year):
    fridays = []
    d = date(year, 1, 1)                    # January 1st
    while d.year == year:
        d += timedelta(days = 4 - d.weekday())  # First friday
        fridays.append(d)
        d += timedelta(days = 7)
    return fridays

def get_previous_saturday(date_in):
    start_date = date_in - timedelta(1)
    for previous_day in (start_date - timedelta(n) for n in range(7)):
        if previous_day.weekday() == 5:
            return previous_day

def get_weeks_worth_of_dates(start_date):
    dates = []
    for day in (start_date + timedelta(n) for n in range(7)):
        dates.append(day)
    return dates

#for d in all_fridays(2019):
#   print(d.strftime('%a %b %d'))


# Gather our code in a main() function
def main(year, loglevel):
      logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
      print(args)

      for a_friday in all_fridays(args.year):

            output_dir = "./output"
            if not os.path.exists(output_dir):
              os.mkdir(output_dir)

            f = open(a_friday.strftime('output/%Y-%m-%d_time.txt'), "w+")

            f.write("calendar jira gitlab slack email\n\n\n\n")

            for day in get_weeks_worth_of_dates(get_previous_saturday(a_friday)):
              f.write("################### " + day.strftime('%A %b %d') + "\n\n\n\n")

            week_data_string = a_friday.strftime('%m/%d')
            f.write(

                dedent(f"""\
                    --------------------------------------------------------------------------------
                    
                    PI
                    
                    ||Week||Category||Tasks||Hours||
                    ||{week_data_string}||PI| | |
                    || ||Test| | |
                    || ||Mura Upgrade| | |
                    
                    A
                    
                    ||Week||Tasks||
                    ||{week_data_string}| |
                    
                    B
                    
                    ||Week||Tasks||
                    ||{week_data_string}| |
                    
                    C
                    
                    ||Week||Tasks||
                    ||{week_data_string}| |
                    
                    D
                    
                    ||Week||Tasks||
                    ||{week_data_string}| |
            
                """)
            )
 
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = "Does a thing to some stuff.",
        epilog = "As an alternative to the commandline, params can be placed in a file, one per line, and specified on the commandline like '%(prog)s @params.conf'.",
        fromfile_prefix_chars = '@' )
    # TODO Specify your real parameters here.
    parser.add_argument(
                      "--year",
                      type = int,
                      help = "year to generate")
    parser.add_argument(
                      "-v",
                      "--verbose",
                      help="increase output verbosity",
                      action="store_true")
    args = parser.parse_args()

    # Setup logging
    if args.verbose:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO

    main(args.year, loglevel)