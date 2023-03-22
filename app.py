from flask import Flask
import pandas as pd
from controllers import table
from controllers import liveliness


app = Flask(__name__)

app.register_blueprint(table.tableController,url_prefix= '/table')
app.register_blueprint(liveliness.liveLinessController,url_prefix= '/liveliness')



if __name__ == '__main__':
    app.run()
