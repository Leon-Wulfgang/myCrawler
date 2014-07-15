import sys
print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8')


from ghost import Ghost
ghost = Ghost()

# Opens the web page
#page, resources = ghost.open('http://www.openstreetmap.org/')
page, resources = ghost.open('http://www.openstreetmap.org/search?query=france#map=5/49.539/-11.162')
# Waits for form search field
#ghost.wait_for_selector('input[name=query]')
pageC = ghost.content

fp = open("testwhForm00.txt",'w')
fp.write(pageC)
fp.close()


# Fills the form
#ghost.fill("#search_form", {'query': 'France'})
# Submits the form
#ghost.fire_on("#search_form", "submit")
# Waits for results (an XHR has been called here)
#ghost.wait_for_selector(
#    '#search_osm_nominatim .search_results_entry a')
# Clicks first result link
#ghost.click(
#    '#search_osm_nominatim .search_results_entry:first-child a')
# Checks if map has moved to expected latitude
#lat, resources = ghost.evaluate("map.center.lat")
#assert float(lat.toString()) == 5860090.806537
