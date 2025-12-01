# countries-soap
Python script to extract countries from a SOAP API

## Description
This project is a Python script that extracts country data from the following SOAP API: http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL . The script extracts country names and ISO codes and replaces '&' with 'and' in the names of countries. The script then asks the user for input to authenticate with a MySQL database and to determine the location where the data will be stored. The user is also asked to input a preference for sorting - sorting based on the ISO codes or based on the country names. Finally, the user input is used to show the first 10 countries in alphabetical order.

## Requirements
The user needs to have a MYSQL database where the data can be stored.