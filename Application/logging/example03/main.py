import logging
import lib

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    lib.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()