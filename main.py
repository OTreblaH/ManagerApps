from ManagerApp.app import app

import ManagerApp.routers


if __name__ == '__main__':
    app.run(debug=True, port=80)
