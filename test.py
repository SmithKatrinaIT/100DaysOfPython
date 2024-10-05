var = {

    "status": 0,

    "result": {

        "records": [

            {

                "attributes": {

                    "type": "ApexLog",

                    "url": "/services/data/v61.0/sobjects/ApexLog/07L3t00003unPRXEA2"

                },

                "Id": "07L3t00003unPRXEA2",

                "StartTime": "2024-08-21T06:41:02.000+0000",

                "LogUserId": "0053t00000AxHqOAAV",

                "LogLength": 417,

                "Location": "SystemLog"

            },

            {

                "attributes": {

                    "type": "ApexLog",

                    "url": "/services/data/v61.0/sobjects/ApexLog/07L3t00003unPRhEAM"

                },

                "Id": "07L3t00003unPRhEAM",

                "StartTime": "2024-08-21T06:41:03.000+0000",

                "LogUserId": "0053t00000AxHqOAAV",

                "LogLength": 539,

                "Location": "SystemLog"

            },

            {

                "attributes": {

                    "type": "ApexLog",

                    "url": "/services/data/v61.0/sobjects/ApexLog/07L3t00003unPRjEAM"

                },

                "Id": "07L3t00003unPRjEAM",

                "StartTime": "2024-08-21T06:41:03.000+0000",

                "LogUserId": "0053t00000AxHqOAAV",

                "LogLength": 356,

                "Location": "SystemLog"

            },

            {

                "attributes": {

                    "type": "ApexLog",

                    "url": "/services/data/v61.0/sobjects/ApexLog/07L3t00003unPRnEAM"

                },

                "Id": "07L3t00003unPRnEAM",

                "StartTime": "2024-08-21T06:41:04.000+0000",

                "LogUserId": "0053t00000AxHqOAAV",

                "LogLength": 622,

                "Location": "SystemLog"

            },

            {

                "attributes": {

                    "type": "ApexLog",

                    "url": "/services/data/v61.0/sobjects/ApexLog/07L3t00003unPRrEAM"

                },

                "Id": "07L3t00003unPRrEAM",

                "StartTime": "2024-08-21T06:41:06.000+0000",

                "LogUserId": "0053t00000AxHqOAAV",

                "LogLength": 539,

                "Location": "SystemLog"

            },

            {

                "attributes": {

                    "type": "ApexLog",

                    "url": "/services/data/v61.0/sobjects/ApexLog/07L3t00003v92IMEAY"

                },

                "Id": "07L3t00003v92IMEAY",

                "StartTime": "2024-08-21T18:08:59.000+0000",

                "LogUserId": "0054O00000AelLRQAZ",

                "LogLength": 1765,

                "Location": "Monitoring"

            },

            {

                "attributes": {

                    "type": "ApexLog",

                    "url": "/services/data/v61.0/sobjects/ApexLog/07L3t00003v92INEAY"

                },

                "Id": "07L3t00003v92INEAY",

                "StartTime": "2024-08-21T18:08:59.000+0000",

                "LogUserId": "0054O00000AelLRQAZ",

                "LogLength": 1309,

                "Location": "Monitoring"

            }

        ],

        "totalSize": 7,

        "done": True

    }

}
for val in var.items():
    print(val)
    print(val[1])
    print(var['result']['records'][val])


print("=====================\n")
print(var["result"]["records"])

