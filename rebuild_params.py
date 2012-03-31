#! /usr/bin/env python
#
#  Purpose: read a file
#
#  $Id: rebuild.py,v 1.2 2003/10/11 08:10:11 zyx Exp $
#
#---------------------------------------------------------------------

import os
import sys
import getopt

#---------------------------------------------------------------------

__version__ = "1.0.0"

debugFlg    = 0
verboseFlg  = 0
filename    = "file.txt"

#=====================================================================

class Parameter:
   Name       = None

   def __init__(self, name):
      self.Name     = name

   def __str__(self):
      str = "Name: %s " % \
          (self.Name, )
      return str

   def write(self, fd):
      print >>fd, "#"
      print >>fd, self.Definition

      try :
         print >>fd, self.Type
      except:
         pass

      try :
         print >>fd, self.Table
      except:
         pass

      try :
         print >>fd, self.ColumnName
      except:
         pass

      try :
         print >>fd, self.GenerateNewVal
      except:
         pass

      try :
         print >>fd, self.TableLocation
      except:
         pass

      try :
         print >>fd, self.MaxValue
      except:
         pass
      try :
         print >>fd, self.MinValue
      except:
         pass

      try :
         print >>fd, self.OriginalValue
      except:
         pass

      try :
         print >>fd, self.Format
      except:
         pass

      try :
         print >>fd, self.StartRow
      except:
         pass

      try :
         print >>fd, self.Delimiter
      except:
         pass

      try :
         print >>fd, self.ParamName
      except:
         pass

      try :
         print >>fd, self.SelectNextRow
      except:
         pass

#=====================================================================

def rebuild(filename):
   infile  = filename + ".prm"
   outfile = filename + ".txt"

   try:
      ifd = open(infile, 'r')
   except IOError, msg:
      sys.stderr.write(infile + ': cannot open: ' + `msg` + '\n')
      return 1

   try:
      ofd = open(outfile, 'w')
   except IOError, msg:
      sys.stderr.write(outfile + ': cannot open: ' + `msg` + '\n')
      return 2

   lineno     = 0
   parameters = {}
   parameter  = None

   while 1:
      line = ifd.readline()

      if not line:
         break

      lineno += 1

      line = line[:-1]
      line = line.replace('\r','')

      if len(line) == 0:
         continue

      if line.find("#") == 0:
         continue

      if line.find("[") == 0:
         name = line.split(':', 1)
         name = name[1]
         name = name.replace(']','')
     
         print name

         parameter            = Parameter(name)

         parameter.Definition = line

         parameters[name]     = parameter

         continue

      if parameter != None:
         if line.find("ColumnName=") == 0:
            parameter.ColumnName = line
         elif line.find("Table=") == 0:
            parameter.Table = line
         elif line.find("Type=") == 0:
            parameter.Type = line
         elif line.find("GenerateNewVal=") == 0:
            parameter.GenerateNewVal = line
         elif line.find("TableLocation=") == 0:
            parameter.TableLocation = line
         elif line.find("OriginalValue=") == 0:
            parameter.OriginalValue = line
         elif line.find("StartRow=") == 0:
            parameter.StartRow = line
         elif line.find("Delimiter=") == 0:
            parameter.Delimiter = line
         elif line.find("ParamName=") == 0:
            parameter.ParamName = line
         elif line.find("SelectNextRow=") == 0:
            parameter.SelectNextRow = line
         elif line.find("MaxValue=") == 0:
            parameter.MaxValue = line
         elif line.find("MinValue=") == 0:
            parameter.MinValue = line
         elif line.find("Format=") == 0:
            parameter.Format = line
         else:
            print ">>> %s" % line

   print "Processed %d lines" % lineno

   keys = parameters.keys()

   keys.sort()

   # print keys

   for idx in range(len(keys)):
      parameter = parameters[keys[idx]]
      parameter.write(ofd)

   ifd.close()
   ofd.close()

#---------------------------------------------------------------------

def main():
   global debugFlg
   global verboseFlg

   try:
      opts, args = getopt.getopt(sys.argv[1:], "dvV?")
   except getopt.error, msg:
      print __doc__
      return 1

   for o, a in opts:
      if o == '-d':
         debugFlg = 1
      elif o == '-v':
         verboseFlg = 1
      elif o == '-V':
         print "Version: %s" % __version__
         return 1
      elif o == '-?':
         print __doc__
         return 1

   if (debugFlg):
      print ">> Flg    %s" % debugFlg

   if args:
      for arg in args:
         print arg
   else:
      pass

   wrk = os.getcwd()

   name = os.path.basename(wrk)

   rebuild(name)

#---------------------------------------------------------------------

if __name__ == '__main__' or __name__ == sys.argv[0]:
   sys.exit(main())

#---------------------------------------------------------------------

"""
Revision History:

     Date     Who   Description
   --------   ---   --------------------------------------------------
   20030920   plh   Initial implementation
   20031002   plh   Cleaned up args in main().  Added '-h', '-?', '-V'

Problems to fix:

To Do:

Issues:

"""


