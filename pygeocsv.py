import csv

class pygeocsv:

    def __init__(self, filename, debug=0):

        self.debug = debug
        self.delimiter = ',' #default

        if (self.debug):
            print("Opening file: " + filename)

        self.handle = fopen(filename, 'r')


    def __del__(self):

        if (self.debug):
            print("Closeing file at: " + self.handle)

        self.handle.close()


    def parse_header(self):

        if (self.debug):
            print("Parsing header lines.")

        # Loop through file until we get to the first line
        # that isn't a comment
        while (line = get_the_next_line):
            if (lastline):
                break

            elif (!regex('/^#/')):
                # First line of data
                # trim the #
                previous_line = previous_line[1:]
                break

            else:
                if (isset(previous_line)):
                    # previous line must be a key:value pair
                    # split on :
                    pairs = previous_line.split(':')
                    # add the two parts to a dictionary
                    dict_push(pairs[0], pairs[1])

                # strip the # and set this to previous_line
                previous_line = line[1:]

        # look to see if a different delimiter was specified
        if (isset(dictionary['delimiter']):
            self.delimiter = dictionary['delimiter']

        # now work with the header line
        # split on delimiter
        self.fields = previous_line.split(self.delimiter)
        self.field_count = len(fields)


        # now loop through the dict we just created
        foreach (key and value)

            if (len(value.split(self.delimiter)) == self.field_count):
                # these are field specific
            else:
                # one value per file$a


    def isvalid(self)
