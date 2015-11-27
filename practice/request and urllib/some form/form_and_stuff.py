from mechanize import Browser

website = "http://in.bookmyshow.com/hyderabad"

br = Browser()    # allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Firefox')]
br.open(website)

for form in br.forms():
    try:
        if form.find_control(id='iUserName'):
            br.form = form.find_control(id='iUserName')
            
        else:
            print "nahi"
    except:
        print "except"
