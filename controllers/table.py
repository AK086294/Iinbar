from flask import Blueprint, Response
from bl.table_service import TableService

tableController = Blueprint('table',__name__)
table_service = TableService()

@tableController.route("/getTable")
def get_table():
    return table_service.get_table().to_json(force_ascii=False)


@tableController.route("/getTableAsJson")
def export_table_as_json():
    return Response(get_table(),
             mimetype='application/json',
             headers={'Content-Disposition': 'attachment;filename=flight_output.json'})


@tableController.route("/update_excel/<excel_path>")
def update_excel(excel_path):
    return table_service.update_excle()

# @tableController.route("/update_excel/<excel_path>")
# def update_excel(excel_path):
#     return table_service.update_excle()