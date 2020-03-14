from enum import Enum
import pathlib

from models import NearEarthObject


PROJECT_ROOT = pathlib.Path(__file__).parent.absolute()


class OutputFormat(Enum):
    """
    Enum representing supported output formatting options for search results.
    """
    display = 'display'
    csv_file = 'csv_file'

    @staticmethod
    def list():
        """
        :return: list of string representations of OutputFormat enums
        """
        return list(map(lambda output: output.value, OutputFormat))


class NEOWriter(object):
    """
    Python object use to write the results from supported output formatting options.
    """

    def __init__(self):
        # TODO: How can we use the OutputFormat in the NEOWriter?
        pass

    def write(self, format, data, **kwargs):
        """
        Generic write interface that, depending on the OutputFormat selected calls the
        appropriate instance write function

        :param format: str representing the OutputFormat
        :param data: collection of NearEarthObject or OrbitPath results
        :param kwargs: Additional attributes used for formatting output e.g. filename
        :return: bool representing if write successful or not
        """
        # TODO: Using the OutputFormat, how can we organize our 'write' logic for output to stdout vs to csvfile
        # TODO: into instance methods for NEOWriter? Write instance methods that write() can call to do the necessary
        # TODO: output format.

        # Write to screen
        if format == OutputFormat.display.value:
            print(NearEarthObject.get_csv_header())
            for datum in data:
                print(datum)
        # Write to CSV file
        elif format == OutputFormat.csv_file.value:
            filename = f'{PROJECT_ROOT}/data/neo_neo_data.csv'
            with open(filename, 'w') as f:
                f.writelines(NearEarthObject.get_csv_header() + '\n')
                for datum in data:
                    f.writelines(datum.__repr__() + '\n')
        else:
            return False

        return True
