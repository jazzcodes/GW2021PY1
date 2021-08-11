#  Argument Parsing

import argparse

log = {
    "date": "11 Aug 2021",
    "time": "11:27",
    "severity": "high",
    "message": "[DEVICE WORKING]: this is an initial log"
}


def write_log(file_name):
    log_to_write = "{date},{time},{severity},{message}\n".format_map(log)
    with open(file_name, "a") as file:
        file.write(log_to_write)
        print("Log Written...")


def read_logs(file_name):
    with open(file_name, "r") as file:
        for log_in_file in file.readlines():
            print(log_in_file, end="")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--operation", required=True, help="please give operation as read or write")
    ap.add_argument("-f", "--filename", required=True, help="please give filename eg logs.csv")

    result = ap.parse_args()
    print(result, type(result))

    args = vars(result)
    print(args, type(args))

    if args['operation'] == "write":
        write_log(file_name=args['filename'])
    else:
        read_logs(file_name=args['filename'])

if __name__ == '__main__':
    main()