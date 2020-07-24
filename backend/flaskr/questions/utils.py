from flask import abort

from ..models import db, Question


def get_item_or_404(db_table, id):
    return db.session.query(db_table).get_or_404(id)


QUESTIONS_PER_PAGE = 10


def pagination(request, selection):
    page = request.args.get("page", 1, type=int)
    if page > (len(selection)/QUESTIONS_PER_PAGE) + 1:
        # if Requested page is greater than total pages in db, then start from first element
        start = 0
    else:
        start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    formatted_data = [record.format() for record in selection[start:end]]
    return formatted_data


def format_selection(request, selection):
    formatted_questions = pagination(request, selection)
    return [formatted_questions, len(selection)]


def query_questions(request, text=None, cat_id=None):
    if text:
        questions = db.session.query(Question).filter(Question.question.ilike(f"%{text}%")).order_by(Question.id).all()
    elif cat_id:
        questions = db.session.query(Question).filter(Question.category == str(cat_id)).order_by(Question.id).all()
    else:
        questions = db.session.query(Question).order_by(Question.id).all()
    return format_selection(request, questions)


def set_attributes_all_required(instance, attrs, res):
    """strictly sets all given attributes on a given instance from a given dictionary. If any attribute value is
        missing, raise exception (Bad Request).
    @type instance: object
    @param instance: A class instance
    @type attrs: list
    @param attrs: A list of attributes
    @type res: dict
    @param attrs: dict {"attribute": value}
    @rtype: object
    @returns: a list of strings representing the header columns
    """
    if not res:
        abort(400)
    for attr in attrs:
        attr_val = res.get(attr)
        # all attributes are required
        if not attr_val:
            abort(404)
        setattr(instance, attr, attr_val)
    return instance
