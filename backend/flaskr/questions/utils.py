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


def set_attributes(instance, attrs, res):
    """
    set_attributes from a given dictionary on instance object
    """
    if not res:
        return False
    for attr in attrs:
        attr_val = res.get(attr)
        # all attributes are required
        if not attr_val:
            return False
        setattr(instance, attr, attr_val)
    return instance
