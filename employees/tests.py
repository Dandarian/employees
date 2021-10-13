import pytest
from aiohttp import web
from views import get_employees, post_employee
from db import pg_context


@pytest.fixture
def cli(loop, aiohttp_client):
    app = web.Application()
    app.router.add_get('/employees', get_employees)
    app.router.add_post('/employees', post_employee)
    app.cleanup_ctx.append(pg_context)
    return loop.run_until_complete(aiohttp_client(app))


async def test_get_employees(cli):
    resp = await cli.get('/employees')
    assert resp.status == 200


async def test_get_employees_400(cli):
    resp = await cli.get('/employees?id=invalid')
    assert resp.status == 400
    assert await resp.text() == 'id\'s type is not int'


async def test_post_employee(cli):
    data = {
        'employee_name': 'Sase',
        'e_mail': '789@inc.com',
        'phone_number': 42098765,
        'inn': 4682573,
        'position': 'CEO',
        'department': 5,
        'passport': 56468798,
        'passport_issued': 'consectetur adipiscing elit, sed do eiusmod ',
        'education': 'Excepteur sint occaecat cupidatat non proident',
        'address': 'Duis aute irure dolor in reprehenderit in voluptate velit',
        'birth_date': '2021-10-20'
    }
    resp = await cli.post('/employees', data=data)
    assert resp.status == 201
    assert await resp.text() == 'employee is created'
