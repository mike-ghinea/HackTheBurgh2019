import eventFunctions

eventFunctions.getEventsByFestival("fringe")

#eventFunctions.getEventsByGenre("events")


<<<<<<< HEAD
response = requests.get(url)
data = json.loads(response.text)
for x in data:
  try:
    pprint(eventObject(x))
    print ""
  except:
    print(eventObject(x))
=======
>>>>>>> 3898233e62ee8d1efa3dd3d07d0bb3f36022c321
