from ..models import db, Question

QUESTIONS_PER_PAGE = 10


def pagination(re, selection):
    page = re.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    formatted_data = [record.format() for record in selection[start:end]]
    return formatted_data


def get_item_or_404(db_table, id):
    return db.session.query(db_table).get_or_404(id)

