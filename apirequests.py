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


import json
import requests

def author(querry):
    endpoint = requests.get('https://api.mangadex.org/manga?title=' + querry)
    json = endpoint.json()
    endpointid = requests.get('https://api.mangadex.org/author/' + json['data'][0]['relationships'][0]['id'])
    ihatethis = endpointid.json()
    print(ihatethis['data']['attributes']['name'])

def getid(querry):
    endpoint = requests.get('https://api.mangadex.org/manga?title=' + querry)
    json = endpoint.json()
    print(json['data'][0]['id'])
