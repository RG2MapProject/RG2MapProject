# RG2MapProject

Goals:
Create a multi-layered map of Lithuania, each layer containing markers of towns,
each of which display some information derived from RG2 when clicked on.

Contents of github:
maptest.html
    Takes .kml file from github (file must be on publicly available server) and
    displays map with all pins in place, along with window that displays name
    and description when a pin is clicked on. This code is mostly copied over
    from the google maps JavaScript API, and is only meant as a basic template
    of how the map could function in future.
README.md
    pretty self-explanatory
sample_layer_data.py
    Python code (I don't know any JavaScript) to fill KML with description
    information, described in summary of that file.
town_list.txt
    Data off of which above python code ran - condensed and copied from Series II
    of RG2, created using commented-out code also in sample_layer_data.py.
Towns.kml
    File encoding one layer of pins for all the towns present in the collection
    that can be overlayed onto google maps using HTML and JavaScript. Each pin
    contains town name, coordinates, and a description containing the number of
    entries in Series II of RG2 in which that town was listed. Each pin is also
    connected to an icon image at the top of the KML - different icon codes were
    originally different colored icons. (I was having trouble with icon display
    so now they're all just white, I believe.)


More information on Google Maps API/KML Files:
https://developers.google.com/kml/documentation/kml_tut
https://developers.google.com/maps/documentation/javascript/kmllayer

Next steps:
  Figure out the icons and description display
  Make a list of layers - potential options:
    Political
    Cultural
    Economic
    Photographic
    Religious
    Locations of Aid Organizations
    Town Age
  Investigate Omeka and see how the different layers of markers and descriptions
    can best be integrated into one webpage
  Determine what formatting descriptions should have
  Get desired information from collection
  Build webpage
