# @hidden_cell
# The following code contains the credentials for a connection in your Project.
# You might want to remove those credentials before you share your notebook.
credentials_1 = {
    'username': '06f19f77-60dd-4eb8-86a1-ee1cb3842a9d-bluemix',
    'password': """dac845f63d70b00fa7e8ef08e31d5e2770ce6d716c4f0af9de9fe4088c4be297""",
    'custom_url': 'https://06f19f77-60dd-4eb8-86a1-ee1cb3842a9d-bluemix:dac845f63d70b00fa7e8ef08e31d5e2770ce6d716c4f0af9de9fe4088c4be297@06f19f77-60dd-4eb8-86a1-ee1cb3842a9d-bluemix.cloudantnosqldb.appdomain.cloud',
    'port': '50000',
}

# The Watson studio notebook cell


import pixiedust

username = credentials_1["username"]
password = credentials_1["password"]
host = username + '.cloudantnosqldb.appdomain.cloud'
dbName = 'iotp_us725s_gateway-data_2020-04-21' # DB name, can be found on the cloudant service

pixiedust.printAllPackages()
pixiedust.installPackage("cloudant-labs:spark-cloudant:2.0.0-s_2.11")


cloudantdata = sqlContext.read.format("com.cloudant.spark").\
option("cloudant.host", host).\
option("cloudant.username", username).\
option("cloudant.password", password).\
load(dbName)

cloudantdata.show()