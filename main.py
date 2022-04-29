#    Copyright (C) 2022 IdotMaster1
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


from apirequests import *

print("All credit goes to MangaDex (https://mangadex.org)")
name = input('Search any manga author on MangaDex: ')

print("The author of " + name + " is:")
author(name)

wantid = input("Do you want " + name + "'s ID? ")
if wantid == ('y'):
    getid(name)
else:
    print('ratio bozo')
    getid(name)