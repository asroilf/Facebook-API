import requests
import facebook
url = "https://graph.facebook.com/v20.0/"
token = "[PROVIDE TOKEN]"
page_id = "[ID OF THE PAGE/ACCOUNT]"

fb = facebook.GraphAPI(token)


while True:

    print("Actions you can take are: 0- exit, 1- GET posts, 2- POST, 3- DELETE, 4- GET comments, 5- POST commits. Choose the number")
    n = int(input(": "))
        if n==1:
           rq = requests.get(url+str(page_id)+"/feed?access_token="+token)
           
           if rq.status_code == 200:
               response = rq.json()
               s = len(response['data'])
               print(f"{s} posts")
               for i in response["data"]:
                   print("Posted at: " + i['created_time'] + "\n Message: " + i['message'] + "\nPost ID: " + i['id'])
                   print()
           else:
               print(rq.status_code)
           print("\n")
        if n==2:
            message = input("message: ")
    
            fb.put_object(parent_object="me",
               connection_name="feed",
               message=message,
               )
            print("done!")
        elif n==3:
            idd = input("Enter The ID: ")
            rq = requests.delete(url+idd+"?access_token="+token)
            if rq.status_code == 200:
                print("Success!")
            else:
                print(rq.status_code)
        elif n==4:
            post = input("Enter the post ID: ")
            rq = requests.get(url+post+"/comments?access_token="+token)
            response = rq.json()
            for i in response['data']:
                print("Commented at: " + i['created_time'] + "\nBy: " + i['from']['name'] + ", ID: " + i['from']['id'] + "\n Message: " + i['message'] + "\nPost ID: " + i['id'])
                print()
        elif n==5:
            replyTo = input("Enter the post ID that you want to reply: ")
            message = input("Message: ")
            fb.put_comment(object_id=replyTo, message=message)
