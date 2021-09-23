from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>') # dynamically accept different url parameters to get name
def html_page(page_name):
    return render_template(page_name)

# receive data from contact form and then store it in database.txt
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')

# writing to csv file
def write_to_csv(data):
    with open('database.csv', mode='a',newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) # create a csv writer
        # writing role into the database.csv file
        csv_writer.writerow([email, subject, message]) # pass in as list

# get is when the browser wants us to send information 
# post is means that the browser wants to save information
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # check if the method is a post
    if request.method == 'POST':
        try:
            # gets the data of the email, subject, and message as a dictionary on python
            data = request.form.to_dict() # getting the data as a dictionary
            write_to_csv(data)
            return redirect('/thankyou.html') # redirect to thank you page. Which runs in the dynamic route
        except:
            return 'did not save to database'
    else:
        # if the form had a problem
        return 'something went wrong. Try again'