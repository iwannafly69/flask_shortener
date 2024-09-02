from flask import render_template, redirect, url_for
from . import app, db
from .forms import URLForm, get_short

from .models import URLmodel


@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        url = URLmodel()
        url.original_url = form.original_url.data
        url.short = get_short()
        db.session.add(url)
        db.session.commit()
        return redirect(url_for('urls'))
    return render_template('index.html', form=form)


@app.route('/urls', methods=['GET'])
def urls():
    urls = URLmodel.query.all()
    return render_template('urls.html', urls=urls)


@app.route('/<string:short>', methods=['GET'])
def url_redirect(short):
    # Ищем сокращённую ссылку в базе данных
    url = URLmodel.query.filter_by(short=short).first()
    if url:
        url.visits += 1  # Увеличиваем количество посещений
        db.session.commit()  # Сохраняем изменения в базе данных
        return redirect(url.original_url)  # Перенаправляем на оригинальный URL
    else:
        return abort(404)  # Возвращаем ошибку 404, если ссылка не найдена
