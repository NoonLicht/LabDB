from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Main, Name, LastName, MiddleName, Street
from output_tables import output_all_tables

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        last_name = request.form.get('last_name', '')
        first_name = request.form.get('first_name', '')
        middle_name = request.form.get('middle_name', '')
        phone = request.form.get('phone', '')
        
        main_entries = Main.query.filter(
            (Main.last_name.ilike(f'%{last_name}%')) &
            (Main.first_name.ilike(f'%{first_name}%')) &
            (Main.middle_name.ilike(f'%{middle_name}%')) &
            (Main.phone.ilike(f'%{phone}%'))
        ).all()

        output_all_tables()
        return render_template('search_results.html', main_entries=main_entries)

    main_entries = Main.query.all()
    output_all_tables()
    return render_template('index.html', main_entries=main_entries)


# Маршруты для добавления, изменения и удаления записей
@app.route('/add', methods=['POST'])
def add_entry():
    form = request.form

    new_entry = Main(
        last_name=form['last_name'],
        first_name=form['first_name'],
        middle_name=form['middle_name'],
        street=form['street'],
        house=form['house'],
        building=form['building'],
        apartment=form['apartment'],
        phone=form['phone']
    )

    # Дублирование данных в дочерних таблицах
    new_entry.names = [Name(value=form['first_name'])]
    new_entry.last_names = [LastName(value=form['last_name'])]
    new_entry.middle_names = [MiddleName(value=form['middle_name'])]
    new_entry.streets = [Street(value=form['street'])]

    db.session.add(new_entry)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_entry(id):
    entry = Main.query.get(id)

    if request.method == 'POST':
        form = request.form

        entry.last_name = form['last_name']
        entry.first_name = form['first_name']
        entry.middle_name = form['middle_name']
        entry.street = form['street']
        entry.house = form['house']
        entry.building = form['building']
        entry.apartment = form['apartment']
        entry.phone = form['phone']

        # Обновление данных в дочерних таблицах
        entry.names[0].value = form['first_name']
        entry.last_names[0].value = form['last_name']
        entry.middle_names[0].value = form['middle_name']
        entry.streets[0].value = form['street']

        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit.html', entry=entry)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_entry(id):
    entry = Main.query.get(id)

    # Удаление данных из дочерних таблиц
    db.session.delete(entry.names[0])
    db.session.delete(entry.last_names[0])
    db.session.delete(entry.middle_names[0])
    db.session.delete(entry.streets[0])

    # Удаление записи из основной таблицы
    db.session.delete(entry)
    db.session.commit()

    return redirect(url_for('index'))