from datetime import date, timedelta

import pytest
from selenium.webdriver.support import expected_conditions as EC

from pages.auth_page import AuthPage
from pages.turnos_page import TurnosPage


def future_date():
    return (date.today() + timedelta(days=14)).isoformat()


def test_anonymous_user_is_redirected_from_turnos(driver, base_url):
    driver.get(f"{base_url}/turnos")
    AuthPage(driver, base_url).wait.until(EC.url_contains("/login"))
    assert "/login" in driver.current_url


@pytest.mark.parametrize(
    ("email", "password"),
    [
        ("no-existe@example.test", "ClaveIncorrecta1!"),
        ("otra-cuenta@example.test", "OtraClaveIncorrecta1!"),
    ],
)
def test_login_rejects_unknown_credentials(driver, base_url, email, password):
    error = AuthPage(driver, base_url).login_error(email, password)
    assert "incorrectos" in error.text


def test_user_can_register_login_and_logout(driver, base_url, user_factory):
    user_factory()
    AuthPage(driver, base_url).logout()
    assert "/login" in driver.current_url


def test_user_can_list_and_search_own_booking(driver, base_url, user_factory):
    user_factory()
    reason = "Control de seguimiento QA"
    turns = TurnosPage(driver, base_url)
    message = turns.book(future_date(), "10:15", 30, reason)
    assert "reservado correctamente" in message
    assert turns.has_booking(reason), "La reserva confirmada debe aparecer en el listado."

    results = turns.search("seguimiento QA")
    assert reason in results
    no_results = turns.search("motivo-sin-coincidencias")
    assert reason not in no_results


def test_same_slot_cannot_be_reserved_twice(driver, base_url, user_factory):
    user_factory()
    turns = TurnosPage(driver, base_url)
    slot_date = future_date()
    reason = "Primera reserva de control"
    first_message = turns.book(slot_date, "11:30", 30, reason)
    assert "reservado correctamente" in first_message
    assert turns.has_booking(reason), "La primera reserva debe quedar visible antes de probar el conflicto."

    duplicate_message = turns.book(slot_date, "11:30", 15, "Intento duplicado")
    assert "ocupado" in duplicate_message
    assert "Intento duplicado" not in turns.table_text()


def test_user_can_cancel_booking(driver, base_url, user_factory):
    user_factory()
    reason = "Turno a cancelar"
    turns = TurnosPage(driver, base_url)
    message = turns.book(future_date(), "12:45", 45, reason)
    assert "reservado correctamente" in message
    assert turns.has_booking(reason)

    row_text = turns.cancel(reason)
    assert "cancelado" in row_text


@pytest.mark.parametrize("attempt", range(1, 11))
def test_success_message_is_backed_by_visible_booking(driver, base_url, user_factory, attempt):
    user_factory()
    reason = f"Persistencia QA intento {attempt}"
    turns = TurnosPage(driver, base_url)
    message = turns.book(future_date(), f"{8 + attempt:02d}:00", 30, reason)
    assert "reservado correctamente" in message
    assert turns.has_booking(reason), (
        "La UI confirmó la reserva pero la fila correspondiente no aparece en el listado."
    )