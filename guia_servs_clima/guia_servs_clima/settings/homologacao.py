import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

ALLOWED_HOSTS = ['guiaservsclima.testes.necto.com.br']

DEBUG = False

sentry_sdk.init(
    dsn="https://bc030e70af6d47598cd5d5a4466da7ea@sentry.znc.com.br/55",
    integrations=[DjangoIntegration()]
)
