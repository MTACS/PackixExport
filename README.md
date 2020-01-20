# PackixExport

A little script to export Packix transactions.

## How to export
This could probably be done in a more elegant way using the API endpoint, but Packix uses cookies so the easiest way was to let the browser handle that to export the data.

1. Login into Packix.
2. Open the network tab in the browser's developer tools.
3. Go to your package you want to export purchases from.
4. Go into the `transactions` call the browser made to Packix.
5. Copy the URL and open it in a new tab. Copy it all and save it to a file somwehere.
6. Run `PackixExport.py <inputfile>`

Repeat steps 3-6 for every package of interest.
