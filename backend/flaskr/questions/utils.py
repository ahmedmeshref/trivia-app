from flask import abort

from ..models import db, Question

QUESTIONS_PER_PAGE = 10


def pagination(response, selection):
    page = response.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    formatted_data = [record.format() for record in selection[start:end]]
    return formatted_data


def get_item_or_404(db_table, id):
    return db.session.query(db_table).get_or_404(id)


def query_questions(response):
    questions = db.session.query(Question).order_by(Question.id).all()
    formatted_questions = pagination(response, questions)
    return [formatted_questions, len(questions)]


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
