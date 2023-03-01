from database_utils.constants import DB_DESCRIPTION_COLUMN, DB_DATE_COLUMN, DB_AMOUNT_COLUMN, DB_IMAGE_URL_COLUMN, \
    ELEMENTS


def to_carousels(data):
    message = {
        "type": "template",
        "payload": {
            "template_type": "generic",
            "elements": []
        }
    }
    elements = []
    for single_item in data:
        single_element = {
            "title": single_item[DB_DESCRIPTION_COLUMN],
            "subtitle": f"{single_item[DB_AMOUNT_COLUMN]} on {single_item[DB_DATE_COLUMN]}",
            "image_url": single_item[DB_IMAGE_URL_COLUMN]
        }
        elements.append(single_element)
    message[ELEMENTS] = elements