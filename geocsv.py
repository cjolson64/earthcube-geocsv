import re

class geocsv(object):

   def __init__(self, geocsvFilename):

      self.geocsvFile = open(geocsvFilename, 'r')
      self.keys = dict()
      self.fieldLine = ''
      self.delimiter = ','
      self.numberColumns = 0

   def __del__(self):

      self.geocsvFile.close()


   name = 'I created the class'

   knownKeys = [
         'fields',
         'field_unit',
         'field_type',
         'field_name_long',
         'field_standard_name',
         'field_missing',
         'delimiter',
         'attribution',
         'standard_name_cv'
   ]

   allowedTypes = [
         'string',
         'integer',
         'float',
         'datetime'
   ]

   # Public functions

   def validate(self):

      # run through all of the checks

      self._parseHeader()

      #self._checkData()

      return True

   def _parseHeader(self):

      # Extract all the info up until the field line
        
      for line in self.geocsvFile:
         if re.match("^#", line):
            # Keyword declarations
            pair = line.strip("# \r\n").split(":", maxsplit=1)
            self.keys.update({pair[0].strip(): pair[1].strip()})

         else:
            # Fields line
            self.fieldLine = line.strip()
            break

      # Set the delimiter if necessary

      if self.keys['delimiter'] is not None:
         self.delimiter = self.keys['delimiter']

      # Set the number of data columns

      #self.numberColumns = re.split(self.delimiter, self.fieldLine)
      #self.numberColumns = self.fieldLine.split("\t")
      self.numberColumns = self.fieldLine.split(self.delimiter)
      print(self.fieldLine)
      print(self.delimiter)
      print(self.numberColumns)


   def _checkData(self):

      i = 0
      for line in self.geocsvFile:
         if re.match("^#", line):
            continue
         
         else:
            # Data line
            i += 1
            dataEntry = line.strip().split(self.delimiter)


      print(i)


#   def printFieldInfo():
#
#      # display info about the fields
#
#   def printColumns(fieldArray):
#
#      # Extract data dolumns specified in fieldArray (index or name)
#
#   # Checks to perform
#
#   def checkRequiredHeaders:
#
#      # currently only the 'fields'
#
#   def checkNumberColumns:
#
#      # check relevant header lines, column title line, and each data line for the same number of columns according to delimiter
#
#   def checkCharset:
#
#      # make sure everything is UTF-8
#      # (not even sure if this can be done - may just be indicated by other failures...)
#
#   def checkDates:
#
#      # fields of type ‘datetime’ must be in an ISO 8601 format.
#
#   def checkTypes:
#
#      # check known types for consistency
#
#   def setDelimiter:
#
#      # default delimiter is a comma
#
#   def setFieldMissing:
#
#      # no default values
#
#   def setRowStructure:
#
#      # uses field names and field types to create structure for data entry


      # POSIX regular expression to look for header key-value pairs:
      #re = "^#\s*(keyword)\s*:(value)[\r\n]+"


