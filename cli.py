import argparse
from main_app import main_app
from user_registration import register_user
from fetchequestions import give_user_question
from messages import message_log
from user_login import login_user


def main():
    # create argument parser object
    parser = argparse.ArgumentParser(description='RandAlgo_py')

    parser.add_argument('-q', '--query', type=str, nargs=1,
                        metavar = None, default = None, help = None)

    # parse the arguments from standard input
    args = parser.parse_args()

    RandAlgo_py = main_app()


if __name__ == '__main__':
    main_app()
