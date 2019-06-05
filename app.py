from flask import Flask,render_template


from bs4 import BeautifulSoup
# import urllib2
import urllib.request
import requests
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__)

@app.route('/')
def visa():
    try:


        headers = {
            'Authorization': 'Bearer 74efbfe29ca64e959f6c31819892a94d',
            'Content-Type': 'application/json',
        }




        city = ["Chennai", "Kolkata", "Mumbai", "New Delhi"]
        urls = [
            "https://travel.state.gov/content/travel/resources/database/database.getVisaWaitTimes.html?cid=P48&aid=VisaWaitTimesHomePage",
            "https://travel.state.gov/content/travel/resources/database/database.getVisaWaitTimes.html?cid=P100&aid=VisaWaitTimesHomePage",
            "https://travel.state.gov/content/travel/resources/database/database.getVisaWaitTimes.html?cid=P139&aid=VisaWaitTimesHomePage",
            "https://travel.state.gov/content/travel/resources/database/database.getVisaWaitTimes.html?cid=P147&aid=VisaWaitTimesHomePage"]

        cols, rows = (4, 4)
        arr = [[0 for i in range(cols)] for j in range(rows)]

        # for i in range(0, 4):
        #     response_ND = urllib2.urlopen(urls[i])
        #     html = response_ND.read()
        #     soup = BeautifulSoup(html, "html.parser")

        for i in range(0, 4):
            req = urllib.request.Request(urls[i])
            with urllib.request.urlopen(req) as response:
                the_page = response.read()


            ConvertString = the_page.decode("utf-8")
            print (type(ConvertString))
            stripString = ConvertString.strip("\r\n\r\n\r\n")
            print (stripString)
            splitString = stripString.split(",")
            for j in range(0, 4):

                arr[i][j] = splitString[j]

            x = arr[i][j].split(" ")
            z = int(x[0])

            if z < 10:
                message = "Visa date available" + str(z)
                headers = {
                    'Authorization': 'Bearer 74efbfe29ca64e959f6c31819892a94d',
                    'Content-Type': 'application/json',
                }

                data = '{"from": "+919962475678","to": [ "+916360795807" ],"body": "hi"}'

                response = requests.post('https://sms.api.sinch.com/xms/v1/a1e12ff05d99478b982ba1f393b5e385/batches',
                                         headers=headers, data=data)

        # for i in range(0, 4):
        #     for j in range(0, 4):
        #
                # if arr[i][2]<10
                #     data = '{ "from": "+919962475678","to": [ "+916360795807" ],      "body": "Hello! This is a test message from Sinch"\n    }'
                #
                #     response = requests.post(
                #         'https://sms.api.sinch.com/xms/v1/a1e12ff05d99478b982ba1f393b5e385/batches',
                #         headers=headers, data=data)

        return render_template("visa.html",C_V=arr[0][0],C_S=arr[0][1],K_V=arr[1][0],K_S=arr[1][1],
                               M_V=arr[2][0],M_S=arr[2][1],N_V=arr[3][0],N_S=arr[3][1]
                               )

    except Exception as e:
        return str(e)


if __name__=="__main__":
    app.run(debug=True)