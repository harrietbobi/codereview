class Events():
    """ A class to handle actions related to events"""

    def __init__(self, title, location, category, description):
        """define an empty list to hold all the event objects"""
        self.title = title
        self.location = location
        self.category = category
        self.description = description
        self.event_list = []

    def existing_event(self, title, location, category, description):
        """A method to check if a user already has that event in same location"""
        for event in self.event_list:
            # test to see if the user has the same event, in the same location in their list
            if event['title'] == title and event['location'] == location and event['category'] == category and event['description'] == description:
                return True
            else:
                return False

    def create(self, title, location, category, description):
        """A method for creating a new event"""
    
        if self.existing_event(title, location, category, description):
            return False
        else:
            self.event_list.append(title)
            self.event_list.append(location)
            self.event_list.append(category)
            self.event_list.append(description)
            return True
