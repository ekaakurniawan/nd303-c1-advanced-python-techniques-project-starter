class NearEarthObject(object):
    """
    Object containing data describing a Near Earth Object and it's orbits.

    # TODO: You may be adding instance methods to NearEarthObject to help you implement search and output data.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs:    dict of attributes about a given Near Earth Object, only a subset of attributes used
        """
        # TODO: What instance variables will be useful for storing on the Near Earth Object?
        self.id = kwargs['id']
        self.neo_reference_id = kwargs['neo_reference_id']
        self.name = kwargs['name']
        self.nasa_jpl_url = kwargs['nasa_jpl_url']
        self.absolute_magnitude_h = float(kwargs['absolute_magnitude_h'])
        self.estimated_diameter_min_kilometers = float(kwargs['estimated_diameter_min_kilometers'])
        self.estimated_diameter_max_kilometers = float(kwargs['estimated_diameter_max_kilometers'])
        self.estimated_diameter_min_meters = float(kwargs['estimated_diameter_min_meters'])
        self.estimated_diameter_max_meters = float(kwargs['estimated_diameter_max_meters'])
        self.estimated_diameter_min_miles = float(kwargs['estimated_diameter_min_miles'])
        self.estimated_diameter_max_miles = float(kwargs['estimated_diameter_max_miles'])
        try:
            self.estimated_diameter_min_feet = float(kwargs['estimated_diameter_min_feet'])
        except:
            self.estimated_diameter_min_feet = None
        self.estimated_diameter_max_feet = float(kwargs['estimated_diameter_max_feet'])
        self.is_potentially_hazardous_asteroid = (kwargs['is_potentially_hazardous_asteroid'] == 'True')
        self.__orbits = []

    @staticmethod
    def diameter(neo):
        return neo.estimated_diameter_min_kilometers

    @property
    def diameter_min_km(self):
        return self.estimated_diameter_min_kilometers

    @staticmethod
    def is_hazardous(neo):
        return neo.is_potentially_hazardous_asteroid

    @property
    def orbits(self):
        return self.__orbits

    def update_orbits(self, orbit):
        """
        Adds an orbit path information to a Near Earth Object list of orbits

        :param orbit: OrbitPath
        :return: None
        """
        # TODO: How do we connect orbits back to the Near Earth Object?
        self.__orbits.append(orbit)

    def __repr__(self):
        return self.name


class OrbitPath(object):
    """
    Object containing data describing a Near Earth Object orbit.

    # TODO: You may be adding instance methods to OrbitPath to help you implement search and output data.
    """

    def __init__(self, neo_name, **kwargs):
        """
        :param kwargs:    dict of attributes about a given orbit, only a subset of attributes used
        """
        # TODO: What instance variables will be useful for storing on the Near Earth Object?
        self.neo_name = neo_name
        self.kilometers_per_second = float(kwargs['kilometers_per_second'])
        self.kilometers_per_hour = float(kwargs['kilometers_per_hour'])
        self.miles_per_hour = float(kwargs['miles_per_hour'])
        self.close_approach_date = kwargs['close_approach_date']
        self.close_approach_date_full = kwargs['close_approach_date_full'] 
        self.miss_distance_astronomical = float(kwargs['miss_distance_astronomical'])
        self.miss_distance_lunar = float(kwargs['miss_distance_lunar'])
        self.miss_distance_kilometers = float(kwargs['miss_distance_kilometers'])
        self.miss_distance_miles = float(kwargs['miss_distance_miles'])
        self.orbiting_body = kwargs['orbiting_body']

    @staticmethod
    def distance(path):
        return path.miss_distance_kilometers

    def __repr__(self):
        return self.close_approach_date
