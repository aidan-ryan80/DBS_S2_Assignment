### Listing Functional Dependencies for our DB:

##### Hotel Table:
1. hotelID -> address, name

##### Customers Table:
1. customerID -> email, phoneNumber, name, age, address

##### PaymentInfos Table:
1. id -> customerID, billingAddress, cardHolderName, expirationDate, cardIssuer, cardNumber

##### Rooms Table:
1. roomNumber -> price, type, availability, floor

##### skiResorts Table:
1. resortID -> name, size, location, difficultyLevel, skiLiftsCount, slopesCount, businessHours

##### skiPasses Table:
1. skiPassID -> resortID, passType, price

##### Packages Table:
1. packageID -> skiPassID, name, description, price, roomID

##### Transports Table:
1. transportID -> resortID, type, price, timetable

##### PackagesTransports Table:
1. (packageID, transportID) -> packageID, transportID

##### Reservations Table:
1. reservationID -> hotelID, customerID, packageID, roomID, status, paymentStatus, checkInDate, checkOutDate, totalCost