# Bike-Rental-Shop-Management-in-Python
Requirements for application are:
· On start of the application, input should be gathered to set up the bike shop and its inventory of each type of bike.
· Once bike shop is established; customers can then rent bikes.
· The application should be continuous throughout the day. Meaning, the application should always be running during each day.
· A “navigational selection” should be established to state “New Customer Rental” (1), “Rental Return” (2) “Show Inventory” (3) “End of Day (4)” or “Exit Program (5)”. Based on selection, do the following:
o If “New Customer”:
–Gather information on the customer (name and ID)
– Gather type of bike to rent
– Gather length of rental
– Gather amount of bikes
– Gather any discount coupons
– Determine if inventory meets needs
– Complete rental
o If “Rental Return”:
– Display Invoice with:
· Name of Customer
· Type and number of bikes rented
· Total time of rental
· Total before discount
· Discount (if applicable)
· Final total to be collected
– Return bikes to inventory
o If “Show Inventory”:
– Display inventory of:
· Mountain Bikes
· Touring Bikes
· Road Bikes
o If “End of Day”
– Display:
· Total of Bikes Rented for Day
· Daily Revenue Collected for Day based on rentals returned.
· Once 1, 2, 3, or 4 are complete, display “navigational selection” for next transaction.
· If 5 is selected, end program.
Updated Class Requirements (updates noted by highlight):
The Customer Can:
· Provide Name and ID Number (one per family or customer)
· See available bikes at the shop. · Rent a type of bike (mountain, road, touring)
· Rent bikes on hourly basis $5 per hours.
· Rent bikes on daily basis $20 per day.
· Rent bikes on weekly basis $60 per week.
· Family Rental, a promotion that can include from 3 to 5 rentals (of any type) with a discount of 25% of the total price.
· Provide a coupon with a coupon code that ends with “***BBP” to receive 10% off of total.
The Bike Rental Shop Can:
· Establishes initial inventory of each type of bike (mountain, road, touring)
· Issue a bill when customer decides to return the bike.
· Display available inventory of each type of bike.
· Takes requests on hourly, daily, and weekly basis by cross verifying stock. · Total Daily Bikes Rented. · Total Daily Revenue Collected.
For simplicity we assume that: · Any customer request rentals of only one type of bike (mountain, road, touring) for a specific amount of time (hourly, monthly, or weekly).
· Requested bikes should be less or equal to than available.
