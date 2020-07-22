QUESTIONS_PER_PAGE = 10


def pagination(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page-1) * 10
    end = start + 10
    formatted_data = [record.format() for record in selection]
    return formatted_data
