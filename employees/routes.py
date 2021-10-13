from views import (
    get_employees, post_employee,
    put_employee, delete_employees
)


def setup_routes(app):
    app.router.add_get('/employees', get_employees)
    app.router.add_post('/employees', post_employee)
    app.router.add_put('/employees', put_employee)
    app.router.add_delete('/employees', delete_employees)
