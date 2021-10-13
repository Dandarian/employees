from aiohttp import web
import db


async def get_employees(request):
    id = request.query.get('id')
    if id is not None:
        if not id.isnumeric():
            return web.Response(
                text='id\'s type is not int', status=400)
        async with request.app['db'].acquire() as conn:
            cursor = await conn.execute(
                db.employee.select().where(db.employee.c.id == id))
            record = await cursor.fetchall()
            if len(record) == 0:
                return web.Response(text='employee is not found', status=404)
            employees = dict(record[0])
            return web.Response(text=str(employees))
    else:
        async with request.app['db'].acquire() as conn:
            cursor = await conn.execute(db.employee.select())
            records = await cursor.fetchall()
            employees = [dict(q) for q in records]
            return web.Response(text=str(employees))


async def post_employee(request):
    if request.method == 'POST':
        body = await request.post()

    fields = [
        'employee_name', 'e_mail', 'phone_number', 'inn', 'position',
        'department', 'passport', 'passport_issued', 'education', 'address',
        'birth_date'
    ]
    field_values = {}
    for f in fields:
        w = body.get(f)
        if w is None or w == '':
            return web.Response(text=f + ' is required', status=400)
        field_values[f] = w

    try:
        async with request.app['db'].acquire() as conn:
            await db.post_employee(conn, field_values)

        return web.Response(text='employee is created', status=201)
    except Exception:
        return web.Response(
            text='Bad request. Most likely invalid values', status=400)


async def put_employee(request):
    if request.method == 'PUT':
        body = await request.post()

    id = request.query.get('id')
    if id is None or not id.isnumeric():
        return web.Response(
            text='id is empty or it\'s type is not int', status=400)

    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(
            db.employee.select().where(db.employee.c.id == id))
        record = await cursor.fetchall()
        if len(record) == 0:
            return web.Response(text='employee is not found', status=404)

    fields = [
        'employee_name', 'e_mail', 'phone_number', 'inn', 'position',
        'department', 'passport', 'passport_issued', 'education', 'address',
        'birth_date'
    ]
    field_values = {}
    for f in fields:
        w = body.get(f)
        if w is None or w == '':
            return web.Response(text=f + ' is required', status=400)
        field_values[f] = w

    try:
        async with request.app['db'].acquire() as conn:
            await db.put_employee(conn, id, field_values)

        return web.Response(text='employee is updated')
    except Exception:
        return web.Response(
            text='Bad request. Most likely invalid values', status=400)


async def delete_employees(request):
    id = request.query.get('id')
    if id is None or not id.isnumeric():
        return web.Response(
            text='id is empty or it\'s type is not int', status=400)

    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(
            db.employee.select().where(db.employee.c.id == id))
        record = await cursor.fetchall()
        if len(record) == 0:
            return web.Response(text='employee is not found', status=404)

    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(
            db.employee.delete().where(db.employee.c.id == id))
        return web.Response(status=204)
