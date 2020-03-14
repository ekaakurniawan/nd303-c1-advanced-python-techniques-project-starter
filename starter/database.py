import csv
from models import OrbitPath, NearEarthObject


class NEODatabase(object):
    """
    Object to hold Near Earth Objects and their orbits.

    To support optimized date searching, a dict mapping of all orbit date paths to the Near Earth Objects
    recorded on a given day is maintained. Additionally, all unique instances of a Near Earth Object
    are contained in a dict mapping the Near Earth Object name to the NearEarthObject instance.
    """

    def __init__(self, filename):
        """
        :param filename: str representing the pathway of the filename containing the Near Earth Object data
        """
        # TODO: What data structures will be needed to store the NearEarthObjects and OrbitPaths?
        # TODO: Add relevant instance variables for this.

        self.filename = filename
        self.neo_orbit_paths_date_to_neo = {}
        self.neo_name_to_instance = {}

    def load_data(self, filename=None):
        """
        Loads data from a .csv file, instantiating Near Earth Objects and their OrbitPaths by:
           - Storing a dict of orbit date to list of NearEarthObject instances
           - Storing a dict of the Near Earth Object name to the single instance of NearEarthObject

        :param filename: str representing the pathway of the filename containing the Near Earth Object data
        :return: None
        """
        # TODO: Load data from csv file.
        # TODO: Where will the data be stored?

        if not (filename or self.filename):
            raise Exception('Cannot load data, no filename provided')

        filename = filename or self.filename

        # Load data from csv file
        with open(filename) as csvfile:
            neo_orbit_paths = csv.DictReader(csvfile)
            for neo_orbit_path in neo_orbit_paths:
                # Instantiate new Near Earth Object if not already exist
                if neo_orbit_path['name'] in self.neo_name_to_instance:
                    neo = self.neo_name_to_instance[neo_orbit_path['name']]
                else:
                    neo = NearEarthObject(**neo_orbit_path)
                    self.neo_name_to_instance[neo_orbit_path['name']] = neo

                # Instantiate new orbit path
                orbit = OrbitPath(neo.name, **neo_orbit_path)
                if neo_orbit_path['close_approach_date'] in self.neo_orbit_paths_date_to_neo:
                    self.neo_orbit_paths_date_to_neo[neo_orbit_path['close_approach_date']].append(neo)
                else:
                    self.neo_orbit_paths_date_to_neo[neo_orbit_path['close_approach_date']] = [neo]

                # Add an orbit path information to a Near Earth Object list of orbits
                neo.update_orbits(orbit)

        return None
