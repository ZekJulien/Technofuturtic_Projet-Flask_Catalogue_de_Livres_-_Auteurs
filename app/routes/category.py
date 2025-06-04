from flask import Blueprint, render_template, redirect, url_for, request
from app.services import CategoryService
from app.forms import CategoryForm

category_bp = Blueprint("category", __name__)
category_service = CategoryService()

@category_bp.route("/category/add", methods=['POST'])
def add_category():
    form = CategoryForm()
    if form.validate_on_submit():
        category_service.add_category(name=form.name.data)
        return redirect(url_for('category.category'))

@category_bp.route("/category", methods=['GET'])
def category():
    form = CategoryForm()
    categories = category_service.get_all()
    return render_template("category/category.html", form=form, categories = categories)

@category_bp.route("/category/delete/<int:id>",methods=['GET', 'DELETE'])
def delete_category(id : int):
    if category_service.delete(id):
        return redirect(url_for('category.category'))
    

@category_bp.route("/category/update",methods=['POST'])
def update_category():
    form = CategoryForm()
    category_id = request.form.get("id")
    if category_id:
        if form.validate_on_submit():
            if category_service.update(id=category_id, name=form.name.data):
                return redirect(url_for('category.category'))