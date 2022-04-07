# verloop assignment

# libraries used
rest_framework <br>
django<br>
requests<br>
json<br>

link to google geolocation api documentation: https://developers.google.com/maps/documentation/geocoding/start

# API request format:
```
{
  "address": "3582,13 G Main Road, 4th Cross Rd, Indiranagar, Bengaluru, Karnataka 560008",
  "output_format": "json"
}
```


# Sample API response

## json
```
{
  "coordinates": {
    "lat": 7.888888,
    "lng": 56.23423
  },
  "address": "3582,13 G Main Road, 4th Cross Rd, Indiranagar, Bengaluru, Karnataka 560008"
}
```

## xml
```
<?xml version="1.0" encoding="UTF-8"?>
<root>
  <address># 3582,13 G Main Road, 4th Cross Rd, Indiranagar, Bengaluru,Karnataka 560008</address>
  <coordinates>
    <lat>7.888888</lat>
    <lng>56.23423</lng>
  </coordinates>
</root>
```
