#
# VSCP (Very Simple Control Protocol)
# http://www.vscp.org
#
# The MIT License (MIT)
#
# Copyright (c) 2000-2019 Ake Hedman, Grodans Paradis AB <info@grodansparadis.com>
#
# Generate the vscp.constants.classes object for
#  "https://github.com/grodansparadis/node-vscp-class"
#

import sys
import glob
# https://docs.python.org/3/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET
import time
import datetime

xclass = {}
order_list = [] # class list order
class_list = [] # List with class attributes
type_list = []  # List with type attributes

# Read classes list to get list order
class_tree = ET.parse('../classes/list_class.xml')
class_root = class_tree.getroot()
for child in class_root.iter('item'):
    order_list.append( child.attrib['name'] )

if len(order_list) == 0:
    print("No classes defined in class list!")
    sys.exit()

# Get copyright header
with open('../javascript/prefix_class.txt', 'r') as myfile:
    data = myfile.read()
print(data)

print("/*")
print("            !!!!!!!!!!!!!!!!!!!!  W A R N I N G  !!!!!!!!!!!!!!!!!!!!")
print("                           This file is auto-generated")
print("                see https://github.com/grodansparadis/vscp-classes")
print("                        Generated:", datetime.datetime.now() )
print("*/\n\nvar exports = module.exports = {};\n")

for index, vscp_class in enumerate(order_list):
    fname = '../classes/' + vscp_class
    type_tree = ET.parse(fname)
    type_root = type_tree.getroot()
    #print "type root tag",type_root.tag
    outstr =  type_root.attrib["token"] + " = " + \
                type_root.attrib["id"] + ";"
    outstr = outstr.replace(".","_")
    outstr = "module.exports.VSCP_" + outstr;
    print(outstr)

print("\n")