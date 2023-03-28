from flask import Flask, render_template, sessions, url_for, request, session, redirect

from werkzeug.security import generate_password_hash, check_password_hash
from add_db import ins_data
from change_color import change_color
from get_values import select_values
from werkzeug.utils import secure_filename
from dec import outd
from cleartable import outdd
from add_db import check_passw
import hack
from check_meta import get_resault

DEBUG = True 

app = Flask(__name__)

@app.template_test("jinja_is_prime")
def jinja_is_prime(n):
    if n % 2 == 0:
        return True
    else:
        return False

@app.route('/', methods = ['get','post'])
def index():
    print(url_for('index'))
    from init_db import init_db
    init_db()
    ins_data('aaa','fff')
    # ins_data('bbb','111')
    # ins_data('ccc','222')
    # ins_data('ggg','hhh')

    if request.method == "POST":
        passwd = request.form['passwd']
        name = request.form['name']
        file = request.files['file']
        ins_name = file.filename

        if len(passwd) != 3 or len(name) != 3:
            print('bad len')
            good_passwd = ''
            good_name = ''
            
        else:
            good_passwd = passwd
            good_name = name
            
            # ins_data(passwd,name)
            # upassw(date,name)
        if check_passw(good_passwd,good_name)[0] == True:
            hack.hidden_row(ins_name, hack.secret_message)
            hack.hidden_sheet(ins_name, hack.secret_message)
            hack.hidden_description(ins_name,hack.secret_message)
            hack.change_color(ins_name,hack.name_agent)
            hack.add_password(ins_name,hack.pass_on_excel)
            dstat = 'database has been successfully tagged'
        else:
            dstat = ' not changed'
        
        print(check_passw(good_passwd,good_name)[0])
        return render_template('index.html',dbstatus = dstat, good_name = good_name, good_passwd = good_passwd, status = check_passw(good_passwd, good_name)[1], nfile = ins_name)
    return render_template('index.html', status = '')


@app.route('/secpage', methods = ['get','post'])
def secpage():
    print(url_for('secpage'))

    # change_color(select_values()[0],select_values()[1])

    if request.method == "POST":
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            print(filename)
            ff1 = filename
            # fullway = 'output/' + str(ff1)
            # outd1 = outd(fullway)
            # out0 = outd1[0]
            # out1 = outd1[1]
            # out2 = outd1[2]

            arr = get_resault(ff1)
        
            # print('#######################################')
            # print(outd1[0])
            # print(outd1[1])
            # print(outd1[2])
            # print('#######################################')
            # outdd(fullway)
        return render_template('secpage.html', file2 = ff1, outarr = arr)        
        # return render_template('secpage.html', file2 = ff1, o0 = out0, o1 = out1, o2 = out2)
    return render_template('secpage.html')

@app.errorhandler(404)
def error404Catch(error):
    return render_template('error404.html', Title = 'Страница не найдена'), 404
#-----LOAD------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)