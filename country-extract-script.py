from zeep import Client
import mysql.connector

client = Client(
    "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
)
result = client.service.ListOfCountryNamesByCode()

for country in result:
    if "&" in country["sName"]:
        country["sName"] = country["sName"].replace("&", "and")
    else:
        continue

while True:
    username = input("Enter your database username: ")
    password = input("Enter your database password: ")
    userdb = input("Enter database name: ")
    tablename = input("Enter table name (warning if tablename exists it will be dropped): ")
    try:
        mydb = mysql.connector.connect(
            host="localhost", user=username, password=password, database=userdb
        )
        print("Connected succesfully")
        break
    except mysql.connector.Error as e:
        print(f"Try again, connection failed: {e}")


mycursor = mydb.cursor()
mycursor.execute(f"""
DROP TABLE IF EXISTS {tablename}
""")

mycursor.execute(f"""
CREATE TABLE IF NOT EXISTS {tablename} (CountryID
int NOT NULL AUTO_INCREMENT, CountryName varchar(255) NOT NULL,
ISOcode varchar(2) NOT NULL, PRIMARY KEY (CountryID))
""")

for country in result:
    mycursor.execute(
        f"INSERT INTO {tablename} (countryName, ISOcode) VALUES (%s, %s)",
        (country["sName"], country["sISOCode"]),
    )

mydb.commit()

while True:
    sorting = input(
        "Type Y if you want alphabetical sorting by " \
        "country names and N if you want to sort by the ISO-code: "
    )

    if sorting == "Y":
        mycursor.execute(f"""
        SELECT countryName, ISOcode FROM {tablename}
        ORDER BY countryName ASC
        LIMIT 10
        """)
        break
    elif sorting == "N":
        mycursor.execute(f"""
        SELECT countryName, ISOcode FROM {tablename}
        ORDER BY ISOcode ASC
        LIMIT 10
        """)
        break
    else:
        print("Invalid input")

output = mycursor.fetchall()

for x in output:
    print(x)
