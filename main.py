from flask import Flask, render_template, sessions, url_for, request, session, redirect

from werkzeug.security import generate_password_hash, check_password_hash
from add_db import ins_data, upassw
from change_color import change_color
from get_values import select_values
from werkzeug.utils import secure_filename
from dec import outd
from cleartable import outdd
from add_db import check_passw

DEBUG = True 

app = Flask(__name__)

@app.route('/', methods = ['get','post'])
def index():
    print(url_for('index'))

    if request.method == "POST":
        passwd = request.form['passwd']
        name = request.form['name']

        if len(passwd) != 3 or len(name) != 3:
            print('bad len')
            good_passwd = ''
            good_name = ''
        else:
            good_passwd = passwd
            good_name = name
            # ins_data(passwd,name)
            # upassw(date,name)
        check_passw(good_passwd,good_name)
        print(check_passw(good_passwd,good_name))
        return render_template('index.html', good_name = good_name, good_date = good_passwd)
    return render_template('index.html')


@app.route('/secpage', methods = ['get','post'])
def secpage():
    print(url_for('secpage'))

    change_color(select_values()[0],select_values()[1])

    if request.method == "POST":
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            print(filename)
            ff1 = filename
            fullway = 'output/' + str(ff1)
            outd1 = outd(fullway)
            out0 = outd1[0]
            out1 = outd1[1]
            out2 = outd1[2]
            print('#######################################')
            print(outd1[0])
            print(outd1[1])
            print(outd1[2])
            print('#######################################')
            outdd(fullway)
        return render_template('secpage.html', file2 = ff1, o0 = out0, o1 = out1, o2 = out2)
    return render_template('secpage.html')

@app.errorhandler(404)
def error404Catch(error):
    return render_template('error404.html', Title = 'Страница не найдена'), 404
#-----LOAD------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)