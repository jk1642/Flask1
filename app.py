from flask import Flask, request, redirect, render_template

app = Flask(__name__)


nextID = 2
lists = [
    {'id': 1, 'name': 'ex)박ㅇㅇ', 'contact': '010-1111-1111', 'info': '안녕하세요 저는 박ㅇㅇ입니다. 저는 .....'}
]


@app.route('/')
def index():
    return render_template('index.html', lists=lists, id=None)


@app.route('/member/<int:id>/')
def member(id):
    for list in lists:
        if id == list['id']:
            return render_template('member.html', list=list, lists=lists, id=id, show_list = False)


@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('form.html', action='/create/', button='Create', list=None, lists=lists, id=None, hide_create=True)
    elif request.method == "POST":
        global nextID
        name = request.form['name']
        contact = request.form['contact']
        info = request.form['info']
        newList = {'id': nextID, 'name': name, 'contact':contact, 'info':info}
        lists.append(newList)
        url = '/member/' + str(nextID) + '/'
        nextID = nextID + 1
        return redirect(url)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    for list in lists:
        if id == list['id']:
            if request.method == 'GET':
                return render_template('form.html', action=f'/update/{id}', button='Update', list=list, lists=lists, id=id, hide_create=True)
            elif request.method == "POST":
                global nextID
                name = request.form['name']
                contact = request.form['contact']
                info = request.form['info']
                for list in lists:
                    if id == list['id']:
                        list['name'] = name
                        list['contact'] = contact
                        list['info'] = info
                        break
                url = '/member/' + str(id) + '/'
                return redirect(url)


@app.route('/delete/<int:id>/', methods=['POST'])
def delete(id):
    for list in lists:
        if id == list['id']:
            lists.remove(list)
            break
    return redirect('/')


app.run(port=5001, debug=True)