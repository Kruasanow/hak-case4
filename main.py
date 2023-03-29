from flask import Flask, render_template, sessions, url_for, request, session, redirect

from werkzeug.security import generate_password_hash, check_password_hash
from add_db import ins_data
from change_color import change_color
from get_values import select_values
from werkzeug.utils import secure_filename
from cleartable import outdd
from add_db import check_passw
import hack
from check_meta import get_resault

DEBUG = True 

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/home/hackaton/123/hak-case4/'
app.secret_key = 'secretkeycodecrew'

@app.template_test("jinja_is_prime")
def jinja_is_prime(n):
    if n % 2 == 0:
        return True
    else:
        return False

import os
@app.route('/', methods=['GET', 'POST'])
def index():
    print(url_for('index'))
    # from init_db import init_db
    # init_db()
    # ins_data('aaa', 'fff')
    from add_db import ins_file_data
    # ins_data('bbb','111')
    # ins_data('ccc','222')
    # ins_data('ggg','hhh')
    from find_hash import calculate_hash, calculate_string_hash,  calculate_all_hash
    # from check_meta import get_resault
    if request.method == "POST":
        passwd = request.form['passwd']
        name = request.form['name']
        session['pass'] = passwd
        session['name'] = name
        file = request.files['file']
        ins_name = file.filename

        # Сохраняем файл и получаем его путь
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], ins_name)
        file.save(file_path)
        # calc_hash = calculate_hash(file.filename)
        # calc_str_hash = calculate_string_hash(file.filename)
        # calc_all_hash = calculate_all_hash(get_resault(secure_filename(file.filename)))

        # # Получаем дату создания файла
        # file_stat = os.stat(file_path)
        # creation_time = file_stat.st_ctime

        # ins_file_data(name, ins_name, creation_time, calc_str_hash, calc_hash, calc_all_hash)

        if len(passwd) > 3 or len(name) > 3:
            print('bad len')
            good_passwd = ''
            good_name = ''
        else:
            good_passwd = passwd
            good_name = name
        print(good_name,good_passwd)
        # ins_data(passwd,name)
        # upassw(date,name)
        if check_passw(session['name'], session['pass'])[0] == True:
            from hack import prepare_for_hack
            pfh = prepare_for_hack(session['name'],session['pass'])
            print(check_passw(good_name,good_passwd)[0])
            print(good_name,good_passwd)
            hack.hidden_row(ins_name, pfh[0])
            hack.hidden_sheet(ins_name, pfh[0])

            hack.hidden_description(ins_name, pfh[0])

            hack.change_color(ins_name, pfh[1])
            try:
                print("4########################################3")
                hack.add_password(ins_name, pfh[2])
            except Exception:
                print('exception')
            dstat = 'database has been successfully tagged'
        else:
            dstat = ' not changed'
            
        calc_hash = calculate_hash(file.filename)
        calc_str_hash = calculate_string_hash(file.filename)
        calc_all_hash = calculate_all_hash(get_resault(secure_filename(file.filename)))

        # Получаем дату создания файла
        file_stat = os.stat(file_path)
        creation_time = file_stat.st_ctime

        ins_file_data(name, ins_name, creation_time, calc_str_hash, calc_hash, calc_all_hash)

        
        return render_template('index.html', dbstatus=dstat, good_name=good_name, good_passwd=good_passwd,
                               status=check_passw(good_passwd, good_name)[1], nfile=ins_name)
    return render_template('index.html', status='')


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
            # ff1 = session['name']
            arr = get_resault(ff1)
           
        return render_template('secpage.html', file2 = ff1, outarr = arr)        
        # return render_template('secpage.html', file2 = ff1, o0 = out0, o1 = out1, o2 = out2)
    return render_template('secpage.html')

@app.route('/select_base', methods=['GET', 'POST'])
def select_base():
    from date_xl_out import do_xl_by_date
    if request.method == "POST":
        if 'selected-date' in request.form:
            date_start = request.form.get("selected-date") + " 00:00:00"
            date_stop = request.form.get("selected-date-end") + " 00:00:00"
            name_file = request.form.get("text") + '.xlsx'
            do_xl_by_date(date_start,date_stop,name_file)
        
        return render_template('select_base.html', dstart=date_start, dstop=date_stop, name_file = name_file)
    
    return render_template('select_base.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    from get_datename import get_datename
    get_list = get_datename()
    if request.method == "POST":
        if 'text1' in request.form:
            name = request.form.get("text1")
            passw = request.form.get("text2")
            descr = request.form.get("text3")
            ins_data(name,passw,descr)
            status = '+User'
            
        return render_template('admin.html', status = status, getlist = get_list)
    
    return render_template('admin.html', getlist = get_list)

@app.errorhandler(404)
def error404Catch(error):
    return render_template('error404.html', Title = 'Страница не найдена'), 404
#-----LOAD------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)